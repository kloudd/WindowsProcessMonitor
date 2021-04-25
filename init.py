PROCESS_LIST = ["python.exe", "steam.exe"]

INTERVAL = 5  # in seconds

PROCESS_ATTRS = ['pid', 'name', 'memory_info']
# pid', 'memory_percent', 'name', 'cmdline', 'cpu_times',
# 'create_time', 'memory_info', 'status', 'nice', 'username


NUMBER_OF_PROCESSES_TO_VIEW = 25

COLUMNS = "name,cpu_usage,memory_usage,read_bytes,write_bytes,status,create_time,nice,n_threads,cores"

SORT_BY = "memory_usage"