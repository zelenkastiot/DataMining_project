"""

 Created on 16-Jan-21
 @author: Kiril Zelenkovski

"""
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score, make_scorer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder, LabelEncoder
import math

# Read csv
dataset = pd.read_csv("dataset.csv")
dataset = dataset.drop("Address Region", 1)
dataset = dataset.drop("Street Address", 1)
dataset = dataset.drop("Address Locality", 1)
dataset = dataset.drop("Postal Code", 1)
dataset = dataset.drop("Price", 1)

# print(len(dataset))
# print(len(dataset['Address Locality'].unique()))
# print(len(dataset['Street Address'].unique()))
# print(len(dataset['Type'].unique()))
# train_csv = dataset[0:math.ceil(0.75 * len(dataset))]
# print(len(train_csv['Address Locality'].unique()))
# print(len(train_csv['Street Address'].unique()))
# print(len(train_csv ['Type'].unique()))
dataset = dataset.values.tolist()

# Use Ordinal Encoder to encode categorical features as an integer array
encoder = OrdinalEncoder()
encoder.fit([dataset[j][:-1] for j in range(0, len(dataset))])

# Split dataset (75% train, 25% test)
test_csv = dataset[0:math.ceil(0.25 * len(dataset)):]
train_csv = dataset[math.ceil(0.25 * len(dataset)):]

# Load train examples, X
X = [train_csv[j][:-1] for j in range(0, len(train_csv))]

# Call encoder.transform or encoder.fit_transform to transform the data (because it is strings and int)
X = encoder.fit_transform(X)

# Load train examples, y
y = [train_csv[j][-1] for j in range(0, len(train_csv))]

model = LogisticRegression(solver='liblinear', random_state=0)
model.fit(X, y)

# Set accuracy variable to 0
acc = 0

test_x = encoder.fit_transform([test_csv[j][:-1] for j in range(0, len(test_csv))])
test_y = [test_csv[j][-1] for j in range(0, len(test_csv))]

# Add up accuracy using predict function
for j in range(0, len(test_csv)):
    predict = model.predict([test_x[j]])
    if predict[0] == test_csv[j][-1]:
        acc += 1
predicted = [model.predict([test_x[j]])[-1] for j in range(0, len(test_csv))]
# Print accuracy score
print(f"Logistic regression accuracy: {(acc / len(test_csv)):.4f}")

print(predicted)
print(test_y)

le = LabelEncoder()
le.fit([dataset[j][-1] for j in range(0, len(dataset))])

list(le.classes_)

predicted = le.transform(predicted)
test_y = le.transform(test_y)

print(predicted)
print(test_y)