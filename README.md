# Keyprod
This project is  app (a todo-listcommande and ) with a Python FastAPI backend. It is hosted on serverless AWS infrastructure using Lambda.

## Build the Docker Image
```bash
# Only work on UNIX (Mac/Linux) systems!
docker build -t myimage .
```
## Start  Docker 
```bash
# Start the Docker container
docker run -d --name mycontainer -p 80:80 myimage
```
## Check it  
```bash
# http://127.0.0.1/docs

```
## Use FastAPI uvicorn without Docker
```bash
# Install FastApi
pip install fastapi
###############
```
```bash
# Install uvicorn standard
pip install "uvicorn[standard]"
###############
```
## Open app in KEYPROD
```bash
# open folder
cd app
###############
```
## Run it
```bash
# Run App 
uvicorn main:app --reload
###############
```
## Check it  
```bash
#  http://127.0.0.1:8000/docs

```

## Url in Serverless / AWS Lambda
The `/KEYPROD` folder contains the CDK code to deploy all the infrastructure 
Lambda function to your AWS account.

(https://cssukn4vc2glb2gw7hbprpyip40iojsu.lambda-url.eu-north-1.on.aws/docs)
