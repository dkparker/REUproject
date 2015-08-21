
dorstats = []
rdrstats = []
results = []

with open("dorstats.dat", 'r') as f:
    f = f.readlines()
    for i in range(1,5):
        words = f[i].split()
        med = float(words[1])
        nf = float(words[3])
        dorstats.append([med,nf])

with open("rdrstats.dat", 'r') as f:
    f = f.readlines()
    for i in range(1,5):
        words = f[i].split()
        med = float(words[1])
        nf = float(words[3])
        rdrstats.append([med,nf])

for i in range(4):
    medpercent = 1 - rdrstats[i][0]/dorstats[i][0]
    nfpercent = 1 - rdrstats[i][1]/dorstats[i][1]
    results.append([medpercent, nfpercent])

for item in results:
    print "medpercent:", item[0], "nfpercent:", item[1]
