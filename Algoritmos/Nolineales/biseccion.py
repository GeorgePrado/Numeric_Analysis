from sympy import *
global x
x=symbols("x")

def funcion() :
	exp=raw_input("Ingresa la funcion con variable x :\n")
	fx=sympify(exp)	
	return fx

def method_bisection(A,B,tol,max_iter) :
	a=A
	b=B	
	i=1	
	fx=funcion()
	FA=fx.evalf(subs={x:a})
	pn=a	
	while i <= max_iter :
		p=a+(b-a)/2.0
		FP=fx.evalf(subs={x:p})
		if FP == 0.0  or abs(p-pn)/abs(p) < tol :
			print 'una raiz de la ecuacion es :'
			print p
			break
		##sino sigue en el bucle
		i=i+1
		if FA*FP> 0.0 :
			a=p
			FA=FP
		else :
			b=p
		pn=p
		
	if i > max_iter :
		print 'el metodo fracaso'

def main():
	A=1.0
	B=2.0
	tol=0.0001
	max_iter=20
	method_bisection(A,B,tol,max_iter)

main()
#funcion()		



