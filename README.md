## PREREQUISITES
1. Docker Desktop
2. Ubuntu Terminal
3. Visual Studio Code
   ***

git clone (https://github.com/mennaadnan/big-data-assignment.git) <br />
mkdir bd-a1 <br />
cd bd-a1 <br />

docker build -t bd-a1-image . <br />
docker run -it --name bd-a1 bd-a1-image <br />
docker exec -it bd-a1 bash <br />
#create python files and load them inside the container <br />
python3 load.py orders.csv <br />
#exit container <br />
#create final.sh file and run it <br />
bash final.sh
