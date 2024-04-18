import random 
import math 
import time
# from rsa import C
# from rsa import M

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_prime(bits):
    while True:
        num = random.getrandbits(bits)
        if num % 2 == 0:
            num += 1
        if is_prime(num): 
            return num
        
n = int(input("Enter the number to factorize: "))
e = int(input("Enter public key(e): "))

start_time = time.time()

p, q = 0, 0
while p * q != n:
    p = generate_prime(n)
    q = n // p

phi_n = (q - 1) * (p - 1)

def find_priv(e, phi_n):
    for d in range(2, phi_n):
        if (e * d) % phi_n == 1: 
            return d
        
d = find_priv(e, phi_n)
print("Private key (d): ", d)

exact_time = time.time() - start_time 
exact_time *= 1000
print(f"Time taken: {exact_time:.15f} milli-seconds")
