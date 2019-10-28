def decrypt(message : str, key : int):
    """
    Decrypts a message in the caesar cipher with a given key
    :param: message String - The message that should be decrypted
    :param: key Integer - The key that has to be used to decrypted the message
    :return: decryptedMessage String - Returns the decrypted message
    """
    if (message == ''):
        print("[ERROR] The message cannot be empty")
        return
    elif (key > 26 ) or (key < 1):
        print("[ERROR] The key cannot be higher than 26 or less than 1")
        return
    else:
        decryptedMessage = ''
        key = -key
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
                decryptedMessage += chr(number)
            else:
                decryptedMessage += character
        return decryptedMessage