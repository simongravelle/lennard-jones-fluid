#!/bin/bash

set -e

raw_data=raw-data/
if [ ! -d "$raw_data" ];
then
    mkdir $raw_data
fi

for T in 0.6 0.8 1.0 1.2 1.4 1.6 1.8 2.0 2.2 2.4 2.6 2.8 3.0 3.2
do

    folder=${raw_data}T${T}/
    if [ ! -d "$folder" ];
    then
        mkdir $folder
        cd inputs
            newline='T_star = '${T}
            oldline=$(cat prepare_simulation_Grivet2005.py | grep 'T_star = ')
            sed -i '/'"$oldline"'/c\'"$newline" prepare_simulation_Grivet2005.py
            python3 prepare_simulation_Grivet2005.py
       	cd ..
        cp inputs/parameters.lammps $folder
        cp inputs/input.lammps $folder
    else
        echo 'Folder '${folder}'exist already, skipped'
    fi
done
