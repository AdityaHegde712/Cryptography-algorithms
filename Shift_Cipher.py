def encrypt(pt, k):
    global alphabet
    ct = ""
    for i in range(len(pt)):
        if pt[i] == " ":
            ct += " "
            continue
        ct += alphabet[(alphabet.index(pt[i]) + k) % 26]
    print(f"Encrypted text: {ct}\n\n")

def decrypt(ct, k):
    global alphabet
    pt = ""
    for i in range(len(ct)):
        if ct[i] == " ":
            pt += " "
            continue
        # pt += alphabet[(alphabet.index(ct[i]) - alphabet.index(k[i % len(k)])) % 26]
        pt += alphabet[(alphabet.index(ct[i]) - k) % 26]
    print(f"Decrypted text: {pt}\n\n")

if __name__ == "__main__":
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    while True:
        print("1. Encrypt\n2. Decrypt\n3. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            pt = input("Enter plain text: ").upper()
            k = int(input("Enter key: "))
            encrypt(pt, k)
        elif choice == 2:
            ct = input("Enter cipher text: ").upper()
            k = int(input("Enter key: "))
            decrypt(ct, k)
        elif choice == 3:
            break
        else:
            print("Invalid choice!")
