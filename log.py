from collections import Counter

logfile = "server.log"

ips = []

with open(logfile) as f:
    for line in f:
        parts = line.split()
        ips.append(parts[0])

counter = Counter(ips)

print("Top Suspicious IPs")

for ip,count in counter.most_common(5):
    print(ip,count)
