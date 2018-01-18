
i=0
j=0
Gmax = -10000
SumGmax = 0
Va = 0
Vb = 0 
X = []
Y = []
#A = [[0,1,2,3,2,4],[1,0,1,4,2,1],[2,1,0,3,2,1],[3,4,3,0,4,3],[2,2,2,4,0,2], [4,1,1,3,2,0]] 	# Adjacency matrix A[i][j]


A = [[0,1,0,0,0,0],[1,0,0,1,0,0],[0,0,0,1,0,1],[0,1,1,0,1,0],[0,0,0,1,0,1], [0,0,1,0,1,0]] 	# Adjacency matrix A[i][j]
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

	


