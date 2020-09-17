sudo docker container stop mycontainer
sudo docker system prune -f
sudo docker build -t myimage .
sudo docker run -d --name mycontainer -p 5000:5000 myimage