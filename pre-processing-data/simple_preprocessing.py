import pandas as pd
import os
import warnings

from sklearn.model_selection import train_test_split

# Read data locally 
df = pd.read_csv('/opt/ml/processing/input/heart.csv')

# Preprocess the data set
#downsampled = apply_mad_data_science_skills(df)

# Split data set into training, validation, and test
#train, test = train_test_split(downsampled, test_size=0.2)
train, test = train_test_split(df, test_size=0.2)
#train, validation = train_test_split(train, test_size=0.2)

# Create local output directories
try:
    os.makedirs('/opt/ml/processing/train')
    #os.makedirs('/opt/ml/processing/output/validation')
    os.makedirs('/opt/ml/processing/test')
except:
    pass

# Save data locally
train.to_csv("/opt/ml/processing/train/train_features.csv", header=False, index=False)
#validation.to_csv("/opt/ml/processing/output/validation/test_features.csv")
test.to_csv("/opt/ml/processing/test/test_features.csv", header=False, index=False)

print('Finished running processing job')