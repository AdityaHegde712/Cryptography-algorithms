# Affine cipher encryption
def encrypt(pt, a, b):
    ct = ''
    for i in pt:
        if i == ' ':
            ct += i
            continue
        ct += alphabet[(a * alphabet.index(i) + b) % 26]
    print(f"Encrypted text: {ct}\n\n")
    

# Affine cipher decryption
def decrypt(ct, a_inv, b):
    pt = ''
    for i in ct:
        if i == ' ':
            pt += ' '
            continue
        pt += alphabet[(a_inv * (alphabet.index(i) - b)) % 26]
    print(f"Decrypted text: {pt}\n\n")
    

# Finding the inverse of a given index a for keyspace 26
def find_inverse(a):
    for i in range(1, 26):
        if (a * i) % 26 == 1:
            return i
    return -1

if __name__ == "__main__":
    alphabet = sorted(list('QWERTYUIOPASDFGHJKLZXCVBNM'))
    inverse_keys = {alphabet.index(i):find_inverse(alphabet.index(i)) for i in alphabet if find_inverse(alphabet.index(i)) != -1}

    while True:
        print("1. Encrypt\n2. Decrypt\n3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            pt = input("Enter plain text: ").upper()
            a = int(input("Enter key a: "))
            b = int(input("Enter key b: "))
            encrypt(pt, a, b)

        elif choice == 2:
            ct = input("Enter cipher text: ").upper()
            a = int(input("Enter key a: "))

            if a in inverse_keys.keys():
                a = inverse_keys[a]
            else:
                print("Invalid key entered.")
                continue

            b = int(input("Enter key b: "))
            decrypt(ct, a, b)

        elif choice == 3:
            break

        else:
            print("Invalid choice!")
            
    