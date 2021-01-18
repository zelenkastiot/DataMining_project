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
dataset = dataset.drop("Price", 1)
dataset = dataset.drop("Beds", 1)
print(dataset)
columns = dataset.columns.tolist()
dataset = dataset.values.tolist()

# Use Ordinal Encoder to encode categorical features as an integer array
encoder = OrdinalEncoder()
encoder.fit([dataset[j][:-1] for j in range(0, len(dataset))])

# Split dataset 75% train, 25% test
# test_csv = dataset[math.ceil(0.75 * len(dataset)):]
# train_csv = dataset[0:math.ceil(0.75 * len(dataset))]

X_dataset = [dataset[j][:-1] for j in range(0, len(dataset))]
y_dataset = [dataset[j][-1] for j in range(0, len(dataset))]

X, X_test, y, y_test = train_test_split(X_dataset,
                                        y_dataset,
                                        test_size=0.2,
                                        random_state=42)

# Call encoder.transform or encoder.fit_transform to transform the data (because it is strings and int)
X = encoder.transform(X)

# Decision Tree Classifier: A non-parametric supervised learning method used for classification
classifier = DecisionTreeClassifier(criterion='entropy', random_state=0)

# Fit Decision Tree Classifier according to X, y
classifier.fit(X, y)

# Call encoder.transform to transform the data
X_test = encoder.transform(X_test)

# Print accuracy using imported metrics
y_predicted = [classifier.predict([x])[0] for x in X_test]
print(f'DecisionTreeClassifier accuracy: {accuracy_score(y_test, y_predicted, normalize=True):.4f}')

# Print depth for classifier
print('Depth:', classifier.get_depth())

# Print # of leaves for classifier
print('Number of leaves:', classifier.get_n_leaves())

# Load importance of features in list
feature_importance = list(classifier.feature_importances_)

# Most and least important feature
most_important_feature = feature_importance.index(max(feature_importance))
least_important_feature = feature_importance.index(min(feature_importance))

# Print both
print('Most important feature:', columns[most_important_feature])
print('Least important feature:', columns[least_important_feature])
print(feature_importance)

for i in range(0, len(feature_importance)):
    print(columns[feature_importance.index(feature_importance[i])])

print(y_predicted)
print(y_test)

le = LabelEncoder()
le.fit([dataset[j][-1] for j in range(0, len(dataset))])

list(le.classes_)

y_predicted = le.transform(y_predicted)
y_test = le.transform(y_test)

print(y_predicted)
print(y_test)