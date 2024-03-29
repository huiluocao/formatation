#!/bin/bash

dir_size=1000
dir_name="./HGM60664"
n=$((`find ./HGM60664/*.fna -maxdepth 1 -type f | wc -l`/$dir_size+1))
for i in `seq 1 $n`;
do
    mkdir -p "$dir_name$i";
    find ./HGM60664/*.fna -maxdepth 1 -type f | head -n $dir_size | xargs -I '{}' mv {} "$dir_name$i"
done


for i in `seq 1 10`; do mkdir -p "new$i"; find . -type f -maxdepth 1 | head -n 300 | xargs -i mv "{}" "new$i"; done
