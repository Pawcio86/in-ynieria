# in-ynieria
import math
print ("To jest algorytm wyliczania pierwiastków równania kwadratowego w postaci ax^2 + bx + c = 0")
def pierwiastek1 (a,b,delta):
  return -b-math.sqrt(delta)/(2*a)
def pierwiastek2 (a,b,delta):
  return -b+math.sqrt(delta)/(2*a)
def pierwiastek0 (a,b):
  return -b/2*a
a = float(input("Podaj wartość parametru a: "))
b = float(input("Podaj wartość parametru b: "))
c = float(input("Podaj wartość parametru c: "))
if a == 0:
  print ("To nie jest równanie kwadratowe")
else:
  delta = b*b-4*a*c
  print ("Delta wynosi ", delta)
if delta > 0:
  print ("Równanie posiada dwa pierwiastki, które wynosza:")
  print ("Pierwiastek x1 =", pierwiastek1())
  print ("Pierwiastek x2 =", pierwiastek2())
elif delta == 0:
  print ("Równanie posiada jeden pierwiastek, który wynosi:")
  print ("Pierwiastek x0 =", pierwiastek0)
else:
  print ("Równanie nie ma żadnych pierwiastków")
