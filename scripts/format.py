# Formatting CSVs to be read by machine learning algorithms
import csv
import pandas as pd
from io import StringIO
import sys
headers = "$remote_addr,$time_local,$request,$http_user_agent,$ssl_protocol,$ssl_cipher,$ssl_rtt,$tcpinfo_state,$tcpinfo_ca_state,$tcpinfo_retransmits,$tcpinfo_probes,$tcpinfo_backoff,$tcpinfo_options,$tcpinfo_snd_wscale,$tcpinfo_rcv_wscale,$tcpinfo_delivery_rate_app_limited,$tcpinfo_fastopen_client_fail,$tcpinfo_rto,$tcpinfo_ato,$tcpinfo_snd_mss,$tcpinfo_rcv_mss,$tcpinfo_unacked,$tcpinfo_sacked,$tcpinfo_lost,$tcpinfo_retrans,$tcpinfo_fackets,$tcpinfo_last_data_sent,$tcpinfo_last_ack_sent,$tcpinfo_last_data_recv,$tcpinfo_last_ack_recv,$tcpinfo_pmtu,$tcpinfo_rcv_ssthresh,$tcpinfo_rtt,$tcpinfo_rttvar,$tcpinfo_snd_ssthresh,$tcpinfo_snd_cwnd,$tcpinfo_advmss,$tcpinfo_reordering,$tcpinfo_rcv_rtt,$tcpinfo_rcv_space,$tcpinfo_total_retrans,$tcpinfo_pacing_rate,$tcpinfo_max_pacing_rate,$tcpinfo_bytes_acked,$tcpinfo_bytes_received,$tcpinfo_segs_out,$tcpinfo_segs_in,$tcpinfo_notsent_bytes,$tcpinfo_min_rtt,$tcpinfo_data_segs_in,$tcpinfo_data_segs_out,$tcpinfo_delivery_rate,$tcpinfo_busy_time,$tcpinfo_rwnd_limited,$tcpinfo_sndbuf_limited,$tcpinfo_delivered,$tcpinfo_delivered_ce,$tcpinfo_bytes_sent,$tcpinfo_bytes_retrans,$tcpinfo_dsack_dups,$tcpinfo_reord_seen,$tcpinfo_rcv_ooopack,$tcpinfo_snd_wnd,$msec,$request_time,$usec,$start_usec"
header_count = len(headers.split(","))
lines = open("/var/log/nginx/access.log").readlines()
def validate_row(row):
    # Check if number of elements in the row matches expected number of headers
    print(len(lines[row-1].split(",")), header_count)
    return len(lines[row-1].split(",")) <= header_count


pd.set_option('display.max_rows', None)
pd.set_option('max_colwidth', 100)
with open('/var/log/nginx/access.log') as csvfile:
  csv_content = csvfile.read().replace("KHTML,", "KHTML").replace("Expanse,","").replace("company,","").replace("scans,","").replace("Xpanse,","").replace("concerns,","")
  csv_file = headers + "\n" + csv_content.replace('-','0')
  df = pd.read_csv(StringIO(csv_file), sep=",", skiprows=lambda x: not validate_row(x))
  print(df[['$remote_addr', '$http_user_agent', '$tcpinfo_options', '$tcpinfo_snd_wscale', '$tcpinfo_snd_wnd', '$tcpinfo_data_segs_out', '$tcpinfo_data_segs_in', '$msec', '$request_time']])
  df.to_csv('updated.csv', index=False)
  print(df.query(sys.argv[1]))
 # print(pd.get_dummies(df))
