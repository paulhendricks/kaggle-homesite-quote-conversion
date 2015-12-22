'''
Builds a model (TO BE DETERMINED).

Authors:
Paul Hendricks

Date:
2015-12-15

inputs:
test.csv.zip

outputs:
test.h5
'''

# Load libraries
import pandas as pd

# Load data
prepped_path = './data/prepped/'
train = pd.read_hdf(prepped_path + 'train.h5', 'table')
test = pd.read_hdf(prepped_path + 'test.h5', 'table')
submission = pd.read_csv('./data/submission/sample_submission.csv')

submission = pd.read_csv('./data/ensemble/01-model.csv')
