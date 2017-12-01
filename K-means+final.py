
# coding: utf-8

# In[27]:


import math
import csv
import random
with open('C:\Users\Mahesh\Desktop\ESE\DM lab\md\md.csv','rb') as data:
    reader=csv.reader(data,delimiter='\t')
    data=tuple(reader)
length=len(data)
print "Enter no of cluter:-"
no=int(input());
points=[]
for i in range(length):
    points.append(list(map(float,data[i][0].split(','))))
print points
c=[]

for i in range(no):
    c.append(random.randint(0,len(data)-1))
cen=[]
for i in range(no):
    tmp=c[i]
    cen.append(points[tmp])
print "cen"
print cen
for k in range(50):
    dis={}
    for j in range(length):
        dis[j]=0;
        min=999999999;
        for i in range(no):
            tmp=math.sqrt((points[j][0]-cen[i][0])**2+(points[j][1]-cen[i][1])**2)
            if(tmp<min):
                dis[j]=i;
                min=tmp;
    p_in_c=[]
    for i in range(no):
        p_in_c.append([])
    for j in range(length):
        p_in_c[dis[j]].append(j)
    print(p_in_c)
    for i in range(no):
        for j in range(len(p_in_c[i])):
            p_in_c[i][j]=points[p_in_c[i][j]]
    print(p_in_c)
    for i in range(no):
        x=0;y=0;
        for j in range(len(p_in_c[i])):
            x+=p_in_c[i][j][0];
            y+=p_in_c[i][j][1];
        cen[i][0]=x/len(p_in_c[i]);
        cen[i][1]=y/len(p_in_c[i]);
    print "_____________________"
    print "centroid:--"
    print(cen)
    print "_____________________"
    

