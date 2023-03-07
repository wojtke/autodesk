import pickle
import argparse
import pandas as pd

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--file', '-f', type=str, required=True)
    parser.add_argument('--output', '-o', type=str, default=None)
    args = parser.parse_args()

    df = pd.read_csv(args.file)
    with open('model.pkl', 'rb') as f:
        model, sc = pickle.load(f)

    X = df[['Salary', 'Age']]
    poly = PolynomialFeatures(degree=2, include_bias=False)
    X = poly.fit_transform(X)
    X = sc.transform(X)

    y_pred = model.predict(X)

    if args.output is None:
        print(y_pred)
    else:
        df['Purchased'] = y_pred
        df.to_csv(args.output, index=False)




