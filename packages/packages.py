#contain python scripts
#each script should be named as the package it is for, and should contain a function that returns the version of the package
#In data science, we have numpy,pandas,matplotlib,seaborn,scikit-learn,statsmodels,scipy,plotly,bokeh,altair,ggplot,missingno,yellowbrick,mlxtend,xgboost,lightgbm,catboost,lime,shap,pycaret
#To use them you have to instal them first using pip install package_name then you can import them in your script and use their functions to perform various data science tasks.

import numpy as np

age =[12, 15, 14, 10, 18, 20, 25, 30, 35, 40]

np_age = np.array(age)
print(np_age)
print(type(np_age))