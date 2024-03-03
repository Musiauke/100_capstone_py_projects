alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number: "))


def encrypt(plain_text, shift_amount): 
    cipher_text = ''
    for letter in plain_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift_amount) % len(alphabet)
            cipher_text += alphabet[new_position]
        else:
            cipher_text += letter
    print(f"The encoded text is {cipher_text}")
    return cipher_text


def decrypt(cipher_text, shift_amount):
    decoded_text = ''
    for letter in cipher_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position - shift_amount) % len(alphabet)
            decoded_text += alphabet[new_position]
        else:
            decoded_text += letter
    
    print(f"that's decoded text: {decoded_text}")
    
if direction == "encode":
    encrypted_text = encrypt(plain_text=text, shift_amount=shift)  
    decryption = input("Would you like to decrypt? y or n: ").lower()
    if decryption == 'y':
        decrypt(cipher_text=encrypted_text, shift_amount=shift)  
elif direction == 'decode':
    decrypt(cipher_text=text, shift_amount=shift)

