""" 
This is a class for invoking ML model for diabetes readmission
@author: Alex Coqueiro
@date: Feb, 9 2020
"""

import boto3
import sagemaker
import json
#import numpy as np

from sagemaker.predictor import RealTimePredictor

ENDPOINT = "diabetes-readmission"
sess = sagemaker.Session()

pCSV = RealTimePredictor(endpoint=ENDPOINT, 
                              sagemaker_session=sess,
                              content_type="text/csv",
                              accept="text/csv")

def predict_diabetes(diabetes_data):
	response = pCSV.predict(diabetes_data)
	result = json.loads(response)		
	return result