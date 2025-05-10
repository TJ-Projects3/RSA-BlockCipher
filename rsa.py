# RSA Signature Scheme
# Referred to some GeeksforGeeks code to better understand RSA in code.

def power(base, expo, m):
    res = 1
    base = base % m
    while expo > 0:
        if expo & 1:
            res = (res * base) % m
        base = (base * base) % m
        expo = expo // 2
    return res

def modInverse(e, phi):
    for d in range(2, phi):
        if (e * d) % phi == 1:
            return d
    return -1

def generateKeys():
    p = 7919
    q = 1009
    n = p * q
    phi = (p - 1) * (q - 1)
    for e in range(2, phi):
        if gcd(e, phi) == 1:
            break
    d = modInverse(e, phi)
    return e, d, n

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Sign the message using private key (d, n)
def sign(message, d, n):
    return power(message, d, n)

# Verify the signature using public key (e, n)
def verify(signature, e, n, original_message):
    return power(signature, e, n) == original_message

if __name__ == "__main__":
    # Given example info (public key)
    n = 9797
    e = 131

    # Test cases in list
    test_cases = [
        (123, 6292),  # (x = 123, sig(x) = 6292)
        (4333, 4768), # (x = 4333, sig(x) = 4768)
        (4333, 1424)  # (x = 4333, sig(x) = 1424)
    ]

    # For each x and signature of x, run the verifier and log
    for x, sig in test_cases:
        is_valid = verify(sig, e, n, x)
        print(f"Message: {x}, Signature: {sig}, Valid: {is_valid}")