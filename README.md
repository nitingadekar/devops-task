# Devops Tasks
Sample task to get Hand-on with devops tools and flow. 



##### Task 1: Git
Create a Github repo and clone it locally, Commit a README.md file and push it to the repo. 
Create a branch name `test-branch` and update the Readme file in this branch with sample files and raise a merge request to the main branch. 
Approve the merge request after

--- 

##### Task 2: Python
Write a rest api using Python flask framework to return current time and date in json format.
Host the api on 8080 port no. Execute the script locally and make sure the date and time is returned in json format.
Push the code in github repo


Reference: https://flask-restful.readthedocs.io/en/latest/quickstart.html#a-minimal-api

---

##### Task 3: Docker
Write a docker file to containerise above python app. 
Execute the docker container locally by forwarding the app port on local and verify the api is accessible 
Push the Dockerfile in the github repo

Reference:  https://docs.docker.com/language/python/build-images/

---

##### Task 4: Github Pipeline
Use Github actions to write a CI pipeline 
Create a new registry in [dockerhub.com](https://hub.docker.com/)

Checkout the python app and the Dockerfile from above steps 
Build the docker image with the pipeline no. as tag to the docker image
Push the docker image to the docker registry created above

Reference: https://docs.github.com/en/actions/guides/publishing-docker-images

---

##### Task 5: Terraform AWS 

Create an AWS account.
Create new IAM user with Programmatic access and policy to access AWS S3 service, EC2 services. 
Install and configure AWS cli with above credentials. 

Write a terraform script to launch an EC2 instance with public IP assigned, SSH key, security group rule 22 and 8080 port open for your IP or for the internet. 
Store the terraform state in s3 bucket. 

Push the terraform scripts to the github repo

Reference: https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/instance

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

Install kubernetes on AWS using Kops. 
Master Nodes: 1
Worker Nodes: 1
Kube API endpoint: Public
Use official documentation below. 
https://kubernetes.io/docs/setup/production-environment/tools/kops/
Short reference 
https://github.com/nitingadekar/k8s-basics#kubernetese-basic


---

##### Task 8: Helm

Write a Helm chart to render a deployment and service so that the above docker image in Task 3 can be executed.
Ref: https://helm.sh/docs/helm/helm_create/ 
```
Service type: NodePort/Loadbalancer/ClusterIP
Deployment.Port:8080
service.port: 80
Replicas:1
```

Render the template on local and confirm the manifest after rendering.    
Ref: https://helm.sh/docs/helm/helm_template/   
Package the helm chart using helm package on local.    
Ref: https://helm.sh/docs/helm/helm_package/    
Deploy the chart in default namespace using helm install.    
Ref: https://helm.sh/docs/helm/helm_install/   
Deploy same chart in 3 different namespaces (dev,qa,stg) using helm options.    
Ref: https://helm.sh/docs/helm/helm_install/#options    
Update the docker image tag with any changes, and update the deployed application version by updating image tag in helm chart.    
Ref: https://helm.sh/docs/helm/helm_upgrade/    

Push the helm chart to github repo 



