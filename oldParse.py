import fileinput
import matplotlib.pyplot as plt

trials = 0
data = [[0,0] for x in range(150)] #for now...

with open("results.dat", 'r') as f:
    for line in f:
        words = line.split()
        hops = int(float(words[5]))
        avg_latency = float(words[9])
        trials += 1
        data[hops-1][0] += 1
        data[hops-1][1] += avg_latency

for i in range(150):
    data[i][1] /= 150

print data
plt.plot(data)
plt.show()

