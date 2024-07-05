A fake RESTful API that delivers made up data on a few endpoints. The data sits within 
a zip file and needs to be decompressed programmatically. 

Steps To run the project
1. Unzip the project folder
2. change the current directory to project's parent directory which is FlaskDemo
3. Create a Virtual Environment
   python -m venv venv
4. Activate the Virtual Environment
   Windows:
   venv\Scripts\activate
   macOS/Linux:
   source venv/bin/activate
5. Install Dependencies
   pip install -r requirements.txt
6. python main.py

Steps to run locally in IDE.
1. Import the project.
2. In the terminal type the below command
   pip install -r requirements.txt
3. Click on the run button

Swagger UI:
http://localhost:5000/docs/

Command to run unit tests:
python -m pytest

Todo/Improvements:
1. add proper logging
2. add more exception handling
3. add a config file to read hard-coded file names
4. Containerise the applicaiton using Docker.
5. Deploy the application on AWS.