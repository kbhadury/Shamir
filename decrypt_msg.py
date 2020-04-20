import data_ops
import constants
import secret_ops
import user_input_manager as uim

def main():
    print_instructions()
    key_1, key_2 = get_input()
    message = get_message(key_1, key_2)
    print_output(message)
    
def print_instructions():
    print(constants.DECRYPT_MSG_INSTRUCTIONS)
    
def get_input():
    key_1 = uim.get_base64_input("Enter the first key: ")
    key_2 = uim.get_base64_input("Enter the second key: ")
    return (key_1, key_2)
    
def get_message(key_1, key_2):
    try:
        secret_num = secret_ops.get_secret_num(key_1, key_2)
        return data_ops.num_to_str(secret_num)
    except:
        error_and_quit()
        
def print_output(message):
    print("\nDecrypted message: " + message)
    
def error_and_quit():
    print(constants.DECRYPTION_ERROR_MESSAGE)
    exit()
