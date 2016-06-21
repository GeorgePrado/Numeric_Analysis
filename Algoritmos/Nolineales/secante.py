from sympy import *
global x
x=symbols("x")

def funcion() :
	exp=raw_input("Ingresa la funcion con variable x :\n")
	fx=sympify(exp)	
	return fx

def method_secante(P0,P1,tol,max_iter) :
	i=2
	p0=P0
	p1=P1
	fx=funcion()
	q0=fx.evalf(subs={x:p0})
	q1=fx.evalf(subs={x:p1})
	while i <= max_iter :
		p=p1-round((q1*(p1-p0))/(q1-q0),10)
		print 'iteracion :' + str(i) + '  ' + 'pn  : ' + str(p)
		if abs(p-p1) < tol :
			print 'la solucion es :'
			print p
			break
		i=i+1
		p0=p1
		q0=q1
		p1=p
		q1=fx.evalf(subs={x:p})
	#fin del bucle
	if i >= max_iter :
		print 'metodo fracaso'
#fin del metodo

def main():
	P1=3.14/4.0
	P0=0.5
	tol=0.0001
	max_iter=30
	method_secante(P0,P1,tol,max_iter) 

main()	 
