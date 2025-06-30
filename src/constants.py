import os


def find_source(path, name):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)


file_name = "Hospital_log_shortend.xes" #"Sepsis Cases - Event Log.xes"
project_path = "/home/fabian/Github/Z_Anon_Evaluation/data_xes" #os.getcwd()

source_path = find_source(project_path, file_name)
activity = "concept:name"
timestamp = "time:timestamp"
source = "org:group" # Use org:resource for bpi challenges and road traffic fine manageement
case_id = "case:concept:name"
req_cols = [case_id, activity, timestamp, source]

# results path
res_path = f"{project_path}/res"
if not os.path.exists(res_path):
    os.makedirs(res_path)

# Evaluation

multiprocessing = True
multiprocessing_quantifying_risk = True

# write things to disk
write_simplified_log = False
write_middle_results = True

# abstract timestamps
abstract_timestamps = True
# abtraction_level = "d"
# abstractionLevel =



