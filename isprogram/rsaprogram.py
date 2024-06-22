import math

print("RSA ENCRYPTOR/DECRYPTOR")
print("*****************************************************")

# Input Prime Numbers
p = int(input("Enter a prime number for p: "))
q = int(input("Enter a prime number for q: "))
print("*****************************************************")

def prime_check(a):
    if a <= 1:
        return False
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
    return True

while not (prime_check(p) and prime_check(q)):
    print("Both numbers must be prime. Please enter again.")
    p = int(input("Enter a prime number for p: "))
    q = int(input("Enter a prime number for q: "))

# RSA Modulus and Euler's Totient
n = p * q
r = (p - 1) * (q - 1)
print(f"RSA Modulus(n) is: {n}")
print(f"Euler's Totient(r) is: {r}")
print("*****************************************************")

def egcd(e, r):
    while r != 0:
        e, r = r, e % r
    return e

def eea(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = eea(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

def mult_inv(e, r):
    gcd, x, _ = eea(e, r)
    return x % r if gcd == 1 else None

e = next(i for i in range(2, r) if egcd(i, r) == 1)
print(f"The value of e is: {e}")
print("*****************************************************")

d = mult_inv(e, r)
print(f"The value of d is: {d}")
print("*****************************************************")

public = (e, n)
private = (d, n)
print(f"Private Key is: {private}")
print(f"Public Key is: {public}")
print("*****************************************************")

def encrypt(pub_key, n_text):
    e, n = pub_key
    return [(ord(char) - 65 if char.isupper() else ord(char) - 97 if char.islower() else 26) ** e % n for char in n_text]

def decrypt(priv_key, c_text):
    d, n = priv_key
    return ''.join(chr((c ** d % n) + 65) if c != 26 else ' ' for c in c_text)

while True:
    message = input("What would you like encrypted or decrypted? (Separate numbers with ',' for decryption, 'exit' to quit): ")
    if message.lower() == 'exit':
        break
    
    print(f"Your message is: {message}")
    choose = input("Type '1' for encryption and '2' for decryption: ")
    
    if choose == '1':
        encrypted_msg = encrypt(public, message)
        print(f"Your encrypted message is: {encrypted_msg}")
    elif choose == '2':
        cipher_text = list(map(int, message.split(',')))
        decrypted_msg = decrypt(private, cipher_text)
        print(f"Your decrypted message is: {decrypted_msg}")
    else:
        print("Invalid choice. Please choose '1', '2', or 'exit'.")
    
    print("*****************************************************")

print("Exiting RSA Encryptor/Decryptor.")
