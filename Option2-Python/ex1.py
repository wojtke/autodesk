import argparse
import pandas as pd

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument('--file', '-f', type=str, default='Customers.csv')
    args.add_argument('--skip-invalid', '-s', action='store_true')
    args = args.parse_args()

    df = pd.read_json("p_ex_1_runtime_parsing.json")
    invalid = ~df.length.astype(str).str.isnumeric()

    if invalid.any():
        if args.skip_invalid:
            print(f"Skipping {len(invalid)} invalid rows.")
            df = df[~invalid]
        else:
            print("The following rows have invalid length values:")
            print(df[invalid])
            print("Please fix them and try again or use the --skip-invalid flag to ignore them.")
            exit(1)

    df['length'] = df['length'].astype(int)

    # operation, which is taking the longest when summed from all entries

    ops_length = df.groupby("operation").aggregate("sum", numeric_only=True)

    print(f"The operation that takes the longest is '{ops_length.idxmax()[0]}' "
          f"with a total time of {ops_length.max()[0]} seconds.")

    # list of softwares from the one taking the longest, to the one running the shortest
    soft_time = df.groupby("software") \
                    .aggregate("sum", numeric_only=True) \
                    .sort_values(by="length", ascending=False)

    print(f"The list of softwares from the one taking the longest, to the one running the shortest:")
    print(soft_time)
