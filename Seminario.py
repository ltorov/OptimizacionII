# -*- coding: utf-8 -*-
"""Seminario1Optimizacion.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gMrRn1ijlUpjhu4zqqJ56boHWgSIPTLt
"""

pip install sympy

import math
import sympy as sym
from sympy.solvers import solve
import time

"""Punto 1

Método del gradiente
"""

start = time.time()

""" Parámetros
  Se definen los valores iniciales de los parámetros.
  x1inicial, x2inicial: son los puntos iniciales con los que empieza a iterar el algoritmo
  eps: tolerancia, la escogemos nosotros
"""

x1inicial = 0.5
x2inicial = 1.5
eps = 0.01 #tolerancia (nosotros escogemos)

""" Variables
  Se definen las siguientes como variables usando la librería sympy para operarlos.
  x1, x2 : las variables de la función objetivo f(x1, x2)
  lam : el parámetro de penalización
"""

x1 = sym.Symbol('x1')
x2 = sym.Symbol('x2')
lam = sym.Symbol('lam') #lambda

""" Funciones
  Función que depende de las variables anteriores.
  f : función objetivo penalizada.
"""

f = 8 * (x1**2) + 6 *(x2 ** 2) + (4 * (x1 - 1) * (x2 - 2))

"""Métodos auxiliares
  gradiente : toma dos parámetros (dos puntos), calcula la gradiente (diferenciando) y la evalua en los puntos dados.
"""

def gradiente (xn1, xn2):
  gradientex1 = sym.diff(f,x1)
  gradientex2 = sym.diff(f,x2)
  auxx1 = gradientex1.subs(x1,xn1)
  auxx2 = gradientex2.subs(x1,xn1)
  return auxx1.subs(x2,xn2), auxx2.subs(x2,xn2)
  
"""Métodos principales
  metodoGradiente: implementa el algoritmo del gradiente tomando como parámetros iniciales la tolerancia, los puntos iniciales, y la función. 
  El método realiza 10 iteraciones e imprime cuando converge la función y los puntos en los cuales converge.
"""
def metodoGradiente (eps, x1inicial, x2inicial, f):

  gradienteInicialx1, gradienteInicialx2 = gradiente (x1inicial, x2inicial)
  normaGradiente = math.sqrt((gradienteInicialx1 ** 2) + (gradienteInicialx2 ** 2))

  if normaGradiente < eps:
    print("El mínimo de la función fue encontrado en el punto (x1, x2) = (" +str(x10)+", "+str(x20)+") con z = " + str(valorMinimo) )
  else:
    x1n = x1inicial
    x2n = x2inicial
    cont = 0
    for i in range(10):
      minimo = (f.subs(x1,x1n)).subs(x2,x2n)
      gradx1,gradx2 = gradiente(x1n, x2n)
      f1d, f2d = (x1n-lam *gradx1, x2n-lam *gradx2)
      auxfdelambda = f.subs(x1,f1d) 
      fdelambda = auxfdelambda.subs(x2,f2d)
      derivada_fdelambda = sym.diff(fdelambda,lam)
      puntoMaxAux = solve(derivada_fdelambda, lam)
      puntoMax = puntoMaxAux[0]
      normaGradiente = math.sqrt((gradx1 ** 2) + (gradx2 ** 2))
      if normaGradiente<eps and cont == 0 :
        print("El método converge con mínimo de z = "+str(minimo) + " con epsilon o tolerancia de "+ str(eps)+" con los puntos (x1, x2) = ("+str(x1n) + ", " + str(x2n) + ").") 
        cont +=1 
      else:
        print ("La iteración "+ str(i+1)+ " usa los puntos ("+ str(x1n) + ", " + str(x2n)+ ") con un valor de "+ str(minimo)+ ".")
      gx1n,gx2n = gradiente(x1n, x2n)
      x1n = x1n - puntoMax*gx1n
      x2n = x2n - puntoMax*gx2n



"""Correr
"""
metodoGradiente(eps, x1inicial, x2inicial, f)
end = time.time()

print("")
print("El Algorítmo se demoró " + str(end - start) + " Segundos en correr")

"""Método de Newton"""

start = time.time()

""" Parámetros
  Se definen los valores iniciales de los parámetros.
  x1inicial, x2inicial: son los puntos iniciales con los que empieza a iterar el algoritmo
  eps: tolerancia, la escogemos nosotros
"""

x1inicial = 0.5
x2inicial = 1.5
eps = 0.01 #tolerancia (nosotros escogemos)

""" Variables
  Se definen las siguientes como variables usando la librería sympy para operarlos.
  lam : el parámetro de penalización
  x1, x2 : las variables de la función objetivo f(x1, x2)
"""

lam = sym.Symbol('lam') #lambda
x1 = sym.Symbol('x1')
x2 = sym.Symbol('x2')

""" Funciones
  Función que depende de las variables anteriores.
  f : función objetivo penalizada.
"""

f = 8 * (x1**2) + 6 *(x2 ** 2) + (4 * (x1 - 1) * (x2 - 2))

"""Métodos auxiliares
  calcularGradiente : toma dos parámetros (dos puntos), calcula la gradiente (diferenciando) y la evalua en los puntos dados.
  calcularInversaHessiana : calcula la matriz Hessiana con las derivadas correspondientes y la invierte.
  normaGradiente : calcula la norma de un gradiente en dos puntos dados.
"""

def calcularGradiente (xn1, xn2):
  gradientex1 = sym.diff(f,x1)
  gradientex2 = sym.diff(f,x2)
  auxx1 = gradientex1.subs(x1,xn1)
  auxx2 = gradientex2.subs(x1,xn1)
  gradiente = [float((auxx1.subs(x2,xn2)).evalf()), float((auxx2.subs(x2,xn2)).evalf())]
  return gradiente

def calcularInversaHessiana ():
  dfx1 = sym.diff(f,x1)
  dfx2 = sym.diff(f,x2)
  dfxx1 = sym.diff(dfx1,x1)
  dfxx2 = sym.diff(dfx2,x2)
  dfx1x2 = sym.diff(dfx1,x2)
  x11 = int(dfxx1.evalf())
  x22 = int(dfxx2.evalf())
  x12 = int(dfx1x2.evalf())
  matrizHessiana = sym.Matrix([[x11, x12],[x12 , x22]])
  inversa = matrizHessiana **-1
  return inversa

def normaGradiente(xn1, xn2):
  gradiente = calcularGradiente(xn1,xn2)
  x1 = gradiente[0]
  x2 = float(gradiente[1])
  norma = math.sqrt((x1 **2) + (x2 **2))
  return norma

"""Métodos principales
  algoritmoNewton : realiza 10 iteraciones del algoritmo de Newton para la función objetivo dada y cuando converge, 
  muestra el valor de la función en esos puntos y los puntos.
"""
def algoritmoNewton ():
  cont = 0
  xn1 = x1inicial
  xn2 = x2inicial
  norma = normaGradiente(xn1, xn2)
  inversaHessiana = calcularInversaHessiana()
  for i in range(10):
    minimo = (f.subs(x1,xn1)).subs(x2,xn2)
    if norma < eps and cont==0 :
      print("El método converge con mínimo de z = "+str(minimo) + " con epsilon o tolerancia de "+ str(eps)+" con los puntos (x1, x2) = ("+str(xn1) + ", " + str(xn2) + ").")
      cont+=1
    else:
      print ("La iteración "+ str(i+1)+ " usa los puntos (x1, x2) = ("+ str(xn1) + ", " + str(xn2)+ ") con un valor de z = "+ str(minimo)+ ".")
      norma = normaGradiente(xn1, xn2)
      gradiente = sym.Matrix(calcularGradiente(xn1,xn2))
      xnMatriz = sym.Matrix([xn1,xn2]) - inversaHessiana * gradiente
      xn1, xn2 = float(xnMatriz [0]), float(xnMatriz[1])
  
algoritmoNewton()
end = time.time()

print("")
print("El Algorítmo se demoró " + str(end - start) + " Segundos en correr")

"""Punto 2

Condiciones necesarias
"""

from sympy.plotting import plot3d

""" Parámetros
  Se definen los valores iniciales de los parámetros.
  eps: tolerancia, la escogemos nosotros.
"""

eps = 0.01 #tolerancia (nosotros escogemos)

""" Variables
  Se definen las siguientes como variables usando la librería sympy para operarlos.
  x, y: las variables de la función objetivo f(x, y)
  lam : el parámetro de penalización
"""

x = sym.Symbol('x')
y = sym.Symbol('y')
lam = sym.Symbol('lam') #lambda

""" Funciones
  Función que depende de las variables anteriores.
  f : función objetivo penalizada que depende de x y de y.
"""

f = 5 *(x**2) + 5 *(y**2) - x*y - 11*x + 11*y + 11

"""Métodos auxiliares
  calcularGradiente : calcula la gradiente (diferenciando).
  calcularInversaHessiana : calcula la matriz Hessiana con las derivadas correspondientes y la invierte.
  plot : nos grafica la función dada
"""

def calcularGradiente ():
  gradientex = sym.diff(f, x)
  gradientey = sym.diff(f, y)
  gradiente = gradientex, gradientey
  return gradiente

def calcularInversaHessiana ():
  dfx = sym.diff(f,x)
  dfy = sym.diff(f,y)
  dfxx = sym.diff(dfx,x)
  dfyy = sym.diff(dfy,y)
  dfxy = sym.diff(dfx,y)
  xx = int(dfxx.evalf())
  yy = int(dfyy.evalf())
  xy = int(dfxy.evalf())
  matrizHessiana = sym.Matrix([[xx, xy],[xy , yy]])
  inversa = matrizHessiana **-1
  return inversa

def plot(f):
  p = plot3d(f, show=False)
  p.show()
  print("")
  print("Según la forma de la función, es trivial que es convexa, se propone demostrarlo viendo que la matriz Hessiana inversa es semidefinida positiva.")

"""Método principal
  condicionesNecesarias : se verifican las condiciones necesarias de primer orden
  minimoGlobal : se verifica que el punto crítico sea un mínimo global.
"""
def condicionesNecesarias ():
  gradx, grady = calcularGradiente()
  puntoCritico = solve([gradx, grady], (x, y))
  print("El punto crítico que cumple las condiciones necesarias es "+ str(puntoCritico)+".")

def minimoGlobal ():
  plot(f)
  hessianaInversa = calcularInversaHessiana ()
  print("La matriz Hessiana inversa se muestra a continuación:")
  sym.pprint(hessianaInversa)
  autovalores = hessianaInversa.eigenvals()
  print("Los autovalores de la matriz Hessiana inversa son "+str(autovalores)+", y como todos son mayores o iguales a cero, sabemos que esta es semidefinida positiva y así la función es convexa.")

condicionesNecesarias()
minimoGlobal()
print("")

"""
Método de descenso con regla de Armijo


"""

from sympy.functions import transpose

""" Parámetros
  Se definen los valores iniciales de los parámetros.
  eps: tolerancia, la escogemos nosotros.
  xinicial, yinicial : son los puntos iniciales con los que empieza a iterar el algoritmo, en este caso se escogen arbitrariamente.

  Parámetros para la regla de Armijo
  tinicial : se escoge 1 porque es el recomendado en la literatura, pero para t<1 también converge rapidamente.
  gamma : se escoge 0.7 por la revisión literaria.
  eta : se escoge 0.45 por la revisión literaria.
"""

eps = 0.0001
xinicial = 1 
yinicial = 1 
tinicial = 1 
gamma = 0.7
eta = 0.45

""" Variables
  Se definen las siguientes como variables usando la librería sympy para operarlos.
  x, y: las variables de la función objetivo f(x, y)
  lam : el parámetro de penalización
"""

x = sym.Symbol('x')
y = sym.Symbol('y')
lam = sym.Symbol('lam') #lambda

""" Funciones
  Función que depende de las variables anteriores.
  f : función objetivo penalizada que depende de x y de y.
"""

f = 5 *(x**2) + 5 *(y**2) - x*y - 11*x + 11*y + 11
#f = 8 * (x**2) + 6 *(y ** 2) + (4 * (x - 1) * (y - 2))

"""Métodos auxiliares
  calcularGradiente : calcula la gradiente (diferenciando).
  normaGradiente : calcula la norma de un gradiente en dos puntos dados.
  calcularInversaHessiana : calcula la matriz Hessiana con las derivadas correspondientes y la invierte.
"""

def calcularGradiente ():
  gradientex = sym.diff(f, x)
  gradientey = sym.diff(f, y)
  return gradientex, gradientey

def normaGradiente(xn, yn):
  gradx, grady = calcularGradiente()
  gradxn = float(((gradx.subs(x, xn)).subs(y, yn)).evalf())
  gradyn = float(((grady.subs(x, xn)).subs(y, yn)).evalf())
  norma = math.sqrt((gradxn **2) + (gradyn **2))
  return norma

def calcularInversaHessiana ():
  dfx = sym.diff(f,x)
  dfy = sym.diff(f,y)
  dfxx = sym.diff(dfx,x)
  dfyy = sym.diff(dfy,y)
  dfxy = sym.diff(dfx,y)
  xx = int(dfxx.evalf())
  yy = int(dfyy.evalf())
  xy = int(dfxy.evalf())
  matrizHessiana = sym.Matrix([[xx, xy],[xy , yy]])
  inversa = matrizHessiana **-1
  return inversa

"""Métodos principales
  reglaDeArmijo : realiza iteraciones del algoritmo de Armijo hasta que converja
  algoritmoNewton : 
"""

def reglaDeArmijo (xn, yn):
  t = tinicial
  gradx, grady = calcularGradiente()
  gradxn = float(((gradx.subs(x, xn)).subs(y, yn)).evalf())
  gradyn = float(((grady.subs(x, xn)).subs(y, yn)).evalf())
  boolean = True
  while boolean:
    puntox = xinicial - t * gradxn
    puntoy = yinicial - t * gradyn
    gradienteTranspuesta = transpose(sym.Matrix([gradxn, gradyn]))
    gradiente = sym.Matrix([gradxn, gradyn])

    cond1 = (f.subs(x, puntox)).subs(y, puntoy)
    a = float((((gradienteTranspuesta * -1 * gradiente))[0]).evalf())

    cond2 = (f.subs(x, xn)).subs(y, yn) + eta * t * a
    if (cond1 <= cond2):
      t = t * gamma
    else:
      boolean = False
  return t

def algoritmoNewton(eps, xninicial, yninicial):
  xn = xninicial
  yn = yninicial
  norma = normaGradiente(xn, xn)
  inversaHessiana = calcularInversaHessiana()
  for i in range(10):
    minimo = (f.subs(x,xn)).subs(y,yn)
    norma = normaGradiente(xn, yn)
    if norma < eps:
      print("El método converge con mínimo de "+str(minimo) + " con epsilon o tolerancia de "+ str(eps)+" con los puntos ("+str(xn) + ", " + str(yn) + ").")
      break
    else:
      print ("La iteración "+ str(i+1)+ " usa los puntos ("+ str(xn) + ", " + str(yn)+ ") con un valor de "+ str(minimo)+ ".")
      norma = normaGradiente(xn, yn)
      gradx, grady = calcularGradiente()
      gradxn = float(((gradx.subs(x, xninicial)).subs(y, yninicial)).evalf())
      gradyn = float(((grady.subs(x, xninicial)).subs(y, yninicial)).evalf())
      t = reglaDeArmijo(xn, yn)
      gradiente = sym.Matrix([gradxn, gradyn])
      xnMatriz = sym.Matrix([xn,yn]) - t * inversaHessiana * gradiente
      xn, yn = float(xnMatriz [0]), float(xnMatriz[1])

algoritmoNewton(eps, xinicial, yinicial)

"""Punto 3

Quasi-Newton
Algoritmo Broyden–Fletcher–Goldfarb–Shanno (BFGS)
"""

import cmath

""" Parámetros
  Se definen los valores iniciales de los parámetros.
  eps: tolerancia, la escogemos nosotros
  miuinicial : parámetro de penalización inicial, varía con cada iteración de penalización interior.
  eta : factor de reducción de miu
  x1inicial, x2inicial, x3inicial : son los puntos iniciales con los que empieza a iterar el algoritmo
"""

eps = 0.0005
miuinicial = 0.1
eta = 0.1
x1inicial, x2inicial, x3inicial = 0.1, 0.1, 0.1

""" Variables
  Se definen las siguientes como variables usando la librería sympy para operarlos.
  x1, x2, x3 : las variables de la función objetivo f(x1, x2, x3)
  miu : el parámetro de penalización
  alpha : variable de linesearch
"""

x1 = sym.Symbol('x1',  nonnegative=True)
x2 = sym.Symbol('x2',  nonnegative=True)
x3 = sym.Symbol('x3',  nonnegative=True)
mu = sym.Symbol('mu',  nonnegative=True)
alpha = sym.Symbol('alpha')

""" Funciones
  Funciones que dependen de las variables anteriores.
  g1 : restricción de desigualdad con un nuevo término de penalización para evitar puntos infactibles.
  g2, g3, g4 : restricciones de no negatividad.
  f : función objetivo
  f1, f2 : casos de penalización de la función objetivo
"""

g2 = x1
g3 = x2
g4 = x3

f =  9 - 8*x1 - 6*x2 - 4*x3 +2*x1**2 + 2*x2**2 + x3**2 + 2*x1*x2 + 2*x1*x3 
f1 = 9 - 8*x1 - 6*x2 - 4*x3 +2*x1**2 + 2*x2**2 + x3**2 + 2*x1*x2 + 2*x1*x3 + mu*(sym.ln(x1+x2+2*x3 - 3) + sym.ln(g2) + sym.ln(g3) + sym.ln(g4))
f2 = 9 - 8*x1 - 6*x2 - 4*x3 +2*x1**2 + 2*x2**2 + x3**2 + 2*x1*x2 + 2*x1*x3 + mu*(sym.ln(eps) + sym.ln(g2) + sym.ln(g3) + sym.ln(g4))

"""Métodos auxiliares
  gradiente : calcula la gradiente (diferenciando), la evalua para el punto (x1n, x2n, x3n) y la retorna en términos de miu.
"""

def gradiente (xn1, xn2, xn3, func):
  gradientex1 = sym.diff(func,x1)
  gradientex2 = sym.diff(func,x2)
  gradientex3 = sym.diff(func,x3)
  auxx1 = gradientex1.subs(x1,xn1)
  auxx2 = gradientex2.subs(x1,xn1)
  auxx3 = gradientex3.subs(x1,xn1)
  grad1 = (auxx1.subs(x2,xn2)).subs(x3,xn3)
  grad2 = (auxx2.subs(x2,xn2)).subs(x3,xn3)
  grad3 = (auxx3.subs(x2,xn2)).subs(x3,xn3)
  return grad1, grad2, grad3

"""Métodos principales
  quasinewton
  penalizacioninterna
"""



def quasiNewton (xn1, xn2, xn3, f1, f2, muValor):
  b = sym.Matrix([[1,0,0],[0,1,0],[0,0,1]])
  hessianaInversa = sym.Matrix([[1,0,0],[0,1,0],[0,0,1]])
  identity = sym.Matrix([[1,0,0],[0,1,0],[0,0,1]])
  boolean = True
  cont = 0
  while boolean:
    cont += 1
    normaold = math.sqrt((xn1**2)+(xn2**2)+(xn3**2))
    if normaold< eps or cont == 1:
      boolean = False
    func = f2.subs(mu, muValor)
    grad1, grad2, grad3 = (gradiente(x1inicial,x2inicial,x3inicial,func))
    dir = hessianaInversa * -1 * sym.Matrix(gradiente(xn1,xn2, xn3,func))
    p1n, p2n, p3n = float((dir[0].subs(mu, muValor)).evalf()), float((dir[1]).subs(mu, muValor).evalf()), float((dir[2].subs(mu, muValor)).evalf())
    xLine1, xLine2, xLine3 = xn1 + alpha*p1n, xn2 + alpha*p2n,  xn3 + alpha*p3n
    fAlpha = ((((func.subs(x1,xLine1)).subs(x2,xLine2))).subs(x3, xLine3))
    dfAlpha = sym.diff(fAlpha, alpha)
    lineAlphaauxf2 = solve(dfAlpha, alpha)
    for i in lineAlphaauxf2:
      realVal, imagVal = i.as_real_imag()
      realVal = float(realVal)
      if realVal >0:
        lineAlpha = realVal
      else: 
        next
    gradAuxx1, gradAuxx2, gradAuxx3 = gradiente(xn1, xn2, xn3, func)
    x1new, x2new, x3new = xn1 + lineAlpha*p1n, xn2 + lineAlpha*p2n, xn3 + lineAlpha*p3n
    gradAux1, gradAux2, gradAux3 = gradiente(x1new, x2new, x3new, func)
    
    yk1, yk2 , yk3 = gradAux1 - gradAuxx1, gradAux2 -gradAuxx2, gradAux3 -gradAuxx3

    sx = sym.Matrix([lineAlpha*p1n, lineAlpha*p2n, lineAlpha*p3n])
    yx = sym.Matrix([yk1, yk2, yk3])
    
    try1 = float((yx.T * sx)[0])

    coef1 = identity - ((sx*yx.T)*try1)
    coef2 = b**-1
    coef3 = ((sx*yx.T)*try1)

    hessianaInversa = (coef1*coef2*coef1) + coef3
    
    xn1,xn2, xn3 = x1new, x2new, x3new


  return (xn1, xn2, xn3)


def penalizacionInterior (x1n, x2n, x3n):  
  miuValor = miuinicial
  
  boolean = True
  cont = 0
  while boolean:
    cont += 1
    normaxnmenos1 = math.sqrt(((x1n **2) + (x2n **2)) + (x3n **2))
    minimo = (((f.subs(x1,x1n)).subs(x2,x2n)).subs(x3,x3n)).subs(mu, miuValor)
    print("La iteración número "+ str(cont)+ " usa los puntos (x1, x2, x3) = ("+ str(x1n) + ", "+str(x2n) + ", "+str(x3n)+") con z = " + str(minimo)+".")
    x1n, x2n, x3n = quasiNewton(x1inicial,x2inicial, x3inicial, f1, f2, miuValor)
    normaxn = math.sqrt(((x1n **2) + (x2n **2)) + (x3n **2))
    if ((abs(normaxnmenos1-normaxn))< eps):
      print("El método converge con valor de "+ str(minimo)+ " con los puntos (x1, x2, x3) = ("+ str(x1n) + ", "+str(x2n) + ", "+str(x3n)+") con mu = "+ str(miuValor) +".")
      boolean = False
    miuValor = eta * miuValor
    if cont ==10:
      print("nada pai")
      boolean = False


penalizacionInterior(x1inicial, x2inicial, x3inicial)