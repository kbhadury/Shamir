import constants
import encrypt_msg
import decrypt_msg
import encrypt_file
import decrypt_file
import user_input_manager as uim

OPTIONS = [
"Exit",
"Encrypt a message",
"Decrypt a message",
"Encrypt a file",
"Decrypt a file",
"Encrypt a file using existing keys"
]

def main():
    print_menu()
    user_choice = get_choice()
    
    if user_choice == 0:
        exit()
    elif user_choice == 1:
        encrypt_msg.main()
    elif user_choice == 2:
        decrypt_msg.main()
    elif user_choice == 3:
        encrypt_file.main()
    elif user_choice == 4:
        decrypt_file.main()
    elif user_choice == 5:
        decrypt_file.main(True)
    else:
        exit()

def print_menu():
    print(constants.MAIN_MENU_HEADER)
    print(uim.get_menu_str(OPTIONS, 40))
    print(constants.MAIN_MENU_FOOTER)
    
def get_choice():
    return uim.get_int_choice_from(range(len(OPTIONS)), "Your choice: ")
    
main()
