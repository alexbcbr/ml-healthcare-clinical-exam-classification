import boto3
import sagemaker
import json
import numpy as np

from sagemaker.predictor import RealTimePredictor

ENDPOINT = "breast-cancer-detection-api-v1"

sess = sagemaker.Session()

print(sess.boto_region_name)

predictor = RealTimePredictor(endpoint=ENDPOINT,
                              sagemaker_session=sess)

def predict_breast_cancer(image_path):
    with open(image_path, 'rb') as f:
        payload = f.read()
        payload = bytearray(payload)
    response = predictor.predict(payload)
    result = json.loads(response)
    print('Probabilities for all classes: ', result)
    predicted_class = np.argmax(result)
    if predicted_class == 0:
        print('Breast cancer not detected')
    else:
        print('Breast cancer detected')

predict_breast_cancer('Patient_8975_x2851_y1201.png')
predict_breast_cancer('Patient_10253_x501_y401.png')

print("End")

