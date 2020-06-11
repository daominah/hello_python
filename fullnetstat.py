import subprocess

stdout = subprocess.check_output('netstat -tlnp'.split(' ')).decode('utf-8')
netstatLines = stdout.split('\n')
pids = {}
localAddrs = {}
for i in range(len(netstatLines)):
    if i > 0:
        # tcp 0 0 127.0.0.1:63342 0.0.0.0:* LISTEN 2646/java
        words = [w for w in netstatLines[i].split(' ') if w != '']
        if len(words) > 6:
            # 2646/java
            slash = words[6].find('/')
            if slash != -1:
                pid = words[6][:slash]
                pids[i] = pid
                localAddrs[i] = words[3]

paths = {}
for i, pid in pids.items():
    stdout = subprocess.check_output('ps {}'.format(pid).split(' ')).decode(
        'utf-8')
    lines = stdout.split('\n')
    if len(lines) > 1:
        # 2646 ? Sl 2:14 /home/tungdt/opt/GoLand -classpath lib/bootstrap.jar
        words = [w for w in lines[1].split(' ') if w != '']
        if len(words) > 4:
            path = ' '.join(words[4:])
            paths[i] = path

fullLines = []
for i in pids:
    fullLine = '{:20}{:9}{}'.format(localAddrs[i], pids[i], paths[i])
    fullLines.append(fullLine)

result = '\n\n'.join(fullLines)
print(result)