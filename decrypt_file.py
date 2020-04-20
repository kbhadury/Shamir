import constants
import file_ops
import secret_ops
import user_input_manager as uim

reencrypt = False

def main(renc = False):
    global reencrypt
    reencrypt = renc
    print_instructions()
    key_1, key_2 = get_key_input()
    secret_seed = get_seed(key_1, key_2)
    in_file, out_file = get_file_input()
    file_ops.xor_file(in_file, secret_seed, out_file)
    print_output(out_file)
    
def print_instructions():
    if reencrypt == True:
        print(constants.REENCRYPT_FILE_INSTRUCTIONS)
    else:
        print(constants.DECRYPT_FILE_INSTRUCTIONS)
    
def get_key_input():        
    key_1 = uim.get_base64_input("Enter the first key: ")
    key_2 = uim.get_base64_input("Enter the second key: ")
    return (key_1, key_2)
    
def get_seed(key_1, key_2):
    try:
        return secret_ops.get_secret_num(key_1, key_2)
    except:
        error_and_quit()
    
def get_file_input():
    action = "decrypt"
    if reencrypt == True:
        action = "encrypt"
    in_file = uim.get_printable_ascii_string("Enter the name of the file to " + action + " (i.e. input.txt): ")
    out_file = uim.get_printable_ascii_string("Enter a name for the file to save the results to (i.e. output.txt): ")
    return (in_file, out_file)
    
def print_output(out_file):
    print("Success!  Saved to " + out_file)
    
def error_and_quit():
    print(constants.DECRYPTION_ERROR_MESSAGE)
    exit()
