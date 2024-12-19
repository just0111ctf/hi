import string
UPPER_CASE_LIST = list(string.ascii_uppercase)
MENU_OPTIONS = "(1)Show results for all possible shift(s)\n(2)Exit"

def validate_input(input):
    if input == "" or not input.isupper():
        return False
    if any(char.isdigit() for char in input):
        return False    
    return True    

def input_cipher_text():
    input_text = input("Input the cipher text: ")
    validate_result = validate_input(input_text)
    while not validate_result:
        input_text = input("Input should consist of uppercase letters, space characters, punctuation marks only. Input the cipher text: ")
        validate_result = validate_input(input_text)
    return input_text

def count_frequencies(text):
    result_list = []
    for letter in UPPER_CASE_LIST:
        result_list.append(text.count(letter))
    return result_list

def get_shift(index):
    if index == 4:
        return 0
    elif index < 4:
        return 22 + index
    else:
        return index - 4

def find_possible_k(result_list):
    possible_k_list = []
    largest_frequency = max(result_list)
    for index, num in enumerate(result_list):
        if num == largest_frequency:
            possible_k_list.append(get_shift(index))
    return possible_k_list

def menu():
    print(MENU_OPTIONS)
    menu_input = (input("Input number choice: "))
    valid = False
    while not valid:
        if not (menu_input.isdigit()):
            menu_input = input("Input must be a digit. Re-enter number choice: ")
        elif not ((int(menu_input) == 2) or (int(menu_input) == 1)):
            menu_input = input("Input must be between 1-2. Re-enter number choice: ")
        else:
            valid = True
    return int(menu_input)

def decrytion(text, shift):
    plain_text = ""
    for c in text:
        if c in UPPER_CASE_LIST:
            index = UPPER_CASE_LIST.index(c)
            char = UPPER_CASE_LIST[index - shift]
        else:
            char = c
        plain_text += char
    return plain_text

def main():
    print("Welcome")
    cipher_text = input_cipher_text()
    count_result = count_frequencies(cipher_text)
    possible_k_list = find_possible_k(count_result)
    print(f'The possible shift(s) is/are: {(', '.join(str(n) for n in possible_k_list))}')
    choice = menu()
    if choice == 1: #continue
        print("Possible plain texts using possible shift(s)")
        for num in possible_k_list:
            print(f'Shift: {num}, the corresponding plain text is: {decrytion(cipher_text, num)}')
    print("Bye")

if __name__ == "__main__":
    main()