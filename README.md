<!--- Register repository https://api.reuse.software/register, then add REUSE badge:
[![REUSE status](https://api.reuse.software/badge/github.com/SAP-samples/REPO-NAME)](https://api.reuse.software/info/github.com/SAP-samples/REPO-NAME)
-->

# [Kyma Deploy]

## Description
A machine learning architecture that enables the simple deployment of containerized pre-trained models. Easily plug in a trained model to the predefined architecture, deploy to Kyma runtime and create a flexible prediction endpoint to solve business-critical problems.
## Requirements
1. SAP BTP account

- [Create trial BTP Account](https://developers.sap.com/tutorials/hcp-create-trial-account.html)

2. SAP Kyma environment is enabled

- [Kyma getting started](https://developers.sap.com/tutorials/cp-kyma-getting-started.html)

3. Docker environment and a Docker Hub account is required.
- [Install Docker on Mac link](https://docs.docker.com/desktop/mac/install)
- [Install Docker on Windows link](https://docs.docker.com/desktop/windows/install/)
- [Create Docker Hub account (dockerID) at link](https://hub.docker.com/)

4. Commands are run in Mac terminal, but if you are using Windows please execute in your Windows Terminal.

5. Verify cURL is working in Mac terminal.
Usually it is pre-installed in Mac OS. Type curl -V in Mac terminal and you should be able to see its help information. If it’s not installed, refer to online information, or follow these steps:

In Mac terminal, run: `ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" < /dev/null 2> /dev/null`
Enter your Mac's user password (if required during installation) then wait for the installation to finish. 
Run the following command in the terminal: brew install curl
 
Curl should also be preinstalled on Windows but if not refer to the [official documentation](https://curl.se/) for installation instructions.
## Download and Installation
### Build Docker Image and Push to Docker Hub
1.  Download the source code and unzip it locally. 
- This example is a python flask application providing prediction service using a linear regression model. It runs on port 8888 and serves a post request to the service. We will discuss more details later, but for now, let's create a folder called kyma_ml_example and put all the source files inside.

2.  Open Mac terminal and make sure you are in the kyma_ml_example directory (since we will run all the commands from there).

3.  Make sure Docker is installed and Docker Desktop is running. You should be able to see the Docker version with the following command: docker -v.

4. Build a Docker image with this command: docker build -t kyma-ml-example .
- Please notice there is a dot at the end of the command.

5. Run command `docker images` to make sure the image is already in the repository.

6.  Run command `docker login` to login to Docker Hub using your Docker Hub account (dockerID and password). 

7.  Tag your image with your dockerID : `docker tag kyma-ml-example [your dockerId]/kyma-ml-example`

8.  And then push to your own public image repository: `docker push [your dockerId]/kyma-ml-example`  You can go to hub.docker.com, log in and check if your image is already uploaded.


### Deploy and run your machine learning model on SAP Kyma
1. Now we are going to run our machine learning service on SAP Kyma where you can easily monitor the health of your service, benefit from auto-scaling, load balancing, and more.
- Please make sure you have a BTP account and get Kyma enabled as mentioned in the prerequisites.
- Open SAP BTP Cockpit ([link](https://account.hana.ondemand.com/cockpit/)) and open your subaccount page. Find Kyma console URL under Kyma Environment tab.

2. Click "link to dashboard" to open Kyma dashboard and then add dev namespace.

3. Open deployment.yaml file with a text editor and replace ‘your-dockerID’ with your real dockerID(docker hub account) at line 31. Save the file.

4. Enter your dev space and choose Deploy new workload->Upload YAML->Browse your deployment.yaml file. Then click Deploy.

5. Go back to your dev space, you should be able to see two running pods after deployment.

6. On Kyma dashboard, go to Discover and Network->API Rules.
- We will create an API rule since we want to expose a restful API to accept POST requests. For our case, we can just simply set value ‘kymamlexample’ for fields Name and Hostname. Then click create. 
- Note down the full url (which will look like the following 'kymamlexample.d4d833f.kyma.shoot.live.k8s-hana.ondemand.com'.

7. Now open your API url in browser.

### Testing your machine learning API

1. We will test our prediction service using the machine learning model in our source code.

2.  We will send a post request with some json data to our API using a curl command. The command looks like this:

- `curl -H "Content-Type: application/json" -X POST -d ‘your_json_data’ API_URL/predict`

3. You can copy the content from file ‘sample_data.json’ in our source folder and replace your_json_data in the command. You will also need to replace API_URL with the one we created earlier.

If everything is OK, you should be able to see the predicted result after the predictions attribute
## Known Issues

## How to obtain support
[Create an issue](https://github.com/SAP-samples/<repository-name>/issues) in this repository if you find a bug or have questions about the content.
 
For additional support, [ask a question in SAP Community](https://answers.sap.com/questions/ask.html).

## Contributing
If you wish to contribute code, offer fixes or improvements, please send a pull request. Due to legal reasons, contributors will be asked to accept a DCO when they create the first pull request to this project. This happens in an automated fashion during the submission process. SAP uses [the standard DCO text of the Linux Foundation](https://developercertificate.org/).

## License
Copyright (c) 2022 SAP SE or an SAP affiliate company. All rights reserved. This project is licensed under the Apache Software License, version 2.0 except as noted otherwise in the [LICENSE](LICENSES/Apache-2.0.txt) file.
