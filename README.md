A fake RESTful API that delivers made up data on a few endpoints. The data sits within 
a zip file and needs to be decompressed programmatically. 

# Steps To run the project in local machine
1. Create a Virtual Environment
   python -m venv venv
2. Activate the Virtual Environment
   Windows:
   venv\Scripts\activate
   macOS/Linux:
   source venv/bin/activate
3. Install Dependencies
   pip install -r requirements.txt
4. python main.py

# Steps to run locally in IDE.
1. Import the project.
2. In the terminal type the below command
   pip install -r requirements.txt
3. Click on the run button

# Swagger UI for local run:
http://localhost:5000/swagger/

# Command to run unit tests:
python -m pytest

# Steps to run the Docker image in local machine(Docker must be installed)
#docker build -t your_image_name .
docker build -t python-flask-demo:0.0.1.RELEASE .

#Run the image -d means detached mode i.e run in the background;5000 is the port on my machine 
#docker run -d -p imageport:port on my machine your_image_name
docker run -d -p 3000:5000 python-flask-demo:0.0.1.RELEASE

#Check if the container is running
docker container ls

#Test app running in docker image on browser
http://localhost:3000/swagger

#Stop
docker container stop f86

# Todo/Improvements:
1. add proper logging
2. add more exception handling
3. add a config file to read hard-coded file names
4. Containerise the applicaiton using Docker.
5. Deploy the application on AWS.