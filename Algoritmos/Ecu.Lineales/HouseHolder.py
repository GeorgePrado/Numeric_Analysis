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
	x[n-1]=b[n-1]/A[n-1][n-1]
	j=n-2
	while j>=0 :
		x[j]=b[j]
		for i in range(j+1,n):
			x[j]=x[j]-A[j][i]*x[i]
		x[j]=x[j]/A[j][j]
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

def norm_2(x):
    return sqrt(sum([x_i**2 for x_i in x]))

def multMatriz(A, B):
	n = len(A)
	C = [[0.0] * n for i in range(n)]
	for i in range(n):
		for j in range(n):
			for k in range(n):
				C[i][j] += A[i][k]*B[k][j]
	return C

def transpuesta(M):
	n = len(M)
	Mt = [[0.0] * n for i in range(n)]
	for i in range(n):
		for j in range(n):
			Mt[j][i] = M[i][j]
	return Mt

def Q_i(Q_min, i, j, k):
    if i < k or j < k:
        return float(i == j)
    else:
        return Q_min[i-k][j-k]

def multMatrix(A,B,n):
  C = []
  for i in range(n):
    C.append([0]*n)

  for i in range(n):
    for j in range(n):
      for k in range(n):
        C[i][j] = C[i][j] + A[i][k]*B[k][j]
  return C

#####################################################
##ELIMINACION DE GAUSS
#####################################################
def eliminacionGauss(A,b,n):
  ##inicializando un arreglo x en 0
  x = []
  for i in range(n):
    x = [0] * n
  for k in range(n-1):
    for i in range(k+1,n):
      m = A[i][k]/A[k][k]
      for j in range(k,n):
        A[i][j] = A[i][j] - m*A[k][j]
      b[i] = b[i] - m*b[k]
  x[n-1] = b[n-1]/A[n-1][n-1]
  for i in range(n-2,-1,-1):
    x[i] = b[i]
    for j in range (i+1,n):
      x[i] = x[i] - A[i][j]*x[j]
    x[i] = x[i]/A[i][i]
  return x

def printVector(c):
  print '[',
  for i in range(len(c)):
    print '{0:8.4f}'.format(c[i]),
  print ']'

def eliminacionGaussPivoteoTotal(A,b,n):
  ##inicializando un arreglo x en 0
  x = []
  for i in range(n):
    x = [0] * n
  for k in range(n-1):
    if A[k][k] == 0:
      l,m = mayor(A,k)
      A = swap(A,k,l,m)
      b[k],b[i] = b[i],b[k]
    for i in range(k+1,n):
      m = A[i][k]/A[k][k]
      for j in range(k+1,n):
        A[i][j] = A[i][j] - m*A[k][j]
      b[i] = b[i] - m*b[k]
  x[n-1] = b[n-1]/A[n-1][n-1]
  for i in range(n-2,-1,-1):
    x[i] = b[i]
    for j in range (i+1,n):
      x[i] = x[i] - A[i][j]*x[j]
    x[i] = x[i]/A[i][i]
  return x

def swap(A,k,l,m):
  for j in range(len(A)):
    A[k][j],A[l][j] = A[l][j],A[k][j]
  for i in range(len(A)):
    A[i][k],A[i][m] = A[i][m],A[i][k]
  return A
def mayor(A,k):
  mayor = abs(A[k][k])
  i_max = j_max = k
  for i in range(k,len(A)):
    for j in range(k,len(A)):
      if mayor < abs(A[i][j]):
        mayor = abs(A[i][j])
        i_max = i
        j_max = j
  return i_max,j_max

def factorizacionHouseHolder(A,b,n):
  R = A
  Q = [[0.0] * n for i in range(n)]

  for k in range (n-1):
    I = [[float(i == j) for i in range(n)] for j in range(n)]

    # Se crea los vectores x, e y un escalar alpha
    x = [row[k] for row in R[k:]]
    e = [row[k] for row in I[k:]]
    #La funcion cmp(a, b) retorna -1 si a<b, 1 si a>b, 0 si a==b
    alpha = -cmp(x[0],0) * norm_2(x) 

    #Se crea los vectores u, v
    u = map(lambda p,q: p + alpha * q, x, e)
    norm_u = norm_2(u)
    v = map(lambda p: p/norm_u, u)

    #Se crea la matriz menor Q_t
    Q_min = [ [float(i==j) - 2.0 * v[i] * v[j] for i in range(n-k)] for j in range(n-k) ]

    #Se rellena la matriz menor Q (Q_min)
    Q_t = [[ Q_i(Q_min,i,j,k) for i in range(n)] for j in range(n)]

    if k == 0:
      Q = Q_t
      R = multMatrix(Q_t,A,n)
    else:
      Q = multMatrix(Q_t,Q,n)
      R = multMatrix(Q_t,R,n)
  Q = transpuesta(Q)
  print "Q:"
  printMatrix(Q)
  print "R:"
  printMatrix(R)
  y = eliminacionGauss(Q,b,n)
  print "Solucion y:"
  printVector(y)
  x = eliminacionGaussPivoteoTotal(R,y,n)
  return x
 
if __name__ == '__main__':
	#A = [4,-1,0,-1,0,0],[-1,4,-1,0,-1,0],[0,-1,4,0,0,-1],[-1,0,0,4,-1,0],[0,-1,0,-1,4,-1],[0,0,-1,0,-1,4]
	A=[[1.0,1.0,1.0,0.0,0.0,0.0],[0.0,-1.0,0.0,1.0,-1.0,0.0],[0.0,0.0,-1.0,0.0,0.0,1.0],[0.0,0.0,0.0,0.0,1.0,-1.0],		[0.0,10.0,-10.0,0.0,-15.0,-5.0],[5.0,-10.0,0.0,-20.0,0.0,0.0]] 
	b=[0.0,0.0,0.0,0.0,0.0,200.0]		
	Q, R = factorizacionHouseHolder(A,b,len(A))
	##printMatrix(A)
	print "Por el metodo de HousHolder:"
	print "Q:"
	printMatrix(Q)
	print "R:"
	printMatrix(R)
	##print "A = Q*R :"
	#printMatrix(multMatriz(Q, R))
	c=mul_vector_matriz(Q,b)
	print 'imprime Q*b \n'
	print c
	##solucion del sistema
	x=sol_regresivo(R,c)
	print 'la solucion del sistema es :\n'
	print x
