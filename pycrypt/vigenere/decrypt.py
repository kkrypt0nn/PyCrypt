from pycrypt import Characters

def decrypt(message : str, key : str):
    """
    Decrypts a message in the vigenère cipher with a given key
    :param: message String - The message that should be decrypted
    :param: key String - The key that has to be used to decrypt the message
    :return: decryptedMessage String - Returns the decrypted message
    """
    if (message == ""):
        print("[ERROR] The message cannot be empty")
        return
    elif (key == ""):
        print("[ERROR] The key cannot be empty")
        return
    translated = []
    decryptedMessage = "";
    keyIndex = 0
    key = key.upper()
    for symbol in message:
        num = Characters.LETTERS.find(symbol.upper())
        if num != -1:
            num -= Characters.LETTERS.find(key[keyIndex])
            num %= len(Characters.LETTERS)
            if symbol.isupper():
                translated.append(Characters.LETTERS[num])
            elif symbol.islower():
                translated.append(Characters.LETTERS[num].lower())
            keyIndex += 1
            if keyIndex == len(key):
                keyIndex = 0
        else:
            translated.append(symbol)
    return decryptedMessage.join(translated)