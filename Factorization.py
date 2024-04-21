import math 
import time 
import random 
from rsa import rsa, factorize_n

def extended_gcd(a, b):
        x0, x1, y0, y1 = 1, 0, 0, 1
        while b: 
            q, a, b = a // b, b, a % b
            x0, x1 = x1, x0 - q * x1
            y0, y1 = y1, y0 - q * y1
        return a, x0, y0 

def modular_inverse(e,n): # Calculates the modular inverse of a number e modulor n by finding the GCD of e anc n then returning the modular inverse
      gcd,x0,y0 = extended_gcd(e,n)
      if gcd != 1:
            raise ValueError('Modular inverse does not exist')
      return x0 % n

# def factorize_n(n):
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             p = i
#             q = n // i
#             return p, q
#     return None, None

n = int(input("\nEnter the number to factorize: "))

e = int(input("Enter public key(e): "))

start_time= time.time()

p,q = factorize_n(n)

phi_n = (q-1) * (p-1)

gcd,x,y = extended_gcd(e,phi_n)

d = modular_inverse(e,phi_n)

print ("p=", p, "q= ", q)
print ("d= ", d)
exact_time = time.time() - start_time
exact_time *= 1000
print (f"Time taken: {exact_time:.10f} milliseconds\n ")