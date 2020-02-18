#!/bin/bash

# Undeploy alexa skill based on lambda
# deploy.sh - Deploy a lambda environment returning ARN of lambda

aws cloudformation delete-stack --stack-name alexa-skill --region us-east-2

