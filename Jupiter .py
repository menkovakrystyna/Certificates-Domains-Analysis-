#!/usr/bin/env python
# coding: utf-8

# In[333]:


import numpy as np
import pandas as pd
from sklearn import *
from sklearn.linear_model import LogisticRegression
from sklearn import metrics


# In[334]:


data = pd.read_csv('finance_train80.csv')
data.head(10)


# In[335]:


data.rename(columns = {'autodiscover.chilipines.com':'domains', '0':'weird_symbols_flag',
                              '0.1':'dots_5numbers_flag', '0.2': 'ip_flag', '0.3':'weird_word_flag',
                       '0.4': 'length', '0.5':'num_flag', '0.6': 'num_nosplit_flag',
                      '0.7':'defis_2number_flag', '0.8':'Result'}, inplace = True)


# In[336]:


data.head(10)


# In[337]:


targets = data['Result']


# In[338]:


data.drop('Result', axis=1, inplace=True)
data.drop('domains', axis=1, inplace=True)


# In[339]:


data.head()


# # Test and Train data Logistic Regression

# In[340]:


training_inputs = data[:2000]
training_outputs = targets[:2000] 
testing_inputs = data[2000:]
testing_outputs = targets[2000:]


# In[341]:


classifier = LogisticRegression()


# In[342]:


classifier.fit(training_inputs, training_outputs)


# In[343]:


predictions = classifier.predict(testing_inputs)


# In[344]:


accuracy = 100.0 * accuracy_score(testing_outputs, predictions)
print ("The accuracy of your Logistic Regression on testing data is: " + str(accuracy))


# # Finding Intercept and Coeficient

# In[345]:


classifier.intercept_


# In[346]:


feature_name = data.columns.values


# In[347]:


summary_table = pd.DataFrame(columns =['Feature name'], data = feature_name)
summary_table['Coeficient']=np.transpose(reg.coef_)


# In[348]:


summary_table
# the most importsnt feature that detect the fishing accounts are 
#dots_5numbers_flag - in domain there are more than 5 dots
#length - the lengh of the domain is more or equalls 40 symbolls
#num_nosplit_flag - there are less than 20 numbers, goes one by one in the domain
# defis_2number_flag -contains more or equalls 3 '-' in domain


# In[349]:


summary_table.index=summary_table.index+1
summary_table.loc[0]=['Intercept', reg.intercept_[0]]
summary_table=summary_table.sort_index()
summary_table


# # Predicting Rest of the Data

# In[350]:


data_to_predict1 = pd.read_csv('finance_test20.csv')


# In[351]:


data_to_predict = pd.read_csv('finance_test20.csv')


# In[352]:


data_to_predict.head()


# In[353]:


data_to_predict.rename(columns = {'www.beachsidemn.com':'domains', '0':'weird_symbols_flag',
                              '0.1':'dots_5numbers_flag', '0.2': 'ip_flag', '0.3':'weird_word_flag',
                       '0.4': 'length', '0.5':'num_flag', '0.6': 'num_nosplit_flag',
                      '0.7':'defis_2number_flag'}, inplace = True)


# In[354]:


data_to_predict.drop('domains', axis=1, inplace=True)


# In[355]:


prediction = classifier.predict(data_to_predict)


# In[1]:


print(metrics.classification_report(prediction, ytest))


# In[356]:


fishing = pd.DataFrame(columns =['Fishing Account'], data = prediction)


# In[357]:


data_to_predict1.columns


# In[358]:


data_to_predict1.rename(columns = {'www.beachsidemn.com':'domains', '0':'weird_symbols_flag',
                              '0.1':'dots_5numbers_flag', '0.2': 'ip_flag', '0.3':'weird_word_flag',
                       '0.4': 'length', '0.5':'num_flag', '0.6': 'num_nosplit_flag',
                      '0.7':'defis_2number_flag'}, inplace = True)


# In[359]:


data_to_predict1.columns


# In[360]:


data_to_predict1.drop('weird_symbols_flag', axis=1, inplace=True)
data_to_predict1.drop('dots_5numbers_flag', axis=1, inplace=True)
data_to_predict1.drop('ip_flag', axis=1, inplace=True)
data_to_predict1.drop('weird_word_flag', axis=1, inplace=True)
data_to_predict1.drop('length', axis=1, inplace=True)
data_to_predict1.drop('num_flag', axis=1, inplace=True)
data_to_predict1.drop('num_nosplit_flag', axis=1, inplace=True)
data_to_predict1.drop('defis_2number_flag', axis=1, inplace=True)


# In[361]:


data_to_predict1.columns


# In[362]:


fish_domains=pd.concat([data_to_predict1,fishing], axis = 1)


# In[363]:


fish_domains.head()


# In[364]:


fish_domains.to_csv('Prediction of Fishing Domains.csv', index= False)


# In[365]:


fish_domains.head(1000)


# In[ ]:




