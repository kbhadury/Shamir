import char_ops
import constants
import user_input_manager as uim

import secrets
import string

def main():
    print_instructions()
    plaintext, num_keys = get_input()
    keys = generate_keys(plaintext, num_keys)
    print_output(keys)
    
def print_instructions():
    print(constants.ENCRYPTION_INSTRUCTIONS)
    
def get_input():
    plaintext = uim.get_printable_ascii_string("Enter the secret to encode (printable ASCII characters only): ")
    num_keys = uim.get_int_gt("Enter the number of keys to generate (at least 2): ", 2)
    return (plaintext, num_keys)
    
def generate_keys(plaintext, num_keys):
    secret_number = char_ops.str_to_num(plaintext)        
    slope = get_rand_num(constants.NUM_SLOPE_DIGITS)
    
    keys = []
    for i in range(num_keys):
        x_pos = i + 1
        key_val = secret_number + slope*x_pos
        key = str(x_pos) + ',' + str(key_val)
        keys.append(char_ops.base64_encode(key))
        
    return keys
    
def print_output(keys):
    print("\nResult:")
    for index, key in enumerate(keys, start = 1):
        print("Key #" + str(index) + ": " + key)
    
    print(constants.ENCRYPTION_FOOTNOTE)
    
def get_rand_num(num_digits):
    num_str = ''.join(secrets.choice(string.digits) for i in range(num_digits))
    return int(num_str)
    
main()
    