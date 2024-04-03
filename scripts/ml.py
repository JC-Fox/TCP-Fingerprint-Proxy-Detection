#pandas is used for data manipulation
import pandas as pd

#read in data and display first 5 rows
features = pd.read_csv('./tester.csv')
features.head(5)
please_predict = pd.read_csv('./updated.csv')
please_predict = please_predict.drop(columns=['$msec', '$request_time','$usec', '$start_usec', '$http_user_agent', '$remote_addr', '$time_local', '$request', '$ssl_protocol', '$ssl_cipher', '$tcpinfo_min_rtt', '$ssl_rtt', '$tcpinfo_rtt'])
print(please_predict.columns)
#please_predict = pd.get_dummies(please_predict)

#Descriptive statistics for each column

import numpy as np
labels = np.array(features['$http_user_agent'])
features = features.drop(columns=['$http_user_agent','$ssl_protocol','$ssl_cipher', 'Unnamed: 60',
       'Unnamed: 61', 'Unnamed: 62', 'Unnamed: 63', 'Unnamed: 64', '$tcpinfo_min_rtt', '$ssl_rtt', '$tcpinfo_rtt'])
#features.drop('$ssl_protocol', axis=1)
#features.drop('$ssl_cipher', axis=1)
print(features.columns)
#one-hot encode the data using pandas get_dummies
print(features.head(1))

#display the first 5 rows of the last 12 columns
features.iloc[:,5:].head(5)

#Use numpy to convert to arrays
#labels are the values we wanna predict
#labels = np.array(features['http_user_agent'])

#Remove the labels from the features
#axis 1 refers to the columns

#saving feature names for later use
feature_list = list(features.columns)
print(feature_list)
#convert to numpy array
features = np.array(features)

print('Done')

#Using Skicit-learn to split data into training and testing sets
from sklearn.model_selection import train_test_split

#Split the data into training and testing sets
train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size = 0.25, random_state = 42)

print('Training Features Shape:', train_features.shape)
print('Training Labels Shape:', train_labels.shape)
print('Testing Features Shape:', test_features.shape)
print('Testing Labels Shape:', test_labels.shape)

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, ConfusionMatrixDisplay
from sklearn.model_selection import RandomizedSearchCV, train_test_split
from scipy.stats import randint


from sklearn.tree import export_graphviz
from IPython.display import Image
import graphviz


rf = RandomForestClassifier()

rf.fit(train_features, train_labels)

label_pred = rf.predict(test_features)

accuracy = accuracy_score(test_labels, label_pred)
print("Accuracy: ", accuracy)


lookup_agent = {
1: "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML like Gecko) Chrome/120.0.0.0 Safari/537.36",
2: "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0",
3: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36",
4: "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0",
5: "Mozilla/5.0 (Android 13; Mobile; rv:109.0) Gecko/116.0 Firefox/116.0",
6: "Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) CriOS/121.0.6167.138 Mobile/15E148 Safari/604.1",
7: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML",
8: "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0",
9: "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/111.0",
10: "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0",
11: "Mozilla/5.0 (X11; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0",
12: "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36",
13: "com.apple.WebKit.Networking/19617.1.17.11.12 CFNetwork/1490.0.4 Darwin/23.2.0",
14: "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/601.2.4 (KHTML",
15: "curl/7.67.0",
16: "Mozilla/5.0 (iPhone; CPU iPhone OS 17_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTM Llike Gecko) Version/17.2 Mobile/15E148 Safari/604.1"  
}


predictions = rf.predict(please_predict)
print(predictions)
num = int(input(f"Number betwee 0-{len(please_predict)-1}"))
print(please_predict.iloc[num])
print(lookup_agent[predictions[num]])
feature_importances = rf.feature_importances_

# Print or sort them for interpretation
print(feature_importances)

# Sort features by importance (descending)
feature_importances_weights = feature_importances[::-1]
sorted_idx = feature_importances.argsort()[::-1]
sorted_features = [f"{please_predict.columns[i]}:{feature_importances[i]}" for i in sorted_idx] 
print("Most important features:", sorted_features[:15])  # Top 5 features

param_dist = {'n_estimators': randint(50,500),'max_depth': randint(1,20)}

rand_search = RandomizedSearchCV(rf, param_distributions=param_dist, n_iter=5, cv=5)

rand_search.fit(train_features, train_labels)

best_rf = rand_search.best_estimator_

print("Best hyperparameters: ", rand_search.best_params_)

