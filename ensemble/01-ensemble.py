'''
Ensembles models and feautures.

Authors:
Paul Hendricks

Date:
2015-12-15

inputs:
data/features/*
data/models/*

outputs:
submission.csv
'''

# Load libraries
import pandas as pd

# Load data
features_path = './data/features/'
models_path = './data/models/'

# Write data out
pd.to_csv('./data/submission/01-submission.csv')
