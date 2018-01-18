# Implementation of KL algorithm
# Author Shrinidhi Rao
# Date : 18/08/2018

import numpy as np
import sys

A= sys.argv[1]


# Get Adjacency Matrix
def Get_matrix(x):
 
   y=len(x)
   list=x
   Matrix=np.zeros((y,y))
   for i in list:
	for j in list:
	   for o in range(1,10):
		if j[o]==i[0]:
		     j[o]=i[10]
 
   for i in list:
	for o in range(1,10):
		if i[o]!='0' and i[o]!=0:
			Matrix[int(i[10])-1][int(i[o])-1]=1
			Matrix[int(i[o])-1][int(i[10])-1]=1
 
   return Matrix


# Removing extra characters
def node(line):
   xy=[]
   z=0
   a="\0"
   if line[0]!="*":
	for i in line:
		if i=="*":
			p=[a.strip("\x00") for a in xy]
			return p
		elif i!=" " and i!="\n":
			a+=i
			z=1
     		else:
			if z==1:
				xy.append(a)
				a="\0"
				z=0
   p=[a.strip("\x00") for a in xy]
   return p


# Obtaining Adjacency list from Netlist (.isc file)

def Get_Adjacency_List(filename):
   f=open(filename,"r");
   line=f.readline()
   c=0;
   a=[]
   y=['','','aaa']
   record=[]
   count=1
   while line:
	y_new=node(line)
	if y_new:
		if y[2]!="from" and y[2]!="inpt" and y[2]!="aaa":
    
			x=[y[0],y_new[0],y_new[1] if int(y[4])-1>0 else 0,y_new[2] if int(y[4])-2>0 else 0,y_new[3] if int(y[4])-3>0 else 0,y_new[4] if int(y[4])-4>0 else 0,y_new[5] if int(y[4])-5>0 else 0,y_new[6] if int(y[4])-6>0 else 0,y_new[7] if int(y[4])-7>0 else 0,y_new[8] if int(y[4])-8>0 else 0,count];
			count+=1
			a.append(x)
			y=['','','aaa']
		else:
			y=y_new
			record.append(y_new)
	line=f.readline()
   f.close()
   z=a;
 
   tag=1
   while tag==1:
	tag=0
	for s in z:
		for row in record:
			for u in range(1,10):
				if s[u]==row[0]:
					if row[2]=="from":
						tag=1
						for i in record:
							if row[3]==i[1]:
								s[u]=i[0]
   z1=z

 
   for s in z1:
	t=9*[0]
	for d in a:
		for u in range(1,10):
			if s[u]==d[0]:
				t[u-1]=1
	for u in range(0,9):
		if t[u]==0:
			s[u+1]=0
 
   return z1

A = Get_Adjacency_List(A)
A = Get_matrix(A)



i=0
j=0
Gmax = 0
SumGmax = 0
Va = 0
Vb = 0 
X = []
Y = []
n = len(A)
m=n

print "\n\nAdjacency matrix : ", A,'\n\n'
while i < m/2:
   X.append(i)
   i=i+1
while i < m:
   Y.append(i)
   i=i+1

I = [0]*m
E = [0]*m
D = [0]*m
Gtemp=0
print "\nInitial X Partition : ", X, "\nInitial Y Partition: ", Y	


while n != 0 :
	G=[]
	
	i=0
	while i <m/2:
	   j=0
	   while j <m/2:
	   	I[X[i]] += A[X[i]][X[j]]
		j+=1					#Internal Cost
	   i+=1

	i=0
	while i <m/2:
	   j=0
	   while j<m/2:
	   	I[Y[i]] += A[Y[i]][Y[j]]		#Internal Cost
	   	j+=1
	   i+=1

	print '\nInternal Cost : ' , I

	i=0
	while i <m/2:
	   j=0
	   while j <m/2:
	   	E[X[i]] += A[X[i]][Y[j]]			#External Cost
		j+=1
	   i+=1
	i=0
	while i<m/2:
	   j=0
	   while j <m/2 :
	   	E[Y[i]] += A[Y[i]][X[j]]			#External Cost
		j+=1
	   i+=1

	print 'External Cost : ' , E
	i = 0
	while i < m:
	   D[i]= E[i]-I[i]					#Cost Difference
	   i+=1
	print 'D Values: ', D
	i=0
	while i < n/2 :
	   j=0
	   while j < n/2:
		Gtemp= D[X[i]]+D[Y[j]]-2*A[X[i]][Y[j]]		#Gain Values for Interchange
		G.append(Gtemp)			
		if Gtemp > Gmax:
		     Gmax = Gtemp
		     Va = X[i]
		     Vb = Y[j]
		j += 1
	   i += 1
	SumGmax += Gmax	
	print 'Gain Values' ,G
	print 'Maximum Gain : ', Gmax	
	Gmax= -10000
	print "Sum of Gains : ", SumGmax
	if SumGmax == 0:
		print "No swapping as condition fails"	   
		break
	else:
		print 'Vertex in X to be swapped : ', Va , '\nVertex in Y to be swapped : ',Vb	
	
	
	i=0
	while i < n/2: 
	   if (X[i] == Va):
		X.pop(i)
		X.append(Vb)
	   i+=1
	i=0
	while i<n/2:
	   if (Y[i]==Vb):
		Y.pop(i)
		Y.append(Va)
	   i+=1
	n = n-2
	print "\nUpdated X Partition: ", X, "\nUpdated Y Partition: ", Y,'\n\n'
	I = [0]*m
	E = [0]*m
	D = [0]*m

	
print "\n\nFinal Prtition :","\nX Partition : ",X,"\nY Partition : ", Y

	

	

