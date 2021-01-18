"""

 Created on 15-Jan-21
 @author: Kiril Zelenkovski

"""

import math
from sklearn.preprocessing import OrdinalEncoder, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import CategoricalNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import pandas as pd

# Read csv
dataset = pd.read_csv("dataset.csv")
dataset = dataset.drop("Address Region", 1)
dataset = dataset.drop("Street Address", 1)
dataset = dataset.drop("Address Locality", 1)
dataset = dataset.drop("Postal Code", 1)
print(dataset)
dataset = dataset.values.tolist()

# Use Ordinal Encoder to encode categorical features as an integer array
encoder = OrdinalEncoder()
encoder.fit([dataset[j][:-1] for j in range(0, len(dataset))])

# Split dataset (75% train, 25% test)
#test_csv = dataset[math.ceil(0.75 * len(dataset)):]
# train_csv = dataset[0:math.ceil(0.75 * len(dataset))]

X_dataset = [dataset[j][:-1] for j in range(0, len(dataset))]
y_dataset = [dataset[j][-1] for j in range(0, len(dataset))]

X, X_test, y, y_test = train_test_split(X_dataset,
                                        y_dataset,
                                        test_size=0.5,
                                        random_state=42)

# Call encoder.transform or encoder.fit_transform to transform the data (because it is strings and int)
X = encoder.fit_transform(X)

# Naive Bayes classifier for categorical features, we use this because we have non-integer values in dataset
clf = CategoricalNB()

# Fit the model with X, y
clf.fit(X, y)

# Call encoder to transform X_test
X_test = encoder.fit_transform(X_test)

# Predict y for X_test values
y_predicted = [clf.predict([x])[0] for x in X_test]

# Print accuracy score
print(f"CategoricalNaiveBayes accuracy: {accuracy_score(y_test, y_predicted, normalize=True):.4f}")

print(y_predicted)
print(y_test)

le = LabelEncoder()
le.fit([dataset[j][-1] for j in range(0, len(dataset))])

list(le.classes_)

y_predicted = le.transform(y_predicted)
y_test = le.transform(y_test)

print(y_predicted)
print(y_test)
