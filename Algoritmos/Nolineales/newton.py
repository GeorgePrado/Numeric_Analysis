from sympy import *
global x
x=symbols("x")

def funcion() :
	exp=raw_input("Ingresa la funcion con variable x :\n")
	fx=sympify(exp)	
	return fx

def method_newton(P,tol,max_iter) :
	p0=P
	i=1
	fx=funcion()
	gx=fx/diff(fx,x)
	while i <= max_iter :
		p=p0-round(gx.evalf(subs={x:p0}),10)
		print 'iteracion :' + str(i) + '  ' + 'pn  : ' + str(p)
		if abs(p-p0)/abs(p) < tol :
			print '\n'
			print 'una raiz de la ecuacion es :'
			print p
			break
		i=i+1
		p0=p
	#fin del bucle
	if i >= max_iter :
		print 'metodo fracaso'
#fin del metodo

def main():
	A=1.0
	B=2.0
	P=(A+B)/2.0
	tol=0.0001
	max_iter=30
	method_newton(P,tol,max_iter) 

main()	 
	
