""" 
This is a class for invoking ML model for breast cances
@author: Alex Coqueiro
@date: Feb, 2 2020
"""

import boto3
import sagemaker
import json
import numpy as np

from sagemaker.predictor import RealTimePredictor

ENDPOINT = "breast-cancer-detection-api-v1"
sess = sagemaker.Session()
predictor = RealTimePredictor(endpoint=ENDPOINT, sagemaker_session=sess)

def predict_breast_cancer(image_path):
	""" 
	  The function to predict if one image has cancer 

	  Parameters: 
	      image_path (Image): Breast image 
	      
	  Returns: 
	      predicted_class: A binary number which indicates 0 no cancer detected and 1 cancer detected
	"""
	with open(image_path, 'rb') as f:
		payload = f.read()
		payload = bytearray(payload)
	response = predictor.predict(payload)
	result = json.loads(response)

	print('Probabilities for all classes: ', result)
	predicted_class = np.argmax(result)

	return predicted_class
