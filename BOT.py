#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit


# In[2]:


print (streamlit.__version__)


# In[3]:


header=streamlit.beta_container()
data=streamlit.beta_container()
Features=streamlit.beta_container()
scripts=streamlit.beta_container()


# In[4]:


with header:
    streamlit.title("SCRAPING TOOL")


# In[ ]:




