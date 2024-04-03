# Beginner code for fail2ban proxy detection banning
import pandas as pd
from io import StringIO
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, ConfusionMatrixDisplay
from sklearn.model_selection import RandomizedSearchCV, train_test_split
from scipy.stats import randint

HEADERS = '$remote_addr|$time_local|$request|$http_user_agent|$ssl_protocol|$ssl_cipher|$ssl_rtt|$tcpinfo_state|$tcpinfo_ca_state|$tcpinfo_retransmits|$tcpinfo_probes|$tcpinfo_backoff|$tcpinfo_options|$tcpinfo_snd_wscale|$tcpinfo_rcv_wscale|$tcpinfo_delivery_rate_app_limited|$tcpinfo_fastopen_client_fail|$tcpinfo_rto|$tcpinfo_ato|$tcpinfo_snd_mss|$tcpinfo_rcv_mss|$tcpinfo_unacked|$tcpinfo_sacked|$tcpinfo_lost|$tcpinfo_retrans|$tcpinfo_fackets|$tcpinfo_last_data_sent|$tcpinfo_last_ack_sent|$tcpinfo_last_data_recv|$tcpinfo_last_ack_recv|$tcpinfo_pmtu|$tcpinfo_rcv_ssthresh|$tcpinfo_rtt|$tcpinfo_rttvar|$tcpinfo_snd_ssthresh|$tcpinfo_snd_cwnd|$tcpinfo_advmss|$tcpinfo_reordering|$tcpinfo_rcv_rtt|$tcpinfo_rcv_space|$tcpinfo_total_retrans|$tcpinfo_pacing_rate|$tcpinfo_max_pacing_rate|$tcpinfo_bytes_acked|$tcpinfo_bytes_received|$tcpinfo_segs_out|$tcpinfo_segs_in|$tcpinfo_notsent_bytes|$tcpinfo_min_rtt|$tcpinfo_data_segs_in|$tcpinfo_data_segs_out|$tcpinfo_delivery_rate|$tcpinfo_busy_time|$tcpinfo_rwnd_limited|$tcpinfo_sndbuf_limited|$tcpinfo_delivered|$tcpinfo_delivered_ce|$tcpinfo_bytes_sent|$tcpinfo_bytes_retrans|$tcpinfo_dsack_dups|$tcpinfo_reord_seen|$tcpinfo_rcv_ooopack|$tcpinfo_snd_wnd'
header_count = len(HEADERS.split("|"))
TRAINING_FILE = './training_file.csv'
OS_TRAINING_FILE = './os_training_file.csv'


def receive_row(data):
   content = HEADERS + "\n" + data
   df = pd.read_csv(StringIO(content), sep="|")
   df["$http_user_agent_code"], uniques = pd.factorize(df["$http_user_agent"])
   df = df.drop(columns=['$http_user_agent','$http_user_agent','$ssl_protocol','$ssl_cipher', '$remote_addr', '$time_local', '$request'])
   return df

def receive_row_os_detection(data):
   content = HEADERS + "\n" + data
   df = pd.read_csv(StringIO(content), sep="|")
   df = df.drop(columns=['$http_user_agent','$ssl_protocol','$ssl_cipher', '$remote_addr', '$time_local', '$request', '$ssl_rtt', '$tcpinfo_rtt', '$tcpinfo_rttvar', '$tcpinfo_min_rtt'])
   return df

accuracy = 0
def train_data():
   features = pd.read_csv(TRAINING_FILE, sep="|")
   labels = np.array(features['$is_proxy']) # this could switch to operating system, user agent, and proxy at some point
   features_ml = features.drop(columns=['$is_proxy','$ssl_protocol','$ssl_cipher', '$remote_addr', '$time_local', '$request'])
   features_ml["$http_user_agent_code"], uniques = pd.factorize(features_ml["$http_user_agent"])
   features_ml = features_ml.drop(columns=['$http_user_agent'])
   feature_list = list(features_ml.columns)
   features_ml = np.array(features_ml)
   train_features, test_features, train_labels, test_labels = train_test_split(features_ml, labels, test_size = 0.25, random_state = 42)
   rf = RandomForestClassifier()
   rf.fit(train_features, train_labels)
   label_pred = rf.predict(test_features)
   accuracy = accuracy_score(test_labels, label_pred)
   print(accuracy)
   print(rf.feature_importances_)
   feature_importances = rf.feature_importances_

   # Print or sort them for interpretation
   print(feature_importances)

   # Sort features by importance (descending)
   feature_importances_weights = feature_importances[::-1]
   sorted_idx = feature_importances.argsort()[::-1]
   sorted_features = [f"{features.columns[i]}:{feature_importances[i]}" for i in sorted_idx] 
   print("Most important features:", sorted_features[:15])  # Top 5 features
   return rf
agents = ['Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML like Gecko) Chrome/120.0.0.0 Safari/537.36',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36',
 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0',
 'Mozilla/5.0 (Android 13; Mobile; rv:109.0) Gecko/116.0 Firefox/116.0',
 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) CriOS/121.0.6167.138 Mobile/15E148 Safari/604.1',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML',
 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0',
 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/111.0',
 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML',
 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36',
 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0',
 'Mozilla/5.0 (X11; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0',
 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36',
 'com.apple.WebKit.Networking/19617.1.17.11.12 CFNetwork/1490.0.4 Darwin/23.2.0',
 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/601.2.4 (KHTML',
 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML',
 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML' 'curl/7.67.0',
 'com.apple.WebKit.Networking/8617.1.17.10.9 CFNetwork/1490.0.4 Darwin/23.2.0',
 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTM Llike Gecko) Version/17.2 Mobile/15E148 Safari/604.1',
 'Mozilla/5.0 (X11; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0']

def train_data_os_detection():
   features = pd.read_csv(OS_TRAINING_FILE, sep="|")
   features["$http_user_agent_code"], uniques = pd.factorize(features["$http_user_agent"])
   labels = np.array(features['$http_user_agent_code']) # this could switch to operating system, user agent, and proxy at some point
   features_ml = features.drop(columns=['$is_proxy','$http_user_agent','$http_user_agent_code','$ssl_protocol','$ssl_cipher', '$remote_addr', '$time_local', '$request', '$ssl_rtt', '$tcpinfo_rtt', '$tcpinfo_rttvar', '$tcpinfo_min_rtt'])
   feature_list = list(features_ml.columns)
   features_ml = np.array(features_ml)
   train_features, test_features, train_labels, test_labels = train_test_split(features_ml, labels, test_size = 0.25, random_state = 42)
   rf = RandomForestClassifier()
   rf.fit(train_features, train_labels)
   label_pred = rf.predict(test_features)
   accuracy = accuracy_score(test_labels, label_pred)
   print(accuracy)
   print(rf.feature_importances_)
   feature_importances = rf.feature_importances_

   # Print or sort them for interpretation
   print(feature_importances)

   # Sort features by importance (descending)
   feature_importances_weights = feature_importances[::-1]
   sorted_idx = feature_importances.argsort()[::-1]
   sorted_features = [f"{feature_list[i]}:{feature_importances[i]}" for i in sorted_idx] 
   print("Most important features:", sorted_features[:15])  # Top 5 features
   return rf



random_forest = train_data_os_detection()
line = input("Line from logs of Nginx to predict: ")
prediction = random_forest.predict(receive_row_os_detection(line))
print(prediction)
print(agents[prediction[0]])
def process_new_line(data):
   new_line_df = receive_row(data)
   is_proxy_prediction = random_forest.predict(new_line_df)
   
