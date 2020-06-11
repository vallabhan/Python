#!/usr/bin/env python
# coding: utf-8

# In[5]:


get_ipython().run_line_magic('matplotlib', 'inline')
from sklearn import datasets
import matplotlib.pyplot as plt


 


# In[6]:


digits = datasets.load_digits()


# In[11]:



print(digits.keys())
print(digits.DESCR)

 


# In[12]:



print(digits.images.shape)
print(digits.data.shape)


# In[13]:


plt.imshow(digits.images[1010], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()  


# In[14]:


from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split


# In[15]:


from sklearn.neighbors import KNeighborsClassifier 
from sklearn.model_selection import train_test_split


X = digits.data
y = digits.target


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42, stratify=y)


knn = KNeighborsClassifier(n_neighbors=7)


knn.fit(X_train, y_train)


print(knn.score(X_test, y_test))


# In[ ]:




