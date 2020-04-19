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
"Modify an encrypted file"
]

def main():
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
        pass
    else:
        exit()
    
def get_choice():
    print(constants.MAIN_MENU_HEADER)
    print(uim.get_menu_str(OPTIONS, 40))
    print(constants.MAIN_MENU_FOOTER)
    return uim.get_int_choice_from(range(len(OPTIONS)), "Your choice: ")
    
main()