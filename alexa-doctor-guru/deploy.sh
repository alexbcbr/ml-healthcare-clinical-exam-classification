#!/bin/sh
# Deploy alexa skill based on lambda
# deploy.sh - Deploy a lambda environment returning ARN of lambda
#
# Revisions:
# Versao 1.0 - First version for MacOSX and Linux
# Versao 1.1 - Add steps to test the function with invoke

echo "*********** LAMBDA DEPLOYMENT **********"
sam validate
sam package --template-file template.yaml --s3-bucket alexbc.app.dev.us-east-2 --output-template-file packaged.yaml
sam deploy --template-file packaged.yaml --stack-name alexa-skill --parameter-overrides Locale=es
rm packaged.yaml
stack_physical_resource_id=$(aws cloudformation describe-stack-resources --stack-name alexa-skill --logical-resource-id DoctorGuru --query 'StackResources[*].[PhysicalResourceId]' --output text)
echo "\n***************** LAMBDA LOG **********************"
aws lambda invoke --function-name $stack_physical_resource_id --invocation-type RequestResponse --payload file://events/start-skill-request.json events/response.json --log-type Tail --query 'LogResult' --output text |  base64 -D

echo "\n****************** LAMBDA RESPONSE ***************"
cat events/response.json
rm events/response.json

echo "\n\n*********** LAMBDA ARN for Alexa Skill **********"
echo "arn:aws:lambda:us-east-2:771620814942:function:"$stack_physical_resource_id
echo "\n********************** END **********************"
