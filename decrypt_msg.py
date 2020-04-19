import char_ops
import constants
import user_input_manager as uim

def main():
    print_instructions()
    key_1, key_2 = get_input()
    message = get_message(key_1, key_2)
    print_output(message)
    
def print_instructions():
    print(constants.DECRYPTION_INSTRUCTIONS)
    
def get_input():
    key_1 = uim.get_base64_input("Enter the first key: ")
    key_2 = uim.get_base64_input("Enter the second key: ")
    return (key_1, key_2)
    
def get_message(key_1, key_2):
    key_1_coords = None
    key_2_coords = None
    try:
        key_1_coords = char_ops.base64_decode(key_1)
        key_2_coords = char_ops.base64_decode(key_2)
    except:
        error_and_quit("Please double check that you entered the keys correctly.")
    
    x_1, y_1 = extract_x_y(key_1_coords)
    x_2, y_2 = extract_x_y(key_2_coords)
    
    secret_num = solve_for_intercept(x_1, y_1, x_2, y_2)
    try:
        return char_ops.num_to_str(secret_num)
    except:
        error_and_quit("Please double check that you entered the keys correctly.")
        
def print_output(message):
    print("\nDecrypted message: " + message)
    
def solve_for_intercept(x_1, y_1, x_2, y_2):
    slope = None
    try:
        slope = (y_2 - y_1) // (x_2 - x_1)
    except:
        error_and_quit("Did you enter the same key twice?")
        
    intercept = y_1 - slope*x_1
    return intercept
    
def extract_x_y(coord_pair):
    coords = coord_pair.split(',')
    if len(coords) != 2:
        error_and_quit("Please double check that you entered the keys correctly.")
    return (int(coords[0]), int(coords[1]))
    
def error_and_quit(extra_msg = None):
    print(constants.DECRYPTION_ERROR_MESSAGE)
    if extra_msg is not None:
        print(extra_msg)
    exit()
