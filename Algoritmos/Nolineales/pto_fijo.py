from sympy import *
global x
x=symbols("x")

def funcion() :
	exp=raw_input("Ingresa la funcion con variable x :\n")
	#x=symbols("x")
	fx=sympify(exp)
	#c=fx.evalf(subs={x:2.0})
	#print c	
	return fx

def pto_fijo(P,tol,max_iter) :
	p0=P
	i=1
	fx=funcion()
	while i <= max_iter :
		p=fx.evalf(subs={x:p0})
		print p
		if abs(p-p0) < tol :
			print 'el pto fijo para la ecuacion es :'
			print p
			break
		i=i+1
		p0=p
	##fin del bucle
	if i >= max_iter :
		print 'el metodo fracaso'


def main():
	A=1.0
	B=2.0
	P=(A+B)/3.0
	tol=0.0001
	max_iter=30
	pto_fijo(P,tol,max_iter)

main()
		
