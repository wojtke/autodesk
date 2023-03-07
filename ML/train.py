import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.preprocessing import StandardScaler
import pickle
import argparse

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--file', '-f', type=str, default='Customers.csv')
    args = args.parse_args()

    df = pd.read_csv(args.file)

    X, y = df[['Salary', 'Age']], df['Purchased']

    # add polynomial features
    poly = PolynomialFeatures(degree=2, include_bias=False)
    X = poly.fit_transform(X)

    # split data into train and test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    # scale data
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    # train model
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # evaluate model
    print(classification_report(y_test, model.predict(X_test)))

    print("Coefficients:")
    for name, c in zip(poly.get_feature_names_out(['Salary', 'Age']), model.coef_[0]):
        print(f"  {name}: {c:.3f}")

    # save model
    with open('model.pkl', 'wb') as f:
        pickle.dump((model, sc), f)








