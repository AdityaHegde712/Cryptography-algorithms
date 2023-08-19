# RC4 algorithm

def initial_permutations(s, t):
    i = j = 0
    l = len(s)
    for i in range(0, l):
        j = (j + s[i] + t[i]) % l
        s[i], s[j] = s[j], s[i]
        print(f"\ns[i] = {s[i]}, t[i] = {t[i]} \ni={i}, j={j} : {s}\n")

def keystream_gen(s, pt):
    l = len(s)
    i = j = 0
    for i in range(len(pt)):
        i = (i + 1) % l
        j = (j + s[i]) % l
        s[i], s[j] = s[j], s[i]
        k = (s[i] + s[j]) % l
        print(s[k])

def encryption(pt, key):
    ct = []
    for i, j in zip(pt, key):
        ct.append(i ^ j)
    return ct

def decryption(ct, key):
    pt = []
    for i, j in zip(ct, key):
        pt.append(i ^ j)
    return pt

if __name__ == "__main__":
    s = list(map(int, input("Enter array s with a space between each: ").split()))
    k = list(map(int, input("Enter key with a space between each: ").split()))
    pt = list(map(int, input("Enter plain text with a space between each: ").split()))
    t = []

    for i in range(len(s)):
        t.append(k[i % len(k)])
    print(f"Generated t: {t}")

    initial_permutations(s, t)
    keystream_gen(s, pt)

    ct = encryption(pt, k)
    print(f"Encrypted text: {ct}")

    pt = decryption(ct, k)
    print(f"Decrypted text: {pt}")
