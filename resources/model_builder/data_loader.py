"""Data Loader File
This file contains the data loading process. If from main being put args 

"""
import pandas



dataframe = pandas.read_csv('emotions.csv')
print(dataframe.head())
print(f"Count {dataframe.count()}")

# Testing Data Loader for Debugging.
