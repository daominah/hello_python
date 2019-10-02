import os

logDir = "/var/log"
fs = os.listdir(logDir)
dpkgLogs = []
for f in fs:
    if f.find("dpkg") == -1: continue
    if f.find(".gz") != -1: continue
    dpkgLogs.append(f)


class Package:
    def __init__(self):
        self.name = ""
        self.status = ""
        self.version = ""
        # installed datetime
        self.time = ""

    def __str__(self):
        return "{0:<20}{1:<30}{2:<15}{3}".format(
            self.time, self.name, self.status, self.version)


packages = {}
for logFilePath in dpkgLogs:
    f = open(logDir + "/" + logFilePath)
    while True:
        line = f.readline()
        if not line: break
        # if line.find(" installed") == -1: continue

        # line = "2019-03-01 09:53:53 status half-installed libllvm3.4:amd64 1:3.4-1ubuntu3"
        words = line.split()
        p = Package()
        p.name = words[-2]
        p.version = words[-1]
        p.status = words[3]
        p.time = words[0] + 'T' + words[1]

        # choose the last installation
        if (p.name in packages) and (p.time < packages[p.name].time): continue
        packages[p.name] = p

packagesList = list(packages.values())
packagesList.sort(key=lambda e: e.time, reverse=True)
for p in packagesList:
    print(p)
