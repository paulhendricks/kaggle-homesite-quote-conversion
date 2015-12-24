'''
Creates a feature (TO BE DETERMINED).

Authors:
Paul Hendricks

Date:
2015-12-15

inputs:
train.h5
test.h5
sample_submission.csv

outputs:
01-feature.h5
'''

# Load libraries
import pandas as pd

# Load data
prepped_path = './data/prepped/'
train = pd.read_hdf(prepped_path + 'train.h5', 'table')
test = pd.read_hdf(prepped_path + 'test.h5', 'table')
submission = pd.read_csv('./data/submission/sample_submission.csv')

# Write data out
pd.to_hdf('./data/features/01-feature.h5')
