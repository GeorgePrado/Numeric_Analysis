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

##funcion principal
def GramSchmidt(A):
	m=len(A)
	n=len(A[0])
	U=matriz_cero(m,n)
	set_col_matriz(U,get_col(A,0),0)
	for k in range(1,n):
		b=vector_cero(m)
		for j in range(k):
			c=prod_int(get_col(U,j),get_col(A,k))/prod_int(get_col(U,j),get_col(U,j))
			b=sum_vector(b,prod_escalar_vector(get_col(U,j),c))
		##fin for
		aux=prod_escalar_vector(b,-1.0)
		u=sum_vector(get_col(A,k),aux)
		set_col_matriz(U,u,k)
	#fin for
	#seguimos operando para encontrar Q y R
	Q=matriz_cero(m,n)
	##usaremos redondeo a 4 digitos
	for i in range(n):
		d=round(1.0/norma(get_col(U,i)),4)
		q=prod_escalar_vector(get_col(U,i),d)
		set_col_matriz(Q,q,i)
	#fin for y hallamos Q
	#hallamos R ahora R=Qt*A
	R=mul_matriz(transpuesta(Q),A)
	return Q,R	

def main():
	#A=[[12.0,-51.0,4.0],[6.0,167.0,-68.0],[-4.0,24.0,-41.0]]
	##print_matriz(A)
	#A = [4,-1,0,-1,0,0],[-1,4,-1,0,-1,0],[0,-1,4,0,0,-1],[-1,0,0,4,-1,0],[0,-1,0,-1,4,-1],[0,0,-1,0,-1,4]	
	A=[[1.0,1.0,1.0,0.0,0.0,0.0],[0.0,-1.0,0.0,1.0,-1.0,0.0],[0.0,0.0,-1.0,0.0,0.0,1.0],[0.0,0.0,0.0,0.0,1.0,-1.0],		[0.0,10.0,-10.0,0.0,-15.0,-5.0],[5.0,-10.0,0.0,-20.0,0.0,0.0]] 
	b=[0.0,0.0,0.0,0.0,0.0,200.0]		
	Q,R=GramSchmidt(A)
	print_matriz(Q)
	print '\n'	
	print 'matriz R es :'
	print_matriz(R)
	c=mul_vector_matriz(transpuesta(Q),b)
	##solucion del sistema
	x=sol_regresivo(R,c)
	print 'la solucion del sistema es :\n'
	print x
main()	

	  	


