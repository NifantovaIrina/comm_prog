# comm_prog


For running first task (comm_prog):
Terminal 1:
*sudo docker-compose build 
*sudo docker-compose up
Terminal 2:
*sudo docker build -t producer producer
*docker run -it --network=commprog_net producer
