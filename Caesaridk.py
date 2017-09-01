key = int(input("Please input a key: "))
msg = input("Please input a message to encrypt: ")
count = 0
a = [ord(c) for c in msg]
for b in a: #a times
    print(chr((a[count] + key - 65) % 26 + 65))
    count = count + 1
        



key = int(input("Please input a key: "))
msg = input("Please input a message to decrypt: ")
count = 0
a = [ord(c) for c in msg]
for b in a: #a times
    print(chr((a[count] - key - 65) % 26 + 65))
    count = count + 1
