"""

 Created on 16-Jan-21
 @author: Kiril Zelenkovski

"""
from sklearn.model_selection import train_test_split
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
dataset = dataset.values.tolist()

# Use Ordinal Encoder to encode categorical features as an integer array
encoder = OrdinalEncoder()
encoder.fit([dataset[j][:-1] for j in range(0, len(dataset))])

X_dataset = [dataset[j][:-1] for j in range(0, len(dataset))]
y_dataset = [dataset[j][-1] for j in range(0, len(dataset))]

X, test_x, y, test_y = train_test_split(X_dataset,
                                        y_dataset,
                                        test_size=0.5,
                                        random_state=42)


model = LogisticRegression(solver='liblinear', random_state=0)
model.fit(X, y)

# Set accuracy variable to 0
acc = 0

# Add up accuracy using predict function
for j in range(0, len(test_x)):
    predict = model.predict([test_x[j]])
    if predict[0] == test_y[j]:
        acc += 1
predicted = [model.predict([test_x[j]])[-1] for j in range(0, len(test_x))]
# Print accuracy score
print(f"Logistic regression accuracy: {(acc / len(test_x)):.4f}")

print(predicted)
print(test_y)

le = LabelEncoder()
le.fit([dataset[j][-1] for j in range(0, len(dataset))])

list(le.classes_)

predicted = le.transform(predicted)
test_y = le.transform(test_y)

print(predicted)
print(test_y)




