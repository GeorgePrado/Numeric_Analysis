def vector_cero(n):
	V=[]
	for i in range(n):
		V.append(0.0)
	
	return V

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
 
#en esta seccion del codigo esta el algoritmo iterativo jacobi
def metodo_jacobi(A,b,xi):
	n=len(A)
	tol=0.000001	
	N=30
	k=1
	xk=xi
	x=vector_cero(n)
	

	while k < N :
		for i in range(n):
			t=0.0
			for j in range(n):
				if i != j :
					t=t+A[i][j]*xk[j]
			##fin para
			x[i]=round((b[i]-t)/A[i][i],7)
		#fin para
		g=sum_vector(x,prod_escalar_vector(xk,-1.0))
		p=norma(g)
		if p < tol :
			print xk
			break
		
		print x
		print '\n'
		k=k+1

		for m in range(n):
			xk[m]=x[m]		
	##fin mientras
	if k >= N :	
		print 'Numero maximo de iteraciones excedido'

def main():
	#A=[[10.0,-1.0,2.0,0.0],[-1.0,11.0,-1.0,3.0],[2.0,-1.0,10.0,-1.0],[0.0,3.0,-1.0,8.0]]
	#b=[6.0,25.0,-11.0,15.0]
	A=[[4.0,-1.0,-1.0,0.0,0.0,0.0],[-1.0,4.0,0.0,-1.0,0.0,0.0],[-1.0,0.0,4.0,-1.0,-1.0,0.0],[0.0,-1.0,-1.0,4.0,0.0,-1.0],[0.0,0.0,-1.0,0.0,4.0,-1.0],[0.0,0.0,0.0,-1.0,-1.0,4.0]]
	b=[2.0,2.0,2.0,2.0,2.0,2.0]	
	xi=[0.0,1.0,0.0,1.0,0.0,1.0]
	metodo_jacobi(A,b,xi)


main()
	
