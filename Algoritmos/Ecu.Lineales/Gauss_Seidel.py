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
def metodo_GaussSeidel(A,b,xi):
	n=len(A)
	tol=0.001	
	N=50
	k=1
	xk=xi
	x=vector_cero(n)
	
	while k < N :
		for i in range(n):
			t=0.0
			d=0.0
			for j in range(0,i):
				t=t+A[i][j]*x[j]
			##fin para
			for l in range(i+1,n):
				d=d+A[i][l]*xk[l]
			x[i]=round((b[i]-(t+d))/A[i][i],4)
		#fin para
		g=sum_vector(x,prod_escalar_vector(xk,-1.0))
		p=norma(g)
		if p < tol :
			print '\n'
			print 'la solucion es :'			
			print xk
			break
		
		print 'iteracion ' + str(k) 
		print x
		
		k=k+1

		for m in range(n):
			xk[m]=x[m]		
	##fin mientras
	if k >= N :	
		print 'Numero maximo de iteraciones excedido'

def main():
	#A=[[10.0,-1.0,2.0,0.0],[-1.0,11.0,-1.0,3.0],[2.0,-1.0,10.0,-1.0],[0.0,3.0,-1.0,8.0]]
	#b=[6.0,25.0,-11.0,15.0]
	#A=[[4.0,-1.0,-1.0,0.0,0.0,0.0],[-1.0,4.0,0.0,-1.0,0.0,0.0],[-1.0,0.0,4.0,-1.0,-1.0,0.0],[0.0,-1.0,-1.0,4.0,0.0,-1.0],[0.0,0.0,-1.0,0.0,4.0,-1.0],[0.0,0.0,0.0,-1.0,-1.0,4.0]]
	#b=[2.0,2.0,2.0,2.0,2.0,2.0]
	A=[[-1.0,0.0,0.0,0.7071,1.0,0.0,0.0,0.0],[0.0,-1.0,0.0,0.7071,0.0,0.0,0.0,0.0],[0.0,0.0,-1.0,0.0,0.0,0.0,0.5,0.0],[0.0,0.0,0.0,-0.7071,0.0,-1.0,0.5,0.0],[0.0,0.0,0.0,0.0,-1.0,0.0,0.0,1.0],[0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0],[0.0,0.0,0.0,-0.7071,0.0,0.0,0.86603,0.0],[0.0,0.0,0.0,0.0,0.0,0.0,-0.86603,-1.0]]		 	 	
  	b=[0.0,0.0,0.0,0.0,0.0,10000.0,0.0,0.0]
	#xi=[0.0,1.0,0.0,1.0,0.0,1.0]	
	xi=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
	metodo_GaussSeidel(A,b,xi)


main()
