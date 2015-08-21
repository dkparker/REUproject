#!/bin/bash

set -x

while getopts ":s" OPT
do
    case $OPT in
    s)
	RDR="s"
	;;
    \?)
        echo "Invalid option: -$OPTARG"
	;;
    esac
done

declare -a nodes=(100 250 500 1000)

for NUM in ${nodes[@]}
do
    ./bandwidth --codes-config=bandwidth$NUM.conf > band$NUM$RDR.dat
done
