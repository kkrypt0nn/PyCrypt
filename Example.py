import pycrypt

# Prints information about the library
print(pycrypt.__name__ + ", Version " + pycrypt.__version__ + ", " + pycrypt.__copyright__)
print("Made by " + pycrypt.__author__ + "\n\n")

# Encrypts a message with the caesar cipher and the key 12
print("Encrypted Caesar Message:")
print(pycrypt.caesar.encrypt("Test", 12))

# Decrypts a message with the caesar cipher and the key 12
print("Decrypted Caesar Message:")
print(pycrypt.caesar.decrypt("Fqef", 12) + "\n")

# Encrypts a message with the vigenère cipher and the key `TheKey`
print("Encrypted Vigenère Message:")
print(pycrypt.vigenere.encrypt("Test", "TheKey"))

# Decrypts a message with the vigenère cipher and the key `TheKey`
print("Decrypted Vigenère Message:")
print(pycrypt.vigenere.decrypt("Mlwd", "TheKey"))