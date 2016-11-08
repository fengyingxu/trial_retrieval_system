# trial_retrieval_system
A computer program based on text analytic algorithm provided to search for the most similar studies to a particular input on ClinicalTrials.gov.

## About the model
The similarity between studies was calculated on TF-IDF scores of descriptive summary of each study. Four most similar studies would be retrieved using nearest neighbor search.

The model can be easily deployed to launch a Predictive Service in Amazon EC2.

Adjustments would be made in the near future.

## Requirements:
This software needs a Python environment and a Graphlab Create (Turi) library to function properly.

## Other files:
The database and model needed in the program is saved in binary format, and is stored on Google Drive, since file larger than 100 MB is not allowed to be pushed on GitHub.
Both of them are presented as zip files. Please unzip them before excution. They can be downloaded at:
Database: https://drive.google.com/file/d/0B0u0jsE9OBwcU3R2ZTgzRTc1R3M/view?usp=sharing
Model: https://drive.google.com/file/d/0B0u0jsE9OBwcRDNDYnNUYXBiZkE/view?usp=sharing
