'''
Creates a feature LogField9 that is the Log transformation of Field9.

Authors:
Paul Hendricks

Date:
2015-12-15

inputs:
test.h5
train.h5
sample_submission.csv

outputs:
01-test-feature-LogField9.h5
01-train-feature-LogField9.h5
'''

# Load libraries
import pandas as pd
import numpy as np

# Load data
prepped_path = './data/prepped/'

train = pd.read_hdf(prepped_path + 'train.h5', 'table')
test = pd.read_hdf(prepped_path + 'test.h5', 'table')

# Create the feature
transformation_name = 'Log'
feature_name = 'Field9'
transformed_feature_name = transformation_name + feature_name

train[transformed_feature_name] = np.log(train[feature_name])
test[transformed_feature_name] = np.log(test[feature_name])

# Subset the primary key and feature
primary_key_name = 'QuoteNumber'
column_names = [primary_key_name, transformed_feature_name]

train_feature = train[column_names]
test_feature = test[column_names]

# Write data out
features_path = './data/features/'

train_feature.to_hdf(features_path + '01-train-feature-' + transformed_feature_name + '.h5', 'table')
test_feature.to_hdf(features_path + '01-test-feature-' + transformed_feature_name + '.h5', 'table')
