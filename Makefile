all: project bandwidth btest

project: project.c fisheryates.c
	mpicc  -I /home/dparker/R/codes-base/install/include -I \
	/home/dparker/R/codes-net/install/include -L /home/dparker/R/ROSS/install/lib \
	-L /home/dparker/R/codes-base/install/lib -L /home/dparker/R/codes-net/install/lib \
	project.c fisheryates.c -I /home/dparker/R/ROSS/install/include -l ROSS -lm -l \
	codes-net -l codes-base  -o project -Wall -lbsd -g

bandwidth: bandwidth.c fisheryates.c
	mpicc  -I /home/dparker/R/codes-base/install/include -I \
	/home/dparker/R/codes-net/install/include -L /home/dparker/R/ROSS/install/lib \
	-L /home/dparker/R/codes-base/install/lib -L /home/dparker/R/codes-net/install/lib \
	bandwidth.c fisheryates.c -I /home/dparker/R/ROSS/install/include -l ROSS -lm -l \
	codes-net -l codes-base  -o bandwidth -Wall -lbsd -g

btest: btest.c fisheryates.c
	mpicc  -I /home/dparker/R/codes-base/install/include -I \
	/home/dparker/R/codes-net/install/include -L /home/dparker/R/ROSS/install/lib \
	-L /home/dparker/R/codes-base/install/lib -L /home/dparker/R/codes-net/install/lib \
	btest.c fisheryates.c -I /home/dparker/R/ROSS/install/include -l ROSS -lm -l \
	codes-net -l codes-base  -o btest -Wall -lbsd -g

clean:
	rm project bandwidth btest