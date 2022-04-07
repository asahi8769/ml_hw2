import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, roc_auc_score, roc_curve, f1_score
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df_info = df.info()
df_desc = df.describe()

