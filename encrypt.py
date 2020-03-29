import base64
import secrets
import string

def main():
    print_instructions()
    plaintext, num_keys = get_input()
    keys = generate_keys(plaintext, num_keys)
    print_output(keys)
    
def print_instructions():
    instrs = """
****************************************
This program allows you to encrypt a    
secret message.  To decrypt it, two keys
must be provided to decrypt.py.  You can
generate as many keys as you want.
****************************************
"""
    print(instrs)
    
def get_input():
    plaintext = ''
    while len(plaintext) == 0 or not is_printable_ascii_str(plaintext):
        plaintext = input("Enter the secret to encode (printable ASCII characters only): ")
        
    num_keys = -1
    while num_keys < 2:
        in_str = input("Enter the number of keys to generate (at least 2): ").strip()
        if not in_str.isnumeric():
            continue
        num_keys = int(in_str)
        
    return (plaintext, num_keys)
    
def generate_keys(plaintext, num_keys):
    secret_number = str_to_num(plaintext)        
    slope = get_rand_num(20)
    
    keys = []
    for i in range(num_keys):
        x_pos = i + 1
        key_val = secret_number + slope*x_pos
        keys.append(b64_encode_key(x_pos, key_val))
        
    return keys
    
def print_output(keys):
    print("\nResult:")
    for index, key in enumerate(keys, start = 1):
        print("Key #" + str(index) + ": " + key)
    
    footnote = """
Remember, any two of these keys can be used to decrypt your secret message.
However, this means you can hand out one key to each person and they won't
be able to decrypt your message without knowing someone else's key.    

These keys must be kept private by their owners.
"""
    print(footnote)
    
def str_to_num(string):
    secret_number = 0
    for char in string:
        ascii_val = ord(char)
        secret_number = (secret_number << 8) | ascii_val
      
    return secret_number
    
def get_rand_num(num_digits):
    num_str = ''.join(secrets.choice(string.digits) for i in range(num_digits))
    return int(num_str)
    
def b64_encode_key(x_pos, key_val):
    key = str(x_pos) + "," + str(key_val)
    input_bytes = key.encode()
    output_bytes =  base64.b64encode(input_bytes)
    return output_bytes.decode()
    
def is_printable_ascii_str(string):
    for char in string:
        ascii_val = ord(char)
        if ascii_val > 127 or ascii_val < 32:
            return False
    return True
    
main()
    