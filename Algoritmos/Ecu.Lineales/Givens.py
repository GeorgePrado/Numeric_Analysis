from math import fabs
from math import sqrt
from sys import exit

def vector_cero(n):
	V=[]
	for i in range(n):
		V.append(0.0)
	
	return V

##crea una matriz mxn de ceros
def matriz_cero(m,n) :
	Z=[]
	for i in range(m):
		Z.append([0.0]*n)
	
	return Z

def prod_int(u,v):
	c=0.0
	if len(u)== len(v):
		for i in range(len(u)):
			c=c+u[i]*v[i]
		return c		
		
	else :
		print 'Imposible operacion a realizar'

def norma(u):
	c=pow(prod_int(u,u),0.5)
	return c

def mul_matriz(A,B):
	m=len(A)
	n=len(B)
	p=len(B[0])
	q=len(A[0])
	if q == n :
 		C=matriz_cero(m,p) 	
		for i in range(m):
			for j in range(p):
				c=0.0
				for k in range(n):
					c=c+A[i][k]*B[k][j]
				C[i][j]=c
		##fin de los for
		if p == 1 :
			D=vector_cero(m)
			for i in range(m):
				D[i]=C[i][0]		
			return D
		
		else :
			D=C		
			return D
	
	else :
		print 'Imposible operacion a realizar'

def mul_vector_matriz(A,v):
	n=len(A)
	m=len(v)  
	x=vector_cero(m)
	for i in range(n):
		c=0.0		
		for j in range(m):
			c=c+A[i][j]*v[j]
		x[i]=c
	
	return x


def matriz_aumentada(A,b):
	n=len(A)
	C=A
	for i in range(n):
		C[i].append(b[i])
	
	return C  

##producto de un escalar con un vector
def prod_escalar_vector(v,a):
	n=len(v)
	t=vector_cero(n)
	for i in range(n):
		t[i]=v[i]*a	 
	
	return t 

##suma de dos vectores
def sum_vector(u,v):
	n=len(u)
	m=len(v)
	if n == m :	
		c=vector_cero(n)
		for i in range(n):
			c[i]=u[i]+v[i]
	
		return c
	
	else :
		print 'Operacion erronea \n'

##obtener col i de una matriz A
def get_col(A,i):
	m=len(A)
	n=len(A[0])	
	v=vector_cero(m) 
	for j in range(m):
		v[j]=A[j][i]
	
	return v

##obtener fila i de una matriz A
def get_fila(A,i):
	m=len(A)
	n=len(A[0])	
	v=vector_cero(n) 
	for j in range(n):
		v[j]=A[i][j]
	
	return v
	
##establece la columna j de A por el vector v
def set_col_matriz(A,v,j):
	n=len(A)
	for i in range(n):
		A[i][j]=v[i]

##establece la fila i de A por el vector v			
def set_fila_matriz(A,v,i):
	m=len(A[0])
	for j in range(m):
		A[i][j]=v[j]

##transpuesta para cualquier matriz
def transpuesta(A):
	m=len(A)
	n=len(A[0])
	B=matriz_cero(n,m)
	for i in range(n):
		for j in range(m):	
			if i==j :
				B[i][j]=A[i][j]
			else :
				B[i][j]=A[j][i]
	##end
	return B	

def enter_matriz(n):
	print 'Ingrese matriz cuadrada'
	A=[]
	for i in range(n) :
		A.append([0]*n)
#ingresamos cada elemento de la matriz
	for i in range(n):
		for j in range(n):
			A[i][j]=float(raw_input('a[%d,%d]:'%(i+1,j+1)))	
	return A

def print_matriz(A):
	n=len(A)
	m=len(A[0])
	for i in range(n):
		l=A[i]		
		s=' '.join(["%.3f" % i for i in l])
		print s

##solucion de sistema de ecuaciones regresivo
def sol_regresivo(A,b):
	n=len(A)
	x=vector_cero(n)
	x[n-1]=round(b[n-1]/A[n-1][n-1],4)
	j=n-2
	while j>=0 :
		x[j]=b[j]
		for i in range(j+1,n):
			x[j]=x[j]-A[j][i]*x[i]
		x[j]=round(x[j]/A[j][j],4)
		j=j-1
	return x


def printMatrix(M):
	for i in range(len(M)):
		print '|',
		for j in range(len(M[i])):
			if(j == len(M)):
				print '|',
				print '{0:8.4f}'.format(M[i][j]),
			else:
				print '{0:8.4f}'.format(M[i][j]),	
		print '|'
	print 

def matrixMulti(A, B):
	"""Multiplica dos matrices, C = A*B """

	rowsA, colsA = len(A), len(A[0])
	rowsB, colsB = len(B), len(B[0])

	if colsA != rowsB:
		exit('Dimensiones incorrectas')

	C = [[0 for row in range(colsB)] for col in range(rowsA)]

	for i in range(rowsA):
		for j in range(colsB):
			for k in range(colsA):
				C[i][j] += A[i][k]*B[k][j]
	return C

def trans(M):
	"""Calcula la matriz transpuesta de M"""

	n = len(M)
	return [[ M[i][j] for i in range(n)] for j in range(n)]

def givens(A):
	"""	Gn* ... G2*G1*A = R
		Q_t = Gn* ... G2*G1
		A = Q*R, de la propiedad Q_t * Q = I
	"""
	n = len(A)

	An = A	
	Gn = [[float(i == j) for j in range(n)] for i in range(n)]
	Q_t = [[float(i == j) for j in range(n)] for i in range(n)]

	a = An[0][n-2]
	b = An[0][n-1]
	index = 1
	for i in range(n):
		for j in range(n-1, i, -1):
			a = An[j-1][i]
			b = An[j][i]
			if a*a + b*b == 0:
				continue

			cosX = round(a / (sqrt(a*a + b*b)),5)
			sinX = round(-b / (sqrt(a*a + b*b)),5)

			Gn[j][j] = cosX
			Gn[j][j-1] = sinX
			Gn[j-1][j] = -sinX
			Gn[j-1][j-1] = cosX

			#print 'G' +str(index) + ':'
			#printMatrix(Gn)

			An = matrixMulti(Gn, An)

			#print 'A' +str(index) + ':'
			#printMatrix(An)

			Q_t = matrixMulti(Gn, Q_t)
			#Volviendo la matriz Gn a la identidad
			Gn = [[float(k == l) for l in range(n)] for k in range(n)]
			index += 1
	return trans(Q_t), An

if __name__ == '__main__':
	##A = [-9.0,1.0,7.0],[3.0,2.0,-1.0],[6.0,8.0,1.0]
	#A = [.0001,.000001,.000000001],[.000000000001,.0000000000000001,.000000000000000001],[.000000000000000000001,.000000000000000000000001,.0000000000000000000000000001]
	#A = [4,-1,0,-1,0,0],[-1,4,-1,0,-1,0],[0,-1,4,0,0,-1],[-1,0,0,4,-1,0],[0,-1,0,-1,4,-1],[0,0,-1,0,-1,4]	
	A=[[1.0,1.0,1.0,0.0,0.0,0.0],[0.0,-1.0,0.0,1.0,-1.0,0.0],[0.0,0.0,-1.0,0.0,0.0,1.0],[0.0,0.0,0.0,0.0,1.0,-1.0],		[0.0,10.0,-10.0,0.0,-15.0,-5.0],[5.0,-10.0,0.0,-20.0,0.0,0.0]] 
	b=[0.0,0.0,0.0,0.0,0.0,200.0]		
	Q, R = givens(A)
	print "A"
	printMatrix(A)
	print "Q"
	printMatrix(Q)
	print "R"
	printMatrix(R)
	##print 'A = Q*R :'
	##printMatrix(multMatriz(Q, R))
	c=mul_vector_matriz(transpuesta(Q),b)
	##solucion del sistema
	x=sol_regresivo(R,c)
	print 'la solucion del sistema es :\n'
	print x


