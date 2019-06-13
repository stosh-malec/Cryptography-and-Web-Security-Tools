def rotation_cipher():
    letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    encrypt = raw_input('Enter a string to Encrypt')
    move = input('Enter a number for the rotation key')
    move = int(move)
    for x in encrypt:
        encypted = letters.index(x) + move
        encrypt = encrypt.replace(letters[encrypted])
    return encrypt

def rotation_cipher_decryptor():
    letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    dencrypt = raw_input('Enter a string to Decrypt')
    move = 7
    for x in encrypt:
        encypted = letters.index(x) - move
        dencrypt = dencrypt.replace(letters[encrypted])
    return dencrypt
    
print("What would you like to do")
answer = input('Type: 1 to encrypt || 2 to decrypt')
if (answer == 1):
    rotation_cipher()
elif (answer == 2):
    rotation_cipher_decryptor()
else:
    print('that wasn\'t a option')
    break


#To contribute add input validation, a better UI/UX, or add other encryption methods
