#!/bin/bash

#create the destination directory
mkdir -p /mnt/c/bd-a1/service-result

#copy output files from the container
docker cp bd-a1:/home/doc-bd-a1/res_dpre.csv /mnt/c/bd-a1/service-result/
docker cp bd-a1:/home/doc-bd-a1/eda-in-1.txt /mnt/c/bd-a1/service-result/
docker cp bd-a1:/home/doc-bd-a1/eda-in-2.txt /mnt/c/bd-a1/service-result/
docker cp bd-a1:/home/doc-bd-a1/eda-in-3.txt /mnt/c/bd-a1/service-result/
docker cp bd-a1:/home/doc-bd-a1/vis.png /mnt/c/bd-a1/service-result/
docker cp bd-a1:/home/doc-bd-a1/k.txt /mnt/c/bd-a1/service-result/

#Stop the container
docker stop bd-a1

echo "All files have been copied to /mnt/c/bd-a1/service-result/ and the container has been stopped."

