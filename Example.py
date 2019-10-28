import pycrypt

# Prints information about the library
print(pycrypt.__name__ + ", Version " + pycrypt.__version__ + ", " + pycrypt.__copyright__)
print("Made by " + pycrypt.__author__ + "\n\n")

# Encrypts a message with the caesar cipher and the key 12
print("Encrypted Message:")
print(pycrypt.caesar.encrypt("Test", 12))

# Decrypts a message with the caesar cipher and the key 12
print("Decrypted Message:")
print(pycrypt.caesar.decrypt("Fqef", 12))