import data_ops
import constants
import secret_ops
import user_input_manager as uim

def main():
    print_instructions()
    plaintext, num_keys = get_input()
    keys = generate_keys(plaintext, num_keys)
    print_output(keys)
    
def print_instructions():
    print(constants.ENCRYPT_MSG_INSTRUCTIONS)
    
def get_input():
    plaintext = uim.get_printable_ascii_string("Enter the secret to encode (printable ASCII characters only): ")
    num_keys = uim.get_int_at_least(2, "Enter the number of keys to generate (at least 2): ")
    return (plaintext, num_keys)
    
def generate_keys(plaintext, num_keys):
    secret_num = data_ops.str_to_num(plaintext) 
    return secret_ops.generate_keys(secret_num, num_keys, constants.NUM_SLOPE_DIGITS)
    
def print_output(keys):
    print("\nSuccess!")
    for index, key in enumerate(keys, start = 1):
        print("Key #" + str(index) + ": " + key)
    
    print(constants.ENCRYPTION_FOOTNOTE)
