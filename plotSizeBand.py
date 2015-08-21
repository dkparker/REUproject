import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import sys
import getopt

trials = 0
hops = [0 for i in range(16)]
other_data = []
rdr = ""

def toRdBl(val): #val between 0 and 1
    if val <= 0.5:
        return [val, val, 1 - val]
    else:
        return [val, 1 - val, 1 - val]
    
list = ["100", "250", "500", "1000"]
datasets = []

def usage():
    print "Usage: python plotSizeBand.py [-s]"

if len(sys.argv) > 1:
    if sys.argv[1] == "-s":
        rdr = "s"
    else:
        usage()
        exit()

for item in list:
    new_data = {}
    data = []
    with open("band" + item + rdr + ".dat", 'r') as f:
        for line in f:
            if line[0] == "$":
                words = line.split()
                sender = int(words[3])
                receiver = int(words[8])
                num_hops = int(words[10])
                if receiver not in new_data.keys():
                    new_data[receiver] = [num_hops, sender, 0]
                else:
                    if new_data[receiver][1] != sender:
                        print "uh oh pairs disagree", receiver,new_data[receiver][1], sender
                        exit(1)
                if new_data[receiver][0] != num_hops:
                    print "uh oh hops disagree, old ", new_data[receiver][0],\
                        " new ", num_hops
                    exit(1)
            if line[0] == "^":
                words = line.split()
                avgLatency = float(words[16])
                num_hops = int(words[21])
                sender = int(words[2])
                if float(words[7]) != 0.0:
                    data.append([avgLatency,num_hops,sender])
                    hops[num_hops] += 1
                
            if "number of hops" in line:
                words = line.split()
                other_hops = int(float(words[5]))
                other_latency = float(words[9])
                other_data.append([other_latency,other_hops])
#mixdata = [[data[i][0],other_data[i][1]] for i in range(len(data))]

    for datum in data:
        new_data[datum[2]][2] = datum[0]
    datasets.append(new_data)

fig = plt.figure(1)
#fig.set_size_inches(10,10)
ax = fig.add_subplot(111)
colors = "rgby"

print "DOR Results:"

for i, new_data in enumerate(datasets):
    newer_data = []
    for key in new_data.keys():
        if new_data[key][2] != 0:
            newer_data.append([new_data[key][2],new_data[key][0]])
    new_data = newer_data
    new_data = map(lambda x: [(8192*10)/float(x[0])/1000.0, x[1]], new_data)
    print "Median: ", np.median(map(lambda x: x[0], new_data)), "95%:", \
        np.percentile(map(lambda x: x[0], new_data),95)
    new_data.sort(key=lambda x: x[0])
    yvals = np.arange(len(new_data))/float(len(new_data))
    plt.axis([0,5,0.0,1.0])

    cm = plt.cm.get_cmap('bwr')

    ax.scatter(map(lambda x: x[0],new_data),yvals, s=30, lw=0, label = list[i] + " nodes",\
                   color = colors[i])
    
plt.xlabel("Average Bandwidth(GB/s)")
plt.ylabel("Relative Frequency")
plt.legend(loc=2)
plt.savefig("bandMulti" + rdr + ".png", bbox_inches="tight")
