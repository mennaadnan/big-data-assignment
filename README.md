PREREQUISITES
1- Docker Desktop
2- Ubuntu Terminal
3- Visual Studio Code

git clone (https://github.com/mennaadnan/big-data-assignment.git)
cd bd-a1

mkdir bd-a1
cd bd-a1
docker build -t bd-a1-image .
docker run -it --name bd-a1 bd-a1-image

docker exec -it bd-a1 bash

#create python files and load them inside the container
python3 load.py orders.csv

#exit container

#create final.sh file and run it

bash final.sh
