import psutil
import pandas as pd
import time

stats = {
    'Time': [],
    'CPU Percentage': [],
    'CPU Thread 1': [],
    'CPU Thread 2': [],
    'CPU Thread 3': [],
    'CPU Thread 4': [],
    'CPU Thread 5': [],
    'CPU Thread 6': [],
    'CPU Thread 7': [],
    'CPU Thread 8': [],
    'CPU Thread 9': [],
    'CPU Thread 10': [],
    'CPU Thread 11': [],
    'CPU Thread 12': [],
    'Bandwidth Usage': [],
}

for _ in range(60):
    stats['Time'].append(time.time())
    stats['CPU Percentage'].append(psutil.cpu_percent(interval=1))
    
    threads = psutil.cpu_percent(interval=1, percpu=True)
    for i in range(1,13):
        stats[f'CPU Thread {i}'].append(threads[i-1])

    ans = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
    stats['Bandwidth Usage'].append(ans)


df = pd.DataFrame(stats)
df.to_csv('System_Network_Stats.csv', index=False)
