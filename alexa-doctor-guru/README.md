# alexa-doctor-guru

This project contains the Alexa Skill to provide patient diagnostic using SAM CLI.
In order to deploy all resources, you can run the sript 

./deploy.sh

This script will deploy the lambda function and lambda layer in us-east-2. The function has a dependency on Lambda Layer which contains 
libraries for alexa development kit (ask) and internacionalization. You need to run lambda layer

./lambda-layer/deploy-lambda-layer.sh

This environment was developed in a local machine (MacOS) with Visual Studio Code

## Dependencies to deploy the Alexa skill

To use the SAM CLI, you need the following tools.

* SAM CLI - [Install the SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* [Python 3 installed](https://www.python.org/downloads/)
* Docker - [Install Docker community edition](https://hub.docker.com/search/?type=edition&offering=community)

### Resources
See the [AWS SAM developer guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html) for an introduction to SAM specification, the SAM CLI, and serverless application concepts.