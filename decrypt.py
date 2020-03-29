import base64
import re

def main():
    print_instructions()
    key_1, key_2 = get_input()
    message = get_message(key_1, key_2)
    print("Decrypted message: " + message)
    
def print_instructions():
    print("*" * 40)
    print("This program allows you to decrypt a")
    print("secret message.  You must have two")
    print("keys associated with the secret.")
    print("*" * 40)
    
def get_input():
    key_1 = input("Enter the first key: ").strip()
    while not is_base64(key_1):
        print("Error: key can only contain letters, numbers, +, /, and =")
        key_1 = input("Enter the first key: ").strip()
        
    key_2 = input("Enter the second key: ").strip()
    while not is_base64(key_2):
        print("Error: key can only contain letters, numbers, +, /, and =")
        key_2 = input("Enter the second key: ").strip()
        
    return (key_1, key_2)
    
def get_message(key_1, key_2):
    x_1, y_1 = b64_decode_key(key_1)
    x_2, y_2 = b64_decode_key(key_2)
    
    secret_num = solve_for_intercept(x_1, y_1, x_2, y_2)
    return num_to_str(secret_num)
    
def solve_for_intercept(x_1, y_1, x_2, y_2):
    slope = None
    try:
        slope = (y_2 - y_1) // (x_2 - x_1)
    except:
        error_and_quit()
        
    intercept = y_1 - slope*x_1
    return intercept
    
def num_to_str(num):
    string = ""
    while num != 0:
        ascii_val = num & 0xFF
        if not is_printable_ascii_val(ascii_val):
            error_and_quit()
            
        char = chr(ascii_val)
        string = char + string
        num = num >> 8
        
    return string

def b64_decode_key(b64_str):
    input_bytes = b64_str.encode()
    output_bytes = None
    try:
        output_bytes =  base64.b64decode(input_bytes)
        key = output_bytes.decode()
    except:
        error_and_quit()
    
    vals = key.split(',')
    if len(vals) != 2:
        error_and_quit()
        
    vals = [int(val) for val in vals]
    return (vals[0], vals[1])
    
def is_base64(string):
    pattern = "\A[a-zA-Z0-9+/=]+\Z"
    result = re.match(pattern, string)
    return (result is not None)
    
def is_printable_ascii_val(ascii_val):
    return (ascii_val <= 127 and ascii_val >= 32)
    
def error_and_quit():
    print("Error: message could not be decrypted.  Please double check that you entered the keys correctly.")
    exit()
    
main()