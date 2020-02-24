#!/bin/bash
# Prepare library for lamdba layer
# deploy-lambda-layer.sh - Deploy a lambda environment returning ARN of lambda
#

echo "*********** LAMBDA LAYER GENERATION **********"
virtualenv venv
venv/bin/pip install -r requirements.txt
mv venv python
zip -r lambda-layer-alexa-sdk-i18n.zip *
rm -r python

aws s3 cp lambda-layer-alexa-sdk-i18n.zip s3://alexbc.app.dev.us-east-2/
rm lambda-layer-alexa-sdk-i18n.zip
echo "*********** END **********"