"""

 Created on 15-Jan-21
 @author: Kiril Zelenkovski

"""
import math
from sklearn.preprocessing import OrdinalEncoder, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import CategoricalNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd

# Read csv
dataset = pd.read_csv("dataset.csv")
dataset = dataset.drop("Address Region", 1)
dataset = dataset.drop("Street Address", 1)
dataset = dataset.drop("Address Locality", 1)
dataset = dataset.drop("Postal Code", 1)
dataset = dataset.drop("Price", 1)
dataset = dataset.values.tolist()

# Split dataset (85% train, 15% test)
# test_csv = dataset[math.ceil(0.75 * len(dataset)):]
# train_csv = dataset[0:math.ceil(0.75 * len(dataset))]

# Use Ordinal Encoder to encode categorical features as an integer array
encoder = OrdinalEncoder()
encoder.fit([dataset[j][:-1] for j in range(0, len(dataset))])

X_dataset = [dataset[j][:-1] for j in range(0, len(dataset))]
y_dataset = [dataset[j][-1] for j in range(0, len(dataset))]

X, X_test, y, y_test = train_test_split(X_dataset,
                                        y_dataset,
                                        test_size=0.5,
                                        random_state=42)
X = encoder.fit_transform(X)
# Random Forest Classifier: Meta estimator that fits a # of decision tree classifiers on sub-samples of a dataset
classifier = RandomForestClassifier(n_estimators=10, criterion='entropy', random_state=0)

# Fit Random Forest Classifier according to X,y
classifier.fit(X, y)

# Setup X values for test_csv
X_test = encoder.fit_transform(X_test)

# # Calculate and print accuracy
y_predicted = [classifier.predict([x])[0] for x in X_test]
print(f'RandomForrest accuracy: {accuracy_score(y_test, y_predicted, normalize=True):.4f}')

print(y_predicted)
print(y_test)

le = LabelEncoder()
le.fit([dataset[j][-1] for j in range(0, len(dataset))])

list(le.classes_)

y_predicted = le.transform(y_predicted)
y_test = le.transform(y_test)

print(y_predicted)
print(y_test)