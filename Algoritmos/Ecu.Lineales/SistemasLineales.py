##Maguinha Aranda Franz
##20134103C
'''
El siguiente programa resuelve el sistema Ax = b usando los
algoritmos que se muestran en el menu, si ocurre una division
entre cero, el algoritmo deja de ejecurtarse y muestra un
mensaje de aviso y procede a ejecutar el mismo algoritmo
pero usando pivoteo parcial, en el caso de eliminacion de Gauss
usa Gauss-Jordan, Pivoteo Total y Pivoteo Parcial.
Si quiere cambiar los valores de la matriz A y del vector b,
estos se encuentran en la linea 1107 y 1108 respectivamente.
'''
from math import *

#####################################################
##IMPRESION DE MATRICES Y VECTORES
#####################################################
def printMatrixVector(A,b):
  for i in range(len(A)):
    print '|',
    for j in range(len(A[i])):
      print '{0:8.4f}'.format(A[i][j]),
    print '|{0:8.4f}'.format(b[i]),'|'
  print

def printMatrix(A):
  for i in range(len(A)):
    print '|',
    for j in range(len(A[i])):
      print '{0:8.4f}'.format(A[i][j]),
    print '|'
  print

def printVector(c):
  print '[',
  for i in range(len(c)):
    print '{0:8.4f}'.format(c[i]),
  print ']'

#####################################################
##ELIMINACION DE GAUSS
#####################################################
def eliminacionGauss(A,b,n):
  op = 0
  ##inicializando un arreglo x en 0
  x = []
  for i in range(n):
    x = [0] * n
  for k in range(n-1):
    for i in range(k+1,n):
      m = A[i][k]/A[k][k]
      op = op + 1
      for j in range(k,n):
        A[i][j] = A[i][j] - m*A[k][j]
        op = op + 2
      b[i] = b[i] - m*b[k]
      op = op + 2
  x[n-1] = b[n-1]/A[n-1][n-1]
  op = op + 1
  for i in range(n-2,-1,-1):
    x[i] = b[i]
    for j in range (i+1,n):
      x[i] = x[i] - A[i][j]*x[j]
      op = op + 2
    x[i] = x[i]/A[i][i]
    op = op + 1
  return x,op
##ELIMINACION DE GAUSS A UNA MATRIZ TRIANGULAR SUPERIOR
def eliminacionGaussTriangularSuperior(A,b,n):
  op = 0
  ##inicializando un arreglo x en 0
  x = []
  for i in range(n):
    x = [0] * n
  x[n-1] = b[n-1]/A[n-1][n-1]
  op = op + 1
  for i in range(n-2,-1,-1):
    x[i] = b[i]
    for j in range (i+1,n):
      x[i] = x[i] - A[i][j]*x[j]
      op = op + 2
    x[i] = x[i]/A[i][i]
    op = op + 1
  return x,op
##ELIMINACION DE GAUSS A UNA MATRIZ TRIANGULAR INFERIOR
def eliminacionGaussTriangularInferior(A,b,n):
  op = 0
  ##inicializando un arreglo x en 0
  x = []
  for i in range(n):
    x = [0] * n
  x[0] = b[0]/A[0][0]
  op = op + 1
  for i in range(1,n):
    x[i] = b[i]
    for j in range (0,i):
      x[i] = x[i] - A[i][j]*x[j]
      op = op + 2
    x[i] = x[i]/A[i][i]
    op = op + 1
  return x,op

##ELIMINACION DE GAUSS-JORDAN
def eliminacionGaussJordan(A,b,n):
  op = 0
  ##inicializando un arreglo x en 0
  x = []
  for i in range(n):
    x = [0] * n
  for j in range(n-1):
    if A[j][j] == 0:
      p = j
      for i in range(j+1,n):
        if abs(A[i][j]) > abs(A[p][j]):
          p = i
      for k in range(n):
        A[p][k],A[j][k] = A[j][k],A[p][k]
      b[p],b[j] = b[j],b[p]
    for i in range(j+1,n):
      m = A[i][j]/A[j][j]
      op = op + 1
      for k in range(j,n):
        A[i][k] = A[i][k] - m*A[j][k]
        op = op + 2
      b[i] = b[i] - m*b[j]
      op = op + 2
  for j in range(n-1,0,-1):
    for i in range(j-1,-1,-1):
      m = A[i][j]/A[j][j]
      op = op + 1
      for k in range(j,n):
        A[i][k] = A[i][k] - m*A[j][k]
        op = op + 2
      b[i] = b[i] - m*b[j]
      op = op + 2
  for i in range(n):
    x[i] = b[i]/A[i][i]
    op = op + 1
  return x,op
#####################################################
##ELIMINACION DE GAUSS CON PIVOTE TOTAL
#####################################################
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
def eliminacionGaussPivoteoTotal(A,b,n):
  op = 0
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
      op = op + 1
      for j in range(k+1,n):
        A[i][j] = A[i][j] - m*A[k][j]
        op = op + 2
      b[i] = b[i] - m*b[k]
      op = op + 2
  x[n-1] = b[n-1]/A[n-1][n-1]
  op = op + 1
  for i in range(n-2,-1,-1):
    x[i] = b[i]
    for j in range (i+1,n):
      x[i] = x[i] - A[i][j]*x[j]
      op = op + 2
    x[i] = x[i]/A[i][i]
    op = op + 1
  return x,op
#####################################################
##ELIMINACION DE GAUSS CON PIVOTE PARCIAL
#####################################################
def eliminacionGaussPivoteoParcial(A,b,n):
  op = 0
  x = [0 for i in range(n)]
  for i in range(0,n):
    maximo = abs(A[i][i])
    i_max = i
    for k in range(i+1, n):
      if abs(A[k][i]) > maximo:
        maximo = abs(A[k][i])
        i_max = k
    for k in range(i, n):
      A[i_max][k],A[i][k] = A[i][k],A[i_max][k] 
    b[i_max],b[i] = b[i],b[i_max]
    for k in range(i+1, n):
      m = A[k][i]/A[i][i]
      op = op + 1
      for j in range(i, n):
        A[k][j] = A[k][j] - m*A[i][j]
        op = op + 2
      b[k] = b[k] - m*b[i]
      op = op + 2
  x[n-1] = b[n-1]/A[n-1][n-1]
  op = op + 1
  for i in range(n-2,-1,-1):
    x[i] = b[i]
    for j in range (i+1,n):
      x[i] = x[i] - A[i][j]*x[j]
      op = op + 2
    x[i] = x[i]/A[i][i]
    op = op + 1
  return x,op

#####################################################
##FACTORIZACION LU1 - CROUT
#####################################################
def factorizacionLU1(A,b,n):
  op = 0
  L = []
  for i in range(n):
    L.append([0]*n)
  U = []
  for i in range(n):
    U.append([])
    for j in range(n):
      U[i].append(0)
      if i == j:
        U[i][j] = 1

  for k in range(n):
    for i in range(k,n):
      L[i][k] = A[i][k]
      for p in range(0,k):
        L[i][k] = L[i][k] - L[i][p]*U[p][k]
        op = op + 2
    for i in range(k+1,n):
      U[k][i] = A[k][i]
      for p in range(0,k):
        U[k][i] = U[k][i] - L[k][p]*U[p][i]
        op = op + 2
      U[k][i] = U[k][i]/L[k][k]
      op = op + 1

  op2 = 0
  print "L:"
  printMatrix(L)
  print "U:"
  printMatrix(U)
  y,op2 = eliminacionGaussTriangularInferior(L,b,n)
  op = op + op2
  print "Solucion y:"
  printVector(y)
  x,op2 = eliminacionGaussTriangularSuperior(U,y,n)
  op = op + op2
  return x,op
#####################################################
##FACTORIZACION LU1 PIVOTEO PARCIAL
#####################################################
def factorizacionLU1PivoteoParcial(A,b,n):
  op = 0
  L = []
  for i in range(n):
    L.append([0]*n)
  U = []
  for i in range(n):
    U.append([])
    for j in range(n):
      U[i].append(0)
      if i == j:
        U[i][j] = 1

  for k in range(n):
    maximo = abs(A[k][k])
    p = k
    for i in range(k+1,n):
      if maximo < abs(A[i][k]):
        maximo = abs(A[i][k])
        p = i
    for i in range(n):
      A[p][i],A[k][i] = A[k][i],A[p][i]
    b[k],b[p] = b[p],b[k]
    for i in range(k,n):
      L[i][k] = A[i][k]
      for p in range(0,k):
        L[i][k] = L[i][k] - L[i][p]*U[p][k]
        op = op + 2
    for i in range(k+1,n):
      U[k][i] = A[k][i]
      for p in range(0,k):
        U[k][i] = U[k][i] - L[k][p]*U[p][i]
        op = op + 2
      U[k][i] = U[k][i]/L[k][k]
      op = op + 1
  op2 = 0
  print "L:"
  printMatrix(L)
  print "U:"
  printMatrix(U)
  y,op2 = eliminacionGaussTriangularInferior(L,b,n)
  op = op + op2
  print "Solucion y:"
  printVector(y)
  x,op2 = eliminacionGaussTriangularSuperior(U,y,n)
  op = op + op2
  return x,op
#####################################################
##FACTORIZACION L1U - DOOLITTLE
#####################################################
def factorizacionL1U(A,b,n):
  op = 0
  L = []
  for i in range(n):
    L.append([])
    for j in range(n):
      L[i].append(0)
      if i == j:
        L[i][j] = 1
  U = []
  for i in range(n):
    U.append([0]*n)

  for k in range(n):
    for j in range(k,n):
      U[k][j] = A[k][j]
      for p in range(0,k):
        U[k][j] = U[k][j] - L[k][p]*U[p][j]
        op = op + 2
    for i in range(k+1,n):
      L[i][k] = A[i][k]
      for p in range(0,k):
        L[i][k] = L[i][k] - L[i][p]*U[p][k]
        op = op + 2
      L[i][k] = L[i][k]/U[k][k]
      op = op + 1

  print "L:"
  printMatrix(L)
  print "U:"
  printMatrix(U)
  op2 = 0
  y,op2 = eliminacionGaussTriangularInferior(L,b,n)
  op = op + op2
  print "Solucion y:"
  printVector(y)
  x,op2 = eliminacionGaussTriangularSuperior(U,y,n)
  op = op + op2
  return x,op

#####################################################
##FACTORIZACION L1U PIVOTEO PARCIAL
#####################################################
def factorizacionL1UPivoteoParcial(A,b,n):
  op = 0
  L = []
  for i in range(n):
    L.append([])
    for j in range(n):
      L[i].append(0)
      if i == j:
        L[i][j] = 1
  U = []
  for i in range(n):
    U.append([0]*n)

  for k in range(n):
    maximo = abs(A[k][k])
    p = k
    for i in range(k+1,n):
      if maximo < abs(A[i][k]):
        maximo = abs(A[i][k])
        p = i
    for i in range(n):
      A[p][i],A[k][i] = A[k][i],A[p][i]
    b[k],b[p] = b[p],b[k]
    for j in range(k,n):
      U[k][j] = A[k][j]
      for p in range(0,k):
        U[k][j] = U[k][j] - L[k][p]*U[p][j]
        op = op + 2
    for i in range(k+1,n):
      L[i][k] = A[i][k]
      for p in range(0,k):
        L[i][k] = L[i][k] - L[i][p]*U[p][k]
        op = op + 2
      L[i][k] = L[i][k]/U[k][k]
      op = op + 1

  print "L:"
  printMatrix(L)
  print "U:"
  printMatrix(U)
  op2 = 0
  y,op2 = eliminacionGaussTriangularInferior(L,b,n)
  op = op + op2
  print "Solucion y:"
  printVector(y)
  x,op2 = eliminacionGaussTriangularSuperior(U,y,n)
  op = op + op2
  return x,op
#####################################################
##FACTORIZACION LDLt
#####################################################
##Devuelve una matriz S simetrica que es igual a A multiplicado por su transpuesta, tambien devuelve su transpuesta
def simetrico(A):
  n = len(A)
  At = []
  S = []
  for i in range(n):
    At.append([0]*n)
    S.append([0]*n)
  
  for i in range(n):
    for j in range(n):
      At[j][i] = A[i][j]
  for i in range(n):
    for j in range(n):
      for k in range(n):
        S[i][j] = S[i][j] + At[i][k]*A[k][j]
  return At,S
def factorizacionLDLt(A,b,n):
  op = op2 = 0

  L = []
  Lt = []
  for i in range(n):
    L.append([])
    Lt.append([])
    for j in range(n):
      L[i].append(0)
      Lt[i].append(0)
      if i == j:
        L[i][j] = Lt[i][j] = 1
  D = []
  for i in range(n):
    D.append([0]*n)
  At,A = simetrico(A)
  b = multMatrixVector(At,b)
  for k in range(n):
    D[k][k] = A[k][k]
    for p in range(0,k):
      D[k][k] = D[k][k] - A[k][p]*A[k][p]*D[p][p]
      op = op + 3
    if D[k][k] == 0:
      break
    for i in range(k+1,n):
      for p in range(0,k):
        A[i][k] = A[i][k] - A[i][p]*A[k][p]*D[p][p]
        op = op + 3
      A[i][k] = A[i][k]/D[k][k]
      op = op + 1
  for i in range(n):
    for j in range(n):
      if j < i:
        L[i][j] = Lt[j][i] = A[i][j]
  print "L:"
  printMatrix(L)
  print "D:"
  printMatrix(D)
  print "Lt:"
  printMatrix(Lt)
  z,op2 = eliminacionGaussTriangularInferior(L,b,n)
  op = op + op2
  print "Solucion z:"
  printVector(z)
  y,op2 = eliminacionGauss(D,z,n)
  op = op + op2
  print
  print "Solucion y:"
  printVector(y)
  x,op2 = eliminacionGaussTriangularSuperior(Lt,y,n)
  op = op + op2
  return x,op
#####################################################
##FACTORIZACION CHOLESKY
#####################################################
def multMatrixVector(A,b):
  n = len(A)
  c = [0 for i in range(n)]
  for i in range(n):
    for j in range(n):
      c[i] = c[i] + A[i][j]*b[j]
  return c
def factorizacionCholesky(A,b,n):
  op = op2 = 0
  G = []
  Gt = []
  for i in range(n):
    G.append([0]*n)
    Gt.append([0]*n)
  At,A = simetrico(A)
  b = multMatrixVector(At,b)

  for i in range(n):
    G[i][i] = A[i][i]
    for k in range(0,i):
      G[i][i] = G[i][i] - G[k][i]*G[k][i]
      op = op + 2
    G[i][i] = sqrt(G[i][i])
    op = op + 1
    for j in range(i+1,n):
      G[i][j] = A[i][j]
      for k in range(0,i):
        G[i][j] = G[i][j] - G[k][i]*G[k][j]
        op = op + 2
      G[i][j] = G[i][j]/G[i][i]
      op = op + 1
  for i in range(n):
    for j in range(n):
      Gt[j][i] = G[i][j]
  print "Gt:"
  printMatrix(Gt)
  print "G:"
  printMatrix(G)
  y,op2 = eliminacionGaussTriangularInferior(Gt,b,n)
  op = op + op2
  print "Solucion y:"
  printVector(y)
  x,op2 = eliminacionGaussTriangularSuperior(G,y,n)
  op = op + op2
  return x,op

#####################################################
##FACTORIZACION GRAM-SCHMIDT
#####################################################
def multMatrix(A,B,n):
  C = []
  for i in range(n):
    C.append([0]*n)

  for i in range(n):
    for j in range(n):
      for k in range(n):
        C[i][j] = C[i][j] + A[i][k]*B[k][j]
  return C
def Identidad(n,m):
	I = []
	for j in range(n):
		I.append([0]*m)
	for i in range(n):
		for j in range(m):
			if i == j:
				I[i][i] = 1
	return I
def Inversa(A,n):
  B = []
  I = []
  for i in range(n):
    B.append([0]*n)
    I.append([0]*n)
  for i in range(n):
    I[i][i] = 1
  for i in range(n):
    B[i]=eliminacionGauss(A,I[i],n)
  return B
def matrizInversa(A):
  n = len(A)
  I = Identidad(n)
  
  for j in range(n-1):
    if A[j][j]==0:
      p=j
      for i in range(j+1,n):
        if abs(A[i][j])>abs(A[p][j]):
          p=i
      for k in range(n):
        A[p][k],A[j][k]=A[j][k],A[p][k]
        I[p][k],I[j][k]=I[j][k],I[p][k]
    for i in range(j+1,n):
      m=A[i][j]/A[j][j]
      for k in range(n):
        A[i][k]=A[i][k]-m*A[j][k]
      for k in range(n):
        I[i][k]=I[i][k]-m*I[j][k]
  for j in range(n-1,0,-1):
    for i in range(j-1,-1,-1):
      m=A[i][j]/A[j][j]
      for k in range(j,n):
        A[i][k]=A[i][k]-m*A[j][k]
      for k in range(n):
        I[i][k]=I[i][k]-m*I[j][k]
  return I
def transpuesta(A):
	At = []
	for j in range(len(A[0])):
		At.append([0]*len(A))
	for i in range(len(A)):
		for j in range(len(A[0])):
			At[j][i] = A[i][j]
	return At
def factorizacionGramSchmidt(A,b,m,n):
	U = []
	e = []
	op = op2= 0
	for i in range(n):
		U.append([0]*n)
	for i in range(m):
		e.append([0]*n)
	for j in range(n):
		for p in range(m):
			e[p][j] = A[p][j]
		for i in range(j):
			for p in range(m):
				U[i][j] = U[i][j] + e[p][i]*e[p][j]
				op = op + 2
			for p in range(m):
				e[p][j] = e[p][j] - U[i][j]*e[p][i]
				op = op + 2
		for k in range(m):
			U[j][j] = U[j][j] + e[k][j]*e[k][j]
			op = op + 2
		U[j][j] = sqrt(U[j][j])
		op = op + 1
		for p in range(m):
			e[p][j] = e[p][j]/U[j][j]
			op = op + 1
	print 'e:'
	printMatrix(e)
	print 'U'
	printMatrix(U)
	b = multMatrixVector(transpuesta(e),b)
	x,op2 = eliminacionGaussTriangularSuperior(U,b,n)
	op = op + op2
	return x,op
#####################################################
##FACTORIZACION QR
#####################################################
def norm_2(x):
  return sqrt(sum([x_i**2 for x_i in x]))
def Q_i(Q_min, i, j, k):
  if i < k or j < k:
    return float(i == j)
  else:
    return Q_min[i-k][j-k]
def factorizacionQR(A,b,n):
  op = op2 = 0
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
  y,op2 = eliminacionGauss(Q,b,n)
  op = op + op2
  print "Solucion y:"
  printVector(y)
  x,op2 = eliminacionGaussPivoteoTotal(R,y,n)
  op = op + op2
  return x,op

def HouseHolder(A,b):
	n = len(A)
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
			R = multMatriz(Q_t,A)
		else:
			Q = multMatriz(Q_t,Q)
			R = multMatriz(Q_t,R)
		
	Q = transpuesta(Q)
	print "Q:"
	printMatrix(Q)
	print "R:"
	printMatrix(R)
	y,op2 = eliminacionGauss(Q,b,n)
	op = op + op2
	print "Solucion y:"
	printVector(y)
	x,op2 = eliminacionGaussPivoteoTotal(R,y,n)
	op = op + op2
	return x,op


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

			cosX = a / (sqrt(a*a + b*b)) 
			sinX = -b / (sqrt(a*a + b*b))

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


#####################################################
##MENU
#####################################################
def menu():
  print "======= M E N U ======="
  print "1. Metodo de Gauss"
  print "2. Factorizacion LU1 Crout"
  print "3. Factorizacion L1U Doolittle"
  print "4. Factorizacion LDLt"
  print "5. Factorizacion Cholesky"
  print "6. Factorizacion QR"
  print "7. Factorizacion Gram-Schmidt"
  print "8. HouseHolder"
  print "9. Rotacion de Givens"	
  print "10. Salir"
#####################################################
##MAIN
#####################################################
if __name__ == '__main__':
  opc = 1
  #A = [4,-1,0,-1,0,0],[-1,4,-1,0,-1,0],[0,-1,4,0,0,-1],[-1,0,0,4,-1,0],[0,-1,0,-1,4,-1],[0,0,-1,0,-1,4]
  #b = [56,25,62,41,10,47]
  A=[[1.0,1.0,1.0,0.0,0.0,0.0],[0.0,-1.0,0.0,1.0,-1.0,0.0],[0.0,0.0,-1.0,0.0,0.0,1.0],[0.0,0.0,0.0,0.0,1.0,-1.0],		[0.0,10.0,-10.0,0.0,-15.0,-5.0],[5.0,-10.0,0.0,-20.0,0.0,0.0]]
  b=[0.0,0.0,0.0,0.0,0.0,200.0]	
  n = len(A)
  print "Sistema Lineal Ax = b"
  printMatrixVector(A,b)
  while opc != 10:
    A1 = []
    A2 = []
    A3 = []
    A4 = []
    for i in range(n):
      A1.append([0]*n)
      A2.append([0]*n)
      A3.append([0]*n)
      A4.append([0]*n)
    b1 = [0 for i in range(n)]
    b2 = [0 for i in range(n)]
    b3 = [0 for i in range(n)]
    b4 = [0 for i in range(n)]
    op = 0
    for i in range(n):
      b1[i] = b2[i] = b3[i] = b4[i] = b[i] 
      for j in range(n):
        A1[i][j] = A2[i][j] = A3[i][j] = A4[i][j] = A[i][j]
    menu()
    opc = int(raw_input("Ingrese opcion: "))
    ##printMatrix(A)
    ##printVector(b)
    if opc == 1:
      try:
        x,op = eliminacionGauss(A1,b1,n)
        print "Solucion x con Gauss:"
        printVector(x)
        print "Nro. Operaciones: ",op
        print
      except ZeroDivisionError:
        print "No se puede factorizar por Gauss, division entre cero inminente"
        print
      finally:
        x,op = eliminacionGaussJordan(A2,b2,n)
        print "Solucion x con Gauss-Jordan:"
        printVector(x)
        print "Nro. Operaciones: ",op
        print
        x,op = eliminacionGaussPivoteoTotal(A3,b3,n)
        print "Solucion x con Gauss Pivoteo Total:"
        printVector(x)
        print "Nro. Operaciones: ",op
        print
        x,op = eliminacionGaussPivoteoParcial(A4,b4,n)
        print "Solucion x con Gauss Pivoteo Parcial:"
        printVector(x)
        print "Nro. Operaciones: ",op
        print
        
    elif opc == 2:
      try:
        print "Factorizacion LU1:"
        x,op = factorizacionLU1(A1,b1,n)
        print
        print "Solucion x:"
        printVector(x)
        print "Nro. Operaciones: ",op
        print
      except ZeroDivisionError:
        print "No se puede factorizar por LU1, division entre cero inminente"
        print
      finally:
        print "Factorizacion LU1 Pivoteo Parcial:"
        x,op = factorizacionLU1PivoteoParcial(A2,b2,n)
        print
        print "Solucion x:"
        printVector(x)
        print "Nro. Operaciones: ",op
        print
    elif opc == 3:
      try:
        print "Factorizacion L1U:"
        x,op = factorizacionL1U(A1,b1,n)
        print
        print "Solucion x:"
        printVector(x)
        print "Nro. Operaciones: ",op
        print
      except ZeroDivisionError:
        print "No se puede factorizar por L1U, division entre cero inminente"
        print
      finally:
        print "Factorizacion L1U Pivoteo Parcial:"
        x,op = factorizacionL1UPivoteoParcial(A1,b1,n)
        print
        print "Solucion x:"
        printVector(x)
        print "Nro. Operaciones: ",op
        print
    elif opc == 4:
      try:
        print "Factorizacion LDLt"
        x,op = factorizacionLDLt(A1,b1,n)
        print
        print "Solucion x:"
        printVector(x)
        print "Nro. Operaciones: ",op
        print
      except ZeroDivisionError:
        print "No se puede factorizar por LDLt, division entre cero inminente"
        print
    elif opc == 5:
      try:
        print "Factorizacion Cholesky:"
        x,op = factorizacionCholesky(A1,b1,n)
        print
        print "Solucion x:"
        printVector(x)
        print "Nro. Operaciones: ",op
        print
      except ZeroDivisionError:
        print "No se puede factorizar por Cholesky, division entre cero inminente"
        print
      except ValueError:
        print "No se puede factorizar por Cholesky, raiz de un imaginario inminete"
        print
    elif opc == 6:
      try:
        print "Factorizacion Gram-Schmidt:"
        x,op = factorizacionGramSchmidt(A1,b1,len(A),len(A[0]))
        print "Solucion x:"
        printVector(x)
        print "Nro. Operaciones: ",op
        print
      except ZeroDivisionError:
        print "No se puede factorizar por Gram-Schmidt, division entre cero inminente"
        print
    elif opc == 7:
      try:
        print "Factorizacion QR:"
        x,op = factorizacionQR(A1,b1,n)
        print "Solucion x:"
        printVector(x)
        print "Nro. Operaciones: ",op
        print
      except ZeroDivisionError:
        print "No se puede factorizar por QR, division entre cero inminente"
        print
	elif opc == 8 :
      try:
        print "Factorizacion QR:"
        x,op = factorizacionQR(A1,b1,n)
        print "Solucion x:"
        printVector(x)
        print "Nro. Operaciones: ",op
        print
      except ZeroDivisionError:
        print "No se puede factorizar por QR, division entre cero inminente"
        print
	elif opc == 9:
      try:
        print "Factorizacion QR:"
        x,op = factorizacionQR(A1,b1,n)
        print "Solucion x:"
        printVector(x)
        print "Nro. Operaciones: ",op
        print
      except ZeroDivisionError:
        print "No se puede factorizar por QR, division entre cero inminente"
        print
    elif opc == 10:
      print "Saliendo ..."
    else:
      print "Opcion Incorrecta, intente de nuevo ..."
      print
