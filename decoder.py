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
    key_1 = input("Enter the first key: ")
    while not is_base64(key_1):
        print("Error: key can only contain letters, numbers, +, /, and =")
        key_1 = input("Enter the first key: ")
        
    key_2 = input("Enter the second key: ")
    while not is_base64(key_2):
        print("Error: key can only contain letters, numbers, +, /, and =")
        key_2 = input("Enter the second key: ")
        
    return (key_1, key_2)
    
def get_message(key_1, key_2):
    x_1, y_1 = b64_decode_coords(key_1)
    x_2, y_2 = b64_decode_coords(key_2)
    
    slope = (y_2 - y_1) // (x_2 - x_1)
    secret_num = -1*slope*x_1 + y_1
    
    return num_to_str(secret_num)
    
def num_to_str(num):
    string = ""
    while num != 0:
        ascii_val = num & 0xFF
        print(ascii_val)
        char = chr(ascii_val)
        string = char + string
        num = num >> 8
        
    return string

def b64_decode_coords(b64_str):
    input_bytes = b64_str.encode()
    output_bytes = ''
    try:
        output_bytes =  base64.b64decode(input_bytes)
    except:
        print("The key '" + b64_str + "' is malformed.  Please double check that you typed it correctly.")
        exit()
        
    coords_str = output_bytes.decode()
    coords_strs = coords_str.split(',')
    coords = [int(coord_str) for coord_str in coords_strs]
    return (coords[0], coords[1])
    
def is_base64(string):
    pattern = "\A[a-zA-Z0-9+/]+\Z"
    result = re.match(pattern, string)
    return (result is not None)
    
main()