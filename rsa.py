import random
import math

bits_input = int(input( "\nHow many number of bits do you want (8/16)?: "))
#First line is to ask the user for input whether he wants 8 or 16 bits
m = int(input("Enter message: ")) 
#Second line is to ask the user to enter the message he wants to encrypt

# The next function to generate a random prime number
def is_prime(n):
    if n < 2: # anything less than 2 is not prime
        return False
    for i in range(2, int(n**0.5) + 1): 
        if n % i == 0: # if n is divisible by any number between 2 and n^0.5, it is not prime
            return False
    return True

def generate_prime(bits): # generate a random prime number with the given number of bits
    while True: # keep generating random numbers until a prime is found
        num = random.getrandbits(bits)
        if num % 2 == 0: 
            num += 1
        if is_prime(num): 
            return num
        
def rsa(): 
    if bits_input == 8: # If the bits inputed is 8 it does the following 
        p = generate_prime(8)
        q = generate_prime(8)
    elif bits_input == 16: 
        p = generate_prime(16)
        q = generate_prime(16)
    else: 
        print("Wrong number of bits ")
        exit()
    n = p * q 
    eul = (p - 1) * (q - 1) 
    e = random.randint(2, eul - 1) 

    def extended_gcd(a, b):
        x0, x1, y0, y1 = 1, 0, 0, 1
        while b: 
            q, a, b = a // b, b, a % b
            x0, x1 = x1, x0 - q * x1
            y0, y1 = y1, y0 - q * y1
        return a, x0, y0

    while True: # This loop runs until it finds a value where the gcd of e and eul is equal to 1
        gcd, x, y = extended_gcd(e, eul)
        if gcd == 1:
            break
        else:
            e += 1

    d = x % eul # To generate the private key 
    print(f"\nPublic key(n,e): {n,e}")
    print(f"n = {n}")
    print(f"Private key(n,d): {n,d}")

    C = pow(m, e, n)
    M = pow(C, d, n)
    print("\nEncrypted:", C)
    print("Decrypted:", M)

    return n

def factorize_n(n): # This function finds the factorization of n which are p and q
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            p = i
            q = n // i
            return p, q
    return None, None

# Call the encryption/decryption function
n = rsa()

# Factorize n and calculate p and q
p, q = factorize_n(n)
print(f"Factorized n: p = {p}, q = {q}\n")