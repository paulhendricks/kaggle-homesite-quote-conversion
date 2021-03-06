'''
Munges train data.

Authors:
Paul Hendricks

Date:
2015-12-15

inputs:
train.csv.zip

outputs:
01-train.h5
'''

# Load libraries
import pandas as pd
import zipfile

# Load data
original_path = './data/original/'
file_name = 'train'
z = zipfile.ZipFile(original_path + file_name + '.csv.zip')
train = pd.read_csv(z.open(file_name + '.csv'))

# TODO Set column names

# TODO Set column types

# TODO Filter out certain columns

# TODO Filter out certain observations

# TODO Ensure uniqueness at some level

# TODO Define other variables

# TODO Write out data to data/prepped/
prepped_path = './data/prepped/'
train.to_hdf(prepped_path + '01' + file_name + '.h5', 'table', append=True)
