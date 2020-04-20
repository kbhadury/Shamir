import constants
import file_ops
import secret_ops
import user_input_manager as uim

def main():
    print_instructions()
    in_file, num_keys, out_file = get_input()
    secret_seed = secret_ops.get_rand_num(constants.NUM_SEED_DIGITS)
    file_ops.xor_file(in_file, secret_seed, out_file)
    keys = secret_ops.generate_keys(secret_seed, num_keys, constants.NUM_SLOPE_DIGITS)
    print_output(keys)
    
def print_instructions():
    print(constants.ENCRYPT_FILE_INSTRUCTIONS)
    
def get_input():
    in_file = uim.get_printable_ascii_string("Enter the name of the file to encrypt (i.e. input.txt): ")
    num_keys = uim.get_int_at_least(2, "Enter the number of keys to generate (at least 2): ")
    out_file = uim.get_printable_ascii_string("Enter a name for the file to save the results to (i.e. output.txt): ")
    return (in_file, num_keys, out_file)
    
def print_output(keys):
    print("\nSuccess!")
    for index, key in enumerate(keys, start = 1):
        print("Key #" + str(index) + ": " + key)
