import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

trials = 0
data = []
hops = [0 for i in range(16)]
other_data = []
new_data = {}

def toRdBl(val): #val between 0 and 1
    if val <= 0.5:
        return [val, val, 1 - val]
    else:
        return [val, 1 - val, 1 - val]
    

with open("lat1000.dat", 'r') as f:
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

print new_data, data

for datum in data:
    new_data[datum[2]][2] = datum[0]

data.sort(key=lambda x: x[0])
yvals = np.arange(len(data))/float(len(data))
plt.figure(1)
plt.axis([0,100,0.0,1.0])
plt.scatter(map(lambda x: x[0],data),yvals, c=map(lambda x: toRdBl(x[1]/15.0), data),s=30, lw=0)
plt.xlabel("Average Latency (us)")
plt.ylabel("Relative Frequency")
#plt.savefig('res500s.png', bbox_inches='tight')

#plt.figure(2)
#plt.plot(hops, "o")
#plt.savefig('hops500s.png')

#plt.figure(3)
#other_data.sort(key=lambda x: x[0])
#yvals = np.arange(len(other_data))/float(len(other_data))
#plt.axis([0,100,0.0,1.0])
#plt.scatter(map(lambda x: x[0]*2,other_data),yvals, c=map(lambda x: toRdBl(x[1]/15.0), other_data),s=30, lw=0)
#plt.xlabel("Average Latency (us)")
#plt.ylabel("Relative Frequency")
#plt.axis([0.0,0.002,0.0,1.0])                                                                    
#plt.savefig('ores500s.png', bbox_inches='tight')

#plt.figure(4)
#mixdata.sort(key=lambda x: x[0])
#yvals = np.arange(len(mixdata))/float(len(mixdata))
#plt.axis([0,100,0.0,1.0])
#plt.scatter(map(lambda x: x[0]*1000000,mixdata),yvals, c=map(lambda x: toRdBl(x[1]/15.0), other_data),s=30, lw=0)
#plt.xlabel("average Latency (us)")
#plt.ylabel("Relative Frequency")
#plt.savefig('mres500s.png', bbox_inches='tight')

plt.figure(5)
fig, ax = plt.subplots()
newer_data = []
for key in new_data.keys():
    if new_data[key][2] != 0:
        newer_data.append([new_data[key][2],new_data[key][0]])
new_data = newer_data
new_data.sort(key=lambda x: x[0])
yvals = np.arange(len(new_data))/float(len(new_data))
plt.axis([0,25,0.0,1.0])

print new_data

cm = plt.cm.get_cmap('bwr')

plt.scatter(map(lambda x: x[0],new_data),yvals, c=map(lambda x: x[1], new_data), cmap=cm, s=30, lw=0)
cbar = plt.colorbar()
cbar.set_label('network hops')
plt.xlabel("Average Latency (us)")
plt.ylabel("Relative Frequency")
plt.savefig("lat1000.png", bbox_inches="tight")
