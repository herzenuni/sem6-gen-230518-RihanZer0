import random
import pytest

#Задание №1
s=[]
def fibo(n):
    fib1, fib2 = 0, 1
    for i in range(n):
        fib1, fib2 = fib2, fib1 + fib2
        yield fib1

n = 5
print(list(fibo(n)))

def listik(n):
	return list(fibo(n))
	
	
def change():
	global n
	n=int(input("Введите желаемое количество чисел ряда Фибоначчи: "))
	listik(fibo(n))

l = fibo(n)
for i in range(n):
  print(next(l))

#Задание №2
def not_UUID():
  global s
  for i in range(99999):
    z=hex(random.getrandbits(4))+hex(random.getrandbits(4))+hex(random.getrandbits(4))+hex(random.getrandbits(4))+hex(random.getrandbits(4))+hex(random.getrandbits(4))+hex(random.getrandbits(4))+hex(random.getrandbits(4))
    z=z.replace('0x','').upper()
    if z not in s:
      s.append(z)
      yield z
    else:
      print('секундочку ')
      not_UUID()
    
y=not_UUID()

#Тесты
@pytest.mark.parametrize("x,expected", [
    (2,[1, 1]),
    (3,[1, 1, 2]),
    (4,[1, 1, 2, 3]),
    (5,[1, 1, 2, 3, 5])])
def test_fibo(x, expected):
    assert listik(x) == expected
