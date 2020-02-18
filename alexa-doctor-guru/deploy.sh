#!/bin/bash
# Deploy alexa skill based on lambda
# deploy.sh - Deploy a lambda environment returning ARN of lambda
#
# Revisions:
# Versao 1.0 - First version for MacOSX and Linux

sam validate
sam package --template-file template.yaml --s3-bucket alexbc.app.dev.us-east-2 --output-template-file packaged.yaml
sam deploy --template-file packaged.yaml --stack-name alexa-skill
rm packaged.yaml
stack_physical_resource_id=$(aws cloudformation describe-stack-resources --stack-name alexa-skill --logical-resource-id DoctorGuru --query 'StackResources[*].[PhysicalResourceId]' --output text)
echo "arn:aws:lambda:us-east-2:771620814942:function:"$stack_physical_resource_id
