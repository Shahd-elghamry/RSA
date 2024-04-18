import random
import math

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

def rsa_encryption_decryption():
    p = generate_prime(8)
    q = generate_prime(8)
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

    while True:
        gcd, x, y = extended_gcd(e, eul)
        if gcd == 1:
            break
        else:
            e += 1

    d = x % eul
    print(f"Public key: {e}")
    print(f"n = {n}")
    print(f"Private key: {d}")

    m = 12
    C = pow(m, e, n)
    M = pow(C, d, n)
    print("Encrypted:", C)
    print("Decrypted:", M)

    return n

def factorize_n(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            p = i
            q = n // i
            return p, q
    return None, None


# Call the encryption/decryption function
n = rsa_encryption_decryption()

# Factorize n and calculate p and q
p, q = factorize_n(n)
print(f"Factorized n: p = {p}, q = {q}")