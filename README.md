# MISC-python


# To create a Docker build 
'''
docker build -t ip-tool .

'''

# To Run the docker Image to Check the collision 

'''
 docker run --rm -v $(pwd)/network.json:/app/network.json ip-tool --check-collision /app/network.json

'''


# To Run Docker-Compose file 


'''
docker-compose up 

'''
