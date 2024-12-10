import glob
import itertools
import json
import pandas as pd

import os; os.chdir(os.path.dirname(os.path.abspath(__file__)))

throughput_data = {}  # Initialize the dictionary
srtt_data = {}
cwnd_data= pd.DataFrame()
time_data= pd.DataFrame()
srtt_data_all= pd.DataFrame()


# Assuming the files in the current directory follow a pattern like '*-result.json'
# Adjust the pattern as necessary to match your file naming convention
result_files_pattern = '*-result.json'
result_ss_files='*-ss.csv'
throughput_data = {}  # Initialize the dictionary
srtt_data = {}


columns = ['timestamp', 'flow ID', 'cwnd', 'srtt']

for result_file in glob.glob(result_files_pattern):
    # Extract the base name (without '-result.json') to use in other file references
    base_name = result_file.replace('-result.json', '')

    # Load the JSON output file into a Python object
    with open(result_file) as f:
        iperf3_data = json.load(f)

    throughput_data[base_name] = iperf3_data['end']['sum_received']['bits_per_second'] / (1000000 * 1)  # to convert Mbit
    
    
for result_file in glob.glob(result_ss_files):
    # Extract the base name (without '-result.json') to use in other file references
    base_name = result_file.replace('-ss.csv', '')

    # Average SRTT for Each Flow
    df_f1 = pd.read_csv(result_file, names=columns)

    # Filter out rows with flow ID = 4, they are for the control flows
    df_f1 = df_f1[df_f1['flow ID'] != 4].reset_index(drop=True)

    average_RTT_f1 = df_f1['srtt'].mean()
    
    cwnd_data[base_name] = df_f1['cwnd']
    time_data[base_name] = df_f1['timestamp']
    srtt_data[base_name] = average_RTT_f1
    srtt_data_all[base_name] = df_f1['srtt']

# Save throughput_data to a JSON file
with open('throughput_data.json', 'w') as f:
    json.dump(throughput_data, f)

# Save srtt_data to a JSON file
with open('srtt_data.json', 'w') as f:
    json.dump(srtt_data, f)
    
cwnd_data.to_csv("consolidated_cwnd_data.csv", index=False)
srtt_data_all.to_csv("srtt_all.csv", index=False)
time_data.to_csv("consolidated_time_data.csv", index=False)