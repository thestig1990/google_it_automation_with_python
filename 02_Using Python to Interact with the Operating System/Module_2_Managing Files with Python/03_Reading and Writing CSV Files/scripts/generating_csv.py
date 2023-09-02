import csv

hosts = [["workstation.local", "192.168.25.46"], ["webserver.cloud", "10.2.5.6"]]

with open("hosts.csv", "w") as host_csv:
    writer = csv.writer(host_csv)
    writer.writerows(hosts)