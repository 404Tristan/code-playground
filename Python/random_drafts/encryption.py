def encryption(plain_text):
    return "".join((chr(ord(letter) + 1) for letter in plain_text))

def decryption(plain_text):
    return "".join(chr(ord(letter) - 1) for letter in plain_text)


text =  "Ikaw na ba si Mr. Right?" #input("Enter a text: ")
encrypted = encryption(text)
decrypted = decryption(encrypted)

print()
print(f"Original message: {text}")       # output: Ikaw na ba si Mr. Right?
print(f"Encrypted message: {encrypted}") # Jlbx!ob!cb!tj!Ns/!Sjhiu@
print(f"Decrypted message: {decrypted}") # output: Ikaw na ba si Mr. Right?
