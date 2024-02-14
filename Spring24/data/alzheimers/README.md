# Detecting Alzheimer's Disease via Positron Emission Tomography

====
Positron Emission Tomography (PET) detects the metabolic processes in the body
and can be used to detec diseases in the brain, such as Alzheimer's Disease (AD). 
In the study of AD, there are two groups of subjects of particular interest:
one group is patients with mild cognitive impairment (MCI), and the other group
is AD patients. In this experiment we will build classification models to detect
AD from the features derived from PET imaging. 

===

## Data 

The dataset is in the Matlab data file `ad_data.mat`, where each patient is 
describe by 116 numerical features extracted from PET imaging. The dataset 
has been divided into a training set and a testing set. Training data (features) 
and labels are given in `X_train` and `y_train`, and testing data (features) 
and labels are given in `X_test` and `y_test`. You will find in the data
file 172 samples for training and 74 for testing.  The labels are given by 
1 (AD patient) and -1 (MCI patient). 


