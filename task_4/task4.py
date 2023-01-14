from sys import argv

# Most repeated words in english language according to Espresso English
CHECK = ['the', 'of', 'and', 'a', 'to', 'in', 'is', 'you', 'that', 'it', 'he', 'was', 'for', 'on', 'are', 'as', 'with', 'his', 'they', 'at', 'by', 'am', 'be', 'or', 'my', 'us', 'not', 'have', 'this', 'from']

def decrypt_msg(encoded_msg: str, shift_key: int) -> str:
    """Decrypts a message encoded with the Caesar Cipher using a given shift key."""
    decoded_msg = ''
    for char in encoded_msg:
        # Characters other than alphabets are kept same
        if not char.isalpha():
            decoded_msg += char
            continue

        # Checks if the character is in upper case or lower case
        is_capital = char.isupper()
        char_index = ord(char.lower())
        decrypt_char_index = char_index + shift_key

        # If character index is greater ascii value of 'z' then it is subtrected by 26
        if decrypt_char_index > ord('z'):
            decrypt_char_index -= 26
        decoded_msg += chr(decrypt_char_index).upper() if is_capital else chr(decrypt_char_index)
    
    return decoded_msg


def shift_key_finder(msg:str) -> int:
    '''Returns the shift key used to encode the message using the Caesar Cipher.'''
    for shift_key in range(1,27):
        decoded_msg = decrypt_msg(msg, shift_key)
        count = 0
        flag = False
        
        # If there is any words from 'CHECK' then count is increase by 1 and if count greater than 2, the shift key is returned
        for word in decoded_msg.split():
            if word in CHECK:
                count += 1
            if count > 2:
                return shift_key
    return None

if __name__ == "__main__":
    try:
        file_name = argv[1]
        with open(file_name) as fp:
            encrypt = fp.read()

        key = shift_key_finder(encrypt)
        if key == None:
            print("Cannot decrypt. Most likely not a Caesar Cypher at work here.")

        else:
            print(decrypt_msg(encrypt, key))

    except FileNotFoundError:
        print(f"Cannot open '{file_name}'. Sorry about that.")

    except IndexError:
        print("Error: Missing command-line argument.")