#!/usr/bin/env python
# coding: utf-8

# In[179]:


import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import random as rand
import collections 


# In[180]:


archivo = '/home/nbzenta/Descargas/lesmis.sif'
#archivo = '/home/nbzenta/Descargas/terrorista.sif'
#archivo = '/home/nbzenta/Descargas/familia_florentino.sif'


# In[181]:


def leer_sif(arch):
    G = nx.Graph()
    datos = open(arch, 'r')
    for line in datos:
        data = line.split()
        G.add_edge(data[0],data[2])
    return G    

       


# In[182]:


G = leer_sif(archivo)
#G = nx.karate_club_graph()
A = nx.to_numpy_matrix(G)


# In[183]:


def transition(i,j,G,A):
    LDN=list(G.nodes())
    return A[LDN.index(i),LDN.index(j)]/G.degree(i)


# In[184]:


def step(i,G,A):
    N=[vecino for vecino in nx.neighbors(G,i)]
    coeficiente_part=[]
    for v in N:
        coeficiente_part.append(transition(i,v,G,A))
    part=[]
    aux=0
    for coef in coeficiente_part:
        part.append(aux+coef)
        aux=aux+coef
    r=np.random.random()
    for p in range(len(part)):
        if p==0:
            if r<part[p]:
                indexf=0
                break
        if p>0:
            if p==len(part)-1:
                indexf=p
                break
            elif (part[p-1]<r  and r<part[p])==True: 
                indexf=p
                break
    return N[indexf]


# In[185]:


list_nodes = list(G.nodes())


# In[186]:


ic=rand.choice(list_nodes) #initial condition
Orbit=[ic]
for i in range(10000):
    ic=step(ic,G,A)
    Orbit.append(ic)


# In[187]:


import pylab as plt
node_color=[float(Orbit.count(i)) for i in G]
cmap = plt.cm.coolwarm
#cmap = plt.cm.plasma
#cmap = plt.cm.seismic
#cmap = plt.cm.Spectral_r
#cmap = plt.cm.jet

plt.figure(figsize=(16,8), dpi=300)
#plt.figure()
#pos = nx.spring_layout(G)
pos = nx.kamada_kawai_layout(G)
#pos = nx.shell_layout(G)
#pos = nx.spectral_layout(G)

nx.draw(G, pos, node_color=node_color, node_size=500, edge_color='gray',
        width=2, with_labels=True, cmap=cmap,alpha=0.9)
plt.show()


# In[188]:


hist_order = dict(zip(list(G.nodes()),node_color))


# In[189]:


sorted_hist = {k: v for k, v in sorted(hist_order.items(), key=lambda item: item[1], reverse=True)}
i_aux = 0
new_SH = {}
for k,v in sorted_hist.items():
    if i_aux < 10:
     new_SH[k] = v
     i_aux += 1
    else:
        break


# In[190]:


import pandas as pd
aux1=[]
aux2=[]
for k in new_SH.keys():
    aux1.append(k)
for v in new_SH.values():
    aux2.append(v)    
data_Dic = {'Nodes': aux1,'Connections': aux2}


# In[ ]:





# In[ ]:





# In[191]:


dframe = pd.DataFrame(data_Dic)
dframe.head(70)


# In[192]:


H = []
for w in sorted(new_SH, key=new_SH.get, reverse=True):
  H.append(new_SH[w])
H = np.array(H)
H = H/max(H)


# In[193]:


pos = np.arange(len(new_SH))
plt.bar(range(len(H)),H, align='center',color= 'r', width=0.9)
plt.xticks(pos, new_SH.keys(),rotation = 45)
plt.ylabel('Centrality')
plt.xlabel('Nodes')
plt.show()


# In[ ]:




