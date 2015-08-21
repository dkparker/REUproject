import sys
import subprocess
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


with open("btest.conf", 'r') as f:
    lines = f.readlines()
    count = 10
    for size in [2**n for n in range(20)]:
        lines[14] = "  packet_size=\""+str(size)+"\";\n"
        lines[22] = "  chunk_size=\""+str(size)+"\";\n"
        lines[29] = "  payload_sz=\""+str(size)+"\";\n"
        lines[30] = "  num_messages=\""+str(count)+"\";\n"
        line = "btestSize" + str(size) + "Count" + str(count) + ".conf"
        with open(line, 'w') as g:
            for l in lines:
                g.write(l)
                          
        output = subprocess.check_output(["./btest", "--codes-config="+line])
        with open(line[:-5]+".dat", 'w') as g:
            g.write(output)
        outlines = output.split('\n')
        for oline in outlines:
            try:
                if oline[0] == "^":
                    latency = float(oline.split()[16])
                    time = float(oline.split()[7])
            except IndexError:
                continue
        print size, ",", latency, ",", time
