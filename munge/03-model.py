'''
Munges test data.

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
train = pd.read_hdf(prepped_path + 'train.h5', 'table', append=True)
test = pd.read_hdf(prepped_path + 'test.h5', 'table', append=True)
submission = pd.read_csv('./data/submission/sample_submission.csv')

# TODO Set column names

# TODO Set column types

# TODO Filter out certain columns

# TODO Filter out certain observations

# TODO Ensure uniqueness at some level

# TODO Define other variables

# TODO Write out data to data/prepped/
