
import random 
import math 
import time
from rsa import is_prime, generate_prime # I take those functions from another file 

# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# def generate_prime(bits):
#     while True:
#         num = random.getrandbits(bits)
#         if num % 2 == 0:
#             num += 1
#         if is_prime(num): 
#             return num


n = int(input("\nEnter the n: "))
e = int(input("Enter public key(e): "))
encrypted = int(input("Enter encrypted: "))
message = int(input("Enter decrypted: "))
# bits = int(input("Number of bits 8/16: "))
p = int(input("Enter p: "))
q = int(input("Enter q: "))
start_time = time.time()



# p, q = 0, 0
# while p * q != n:
#     if bits==8:
#         p = generate_prime(8)  # Adjust the number of bits as needed
#     elif bits==16:
#         p = generate_prime(16) 
#     else:
#         exit() 
#     q = n // p
phi_n = (q - 1) * (p - 1) # Euler totient formula

def find_bruteforce(e, phi_n, encrypted, message): # This function fins the d
    attempts = 0
    for d in range(2, phi_n):
        attempts +=1
        if (e * d) % phi_n == 1: 
            decrypted = pow(encrypted, d, n)
            if decrypted == message:
                print(f"\nAttempts made: {attempts}")
                return d
    return None

bruteforce = find_bruteforce(e, phi_n, encrypted, message) # Just adding the function into a variable 
print("\nPrivate key (d): ", bruteforce)

exact_time = time.time() - start_time # Finding the time taken
exact_time *= 1000 # Converting tbe seconds taken into milliseconds
print(f"Time taken in bruteforce was: {exact_time:.15f} milli-seconds\n")
