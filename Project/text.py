import os
import pandas as pd
with open('Distance_Matrix_6.txt') as f:
    data=f.read()
data=data.strip().split('\n')
z=[]
for i in data:
    j=' '.join(i.split())
    k=j.replace(' ','\t')
    z.append(k)
f.close()

with open('new.txt','wt') as k:
    h='\n'.join(z)
    k.write(h)
    k.close()

