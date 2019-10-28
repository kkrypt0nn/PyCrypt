def encrypt(message : str, key : int):
    if (message == ''):
        print("[ERROR] The message cannot be empty")
        return
    elif (key > 26) or (key < 1):
        print("[ERROR] The key cannot be higher than 26 or less than 1")
        return
    else:
        encryptedMessage = ''
        for character in message:
            if (character.isalpha()):
                number = ord(character)
                number += key
                if character.isupper():
                    if number > ord('Z'):
                        number -= 26
                    elif number < ord('A'):
                        number += 26
                elif character.islower():
                    if number > ord('z'):
                        number -= 26
                    elif number < ord('a'):
                        number += 26
                encryptedMessage += chr(number)
            else:
                encryptedMessage += character
        return encryptedMessage