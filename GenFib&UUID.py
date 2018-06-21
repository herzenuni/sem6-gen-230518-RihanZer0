import random

s=[]
def fibo(n):
    fib1, fib2 = 0, 1
    for i in range(n):
        fib1, fib2 = fib2, fib1 + fib2
        yield fib1

n = int(input("Введите желаемое количество чисел ряда Фибоначчи: "))
l = fibo(n)

print(list(fibo(n)))

for i in range(n):
  print(next(l))

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