import pandas as pd
import matplotlib.pyplot as plt

#Question 1 implmentation
def chapter1(file_path):
    cancer_data = pd.read_csv(file_path, names=['class', 'age', 'menopause', 'tumor-size', 'inv-nodes', 'node-caps',
    'deg-malig', 'breast', 'breast-quad', 'irradiat'])
    print(cancer_data['class'])

#Question 2 implmentation
def chapter2(file_path):
    cancer_data = pd.read_csv(file_path, names=['class', 'age', 'menopause', 'tumor-size', 'inv-nodes', 'node-caps',
                                                'deg-malig', 'breast', 'breast-quad', 'irradiat'])
    print("The most common classficiation is: ",cancer_data['class'].value_counts().idxmax())

#Question 3 implementation
def chapter3(file_path):
    cancer_data = pd.read_csv(file_path, names=['class', 'age', 'menopause', 'tumor-size', 'inv-nodes', 'node-caps',
                                                'deg-malig', 'breast', 'breast-quad', 'irradiat'])
    recurr_patients = cancer_data[cancer_data['class'] == 'recurrence-events']
    print("The most common age is:", recurr_patients['age'].value_counts().idxmax())
    print("The most common menopause is:", recurr_patients['menopause'].value_counts().idxmax())

#Question 4 implmentation
def chapter4(file_path):
    cancer_data = pd.read_csv(file_path, names=['class', 'age', 'menopause', 'tumor-size', 'inv-nodes', 'node-caps',
                                                'deg-malig', 'breast', 'breast-quad', 'irradiat'])
    recurr_patients = cancer_data[cancer_data['class'] == 'recurrence-events'].groupby('age').size()
    recurr_patients.plot(kind="bar")
    plt.show()


#Run the functions
chapter1('breast-cancer.data')
chapter2('breast-cancer.data')
chapter3('breast-cancer.data')
chapter4('breast-cancer.data')