import char_ops

def get_printable_ascii_string(msg):
    user_input = ''
    while len(user_input) == 0 or not user_input.isprintable():
        user_input = input(msg)
        
    return user_input
    
def get_int_gt(msg, min_val):
    user_input = min_val - 1
    while user_input < min_val:
        in_str = input(msg).strip()
        if not in_str.isnumeric():
            continue
        user_input = int(in_str)
        
    return user_input
    
def get_base64_input(msg):
    user_input = input(msg).strip()
    while not char_ops.is_base64(user_input):
        print("Error: input can only contain letters, numbers, +, /, and =")
        user_input = input(msg).strip()
        
    return user_input
    