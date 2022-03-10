#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np 


# In[20]:


import math 
from numpy import random 
import matplotlib
from matplotlib import pyplot as plt 


# In[64]:


#gives out the value of the new theta list which would be itereated again and again 
#TO CHANGE THE NUMBER OF NEIGHBOPURS  ONE OSCILLATOR IS INTERACTING WITH WE WILL NEED TO CHANGE THE RANGE OVER WHICH j varies 
twopi= 2*np.pi
def newtheta(theta,omega,k,dt):
    ntheta= np.sort(theta)
    dtheta = np.zeros(len(theta))
    K= len(theta)
    for j in (-1,1):
        stheta=np.roll(theta,j)
        dtheta+=(k/2)*np.sin(stheta-theta)
    dtheta+= omega
    ntheta+= dtheta*dt
    return ntheta%twopi


# In[59]:


twopi= 2*np.pi
#gives out the values of the changing omega every iteration 
def newomega(theta,omega,k,dt):
    ntheta= np.sort(theta)
    dtheta = np.zeros(len(theta))
    K= len(theta)
    for j in range(K):
        stheta=np.roll(theta,j)
        dtheta+=(k/K)*np.sin(stheta-theta)
    dtheta+= omega
    
    return dtheta


# In[70]:



#does n iterations of the new theta function 

def donstepstoc(theta, omega,k,dt,nsteps):
    ntheta=np.sort(theta)
    nomega=np.copy(omega)
    for i in range (nsteps):
        ntheta= newtheta(ntheta,omega,k,dt)
        
    return ntheta
#calculates the order of the of a given phase set 
def calcord(theta):
    l=len(theta)
    ttheta= np.sort(theta)
    j=0
    for i in theta :
        j+=i
    j=j/l
    p=0
    for i in theta :
        p+=abs(j-i)
    p=p/l
    return p
#here we plot out the order parameter after n iterations 
#initial frequencies of all of the oscillators are the same ie 1 
#we use the calcord fucntion to calculate the order parameter for every k in range chosen ad then plot it 

N=20
theta= twopi*np.random.random(N)
omega=np.ones(N)
nsteps=1000
dt=0.1
j=[]
for k in np.linspace(0,100,50):
   
    j.append((calcord(donstepstoc(theta, omega,k,dt,nsteps))))
  
plt.plot(j)
        
        


# In[34]:





# In[71]:


#here we try to give the number of iterations the value of k and plot out the evolution of phases of the oscillators after a given  
#number of iterations again and again .
l=20
theta=2*np.pi*np.random.random(l)
k=1; dt=0.1
nsteps=50
omega = np.ones(l)
ntheta=donstepstoc(theta,omega,k,dt,nsteps)
                               


# In[57]:


#doing as said above , we plot the phsaes after given number of iterations three times 
ntheta=donstepstoc(theta,omega,k,dt,nsteps)
plt.plot(ntheta,'ro')
plt.ylim((0,twopi))
ntheta=donstepstoc(ntheta,omega,k,dt,nsteps)
plt.plot(ntheta,'go')
ntheta=donstepstoc(ntheta,omega,k,dt,nsteps)
plt.plot(ntheta,'bo')


# In[26]:





# In[13]:


print(omega)


# In[ ]:





# In[ ]:




