# devops-task
Sample task to get Hand-on on devops tools and flow. 

---

##### Task 1: Git
Create a Github repo and clone it locally, Commit a README.md file and push it to the repo. 
Create a branch name `test-branch` and update the Readme file in this branch with sample files and raise a merge request to the main branch. 
Approve the merge request after

--- 

##### Task 2: Python
Write a rest api using Python to return current time and date in json format.
Host the api on 8080 port no. Execute the script locally and make sure the date and time is returned in json format.

###### Tools
**Scripting:** Python
**Framework:** Flask 

**Reference:** https://flask-restful.readthedocs.io/en/latest/quickstart.html#a-minimal-api

---

##### Task 3: Docker
Write a docker file to containerise above python app. 
Execute the docker container locally by forwarding the app port on local and verify the api is accessible 

**Reference:**  https://docs.docker.com/language/python/build-images/

---

##### Task 4: Github Pipeline
Use Github actions to write a CI pipeline 
Create a new registry in [dockerhub.com](https://hub.docker.com/)

Checkout the python app and the Dockerfile from above steps 
Build the docker image with the pipeline no. as tag to the docker image
Push the docker image to the docker registry created above

**Reference:** https://docs.github.com/en/actions/guides/publishing-docker-images

---

##### Task 5: Terraform AWS 

Create an AWS account.
Create new IAM user with Programmatic access and policy to access AWS S3 service, EC2 services. 
Install and configure AWS cli with above credentials. 

Write a terraform script to launch an EC2 instance with public IP assigned, SSH key, security group rule 22 and 8080 port open for your IP or for the internet. 

---

##### Task 6: Ansible

Install ansible with latest version 
Write an ansible inventory with above EC2 credentials
Write ansible playbook to 
- Install Docker on the server
- Add the default user to Docker group
- Pull the docker image pushed in Task 4. 
- Run the docker image on the server and map the port of container on the host port 8080

Execute the playbook and verify if the python rest api is accessible on the Public IP of the EC2 public IP.

---

##### Task 7: Kubernetes

