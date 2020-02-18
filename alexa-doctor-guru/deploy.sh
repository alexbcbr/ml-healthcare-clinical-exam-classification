# Deploy alexa skill based on lambda
sam validate
sam package --template-file template.yaml --s3-bucket alexbc.app.dev.us-east-2 --output-template-file packaged.yaml
sam deploy --template-file packaged.yaml --stack-name alexa-skill
rm packaged.yaml
