#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
data1 = np.loadtxt('vela_Pulsar.mbr')


# Loading the Vela Pulsar Data

# In[3]:


north_data = data1[:,[0]]
south_data = data1[:,[1]]
north_data = np.array(north_data,dtype = complex)
south_data = np.array(south_data,dtype = complex)


# Making Matrix of dimention $512 \times 60000$

# In[3]:


north_data = np.reshape(north_data,(512,60000),order = 'F')
south_data = np.reshape(south_data,(512,60000),order = 'F')


# Here we are calculating $FFT(data)$ of every column and taking their square of absolute value i.e. $|FFT|^2$

# In[4]:


# north_fft = np.zeros(512,60000)
# south_fft = np.zeros(512,60000)
for i in range(0,len(north_data[0])):
    north_data[:,i] = np.power(np.abs(np.fft.fft(north_data[:,i])),2)
    south_data[:,i] = np.power(np.abs(np.fft.fft(south_data[:,i])),2)

# north_data = north_data.astype(float)
# south_data = south_data.astype(float)
# for i in range(0,999):
  


# Reducing noise by taking average of every 60 elements....

# In[5]:


north_fft = np.zeros((512,1000))
south_fft = np.zeros((512,1000))
for i in range(0,1000):
    north_fft[:,i] = np.sum(np.real(north_data[:,60*i:60*(i+1)-1]),axis = 1)
    south_fft[:,i] = np.sum(np.real(south_data[:,60*i:60*(i+1)-1]),axis = 1)


# Plotting The Matrix

# In[5]:


from matplotlib import pyplot as plt
ax1 = plt.matshow(north_fft[256:511,:])
ax2 = plt.matshow(south_fft[256:511,:])
plt.xlabel('FFT')
plt.imsave('north.png',arr = north_fft[256:511,:])
plt.imsave('south.png',arr = south_fft[256:511,:])


# In[16]:


# from scipy.stats import norm
# data_normal = norm.rvs(size = 10000,loc = 0,scale = 1)
hist_north = data1[:,[0]]
hist_north = hist_north/len(hist_north)
plt.hist(hist_north,bins = 350)
plt.savefig('hist_n.png')
# print(data_normal)
plt.show()


# In[18]:


hist_south = data1[:,[1]]
plt.hist(hist_south,bins = 350)
plt.xlabel('Voltages')
plt.savefig('hist_s.png')
plt.show()


# In[12]:


from matplotlib import pyplot as plt
northhist = np.power(np.absolute(np.fft.fft(north_data)),2)
plt.hist(northhist,bins = 550)
plt.savefig('north_fft.png')
plt.show()


# In[11]:


southhist = np.power(np.absolute(np.fft.fft(south_data)),2)
plt.hist(southhist,bins = 550)
plt.savefig('south_fft.png')
plt.show()


# In[ ]:




