import numpy as np

def generate_key_matrix(key):
    key = key.upper().replace('J', 'I')  # Convert to uppercase and replace 'J' with 'I'
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key_matrix = []

    for char in key:
        if char not in key_matrix:
            key_matrix.append(char)

    for char in alphabet:
        if char not in key_matrix:
            key_matrix.append(char)

    key_matrix = np.array(key_matrix).reshape(5, 5)
    return key_matrix

def find_char_positions(matrix, char):
    positions = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == char:
                positions.append((i, j))
                # print(positions)
    return positions

def playfair_encrypt(plaintext, key_matrix):
    plaintext = plaintext.upper().replace('J', 'I')
    plaintext_pairs = []
    ciphertext = ""

    for i in range(0, len(plaintext), 2):
        if i == len(plaintext) - 1:  # If the last pair has only one character, add 'X' at the end
            plaintext_pairs.append((plaintext[i], 'X'))
        elif plaintext[i] == plaintext[i + 1]:  # If two consecutive characters are the same, add 'X' in between
            plaintext_pairs.append((plaintext[i], 'X'))
            plaintext = plaintext[:i + 1] + 'X' + plaintext[i + 1:]
        else:
            plaintext_pairs.append((plaintext[i], plaintext[i + 1]))
   
    print("Plain text pairs: " )
    print(plaintext_pairs)

    for pair in plaintext_pairs:
        char1, char2 = pair
        pos1 = find_char_positions(key_matrix, char1)
        print(char1)
        print(pos1)
        pos2 = find_char_positions(key_matrix, char2)
        print(char2)
        print(pos2)


        if pos1[0][0] == pos2[0][0]:  # If both letters are in the same row
            new_pos1 = (pos1[0][0], (pos1[0][1] + 1) % 5)
            print(f"new same row {new_pos1}")
            new_pos2 = (pos2[0][0], (pos2[0][1] + 1) % 5)
            print(f"new same row {new_pos2}")
        elif pos1[0][1] == pos2[0][1]:  # If both letters are in the same column
            new_pos1 = ((pos1[0][0] + 1) % 5, pos1[0][1])
            print(f"new same column {new_pos1}")
            new_pos2 = ((pos2[0][0] + 1) % 5, pos2[0][1])
            print(f"new same column {new_pos2}")

        else:  # If the letters form a rectangle
            new_pos1 = (pos1[0][0], pos2[0][1])
            print(f"new same rectangle {new_pos1}")
            new_pos2 = (pos2[0][0], pos1[0][1])
            print(f"new same rectangle {new_pos2}")

        ciphertext += key_matrix[new_pos1[0]][new_pos1[1]] + key_matrix[new_pos2[0]][new_pos2[1]]

    return ciphertext



def playfair_decrypt(ciphertext, key_matrix):
    ciphertext = ciphertext.upper().replace('J', 'I')
    ciphertext_pairs = []
    plaintext = ""

    for i in range(0, len(ciphertext), 2):
        if i == len(ciphertext) - 1:  # If the last pair has only one character, add 'X' at the end
            ciphertext_pairs.append((ciphertext[i], 'X'))
        elif ciphertext[i] == ciphertext[i + 1]:  # If two consecutive characters are the same, add 'X' in between
            ciphertext_pairs.append((ciphertext[i], 'X'))
            ciphertext = ciphertext[:i + 1] + 'X' + ciphertext[i + 1:]
        else:
            ciphertext_pairs.append((ciphertext[i], ciphertext[i + 1]))
   
    print("Cipher text pairs: " )
    print(ciphertext_pairs)
    

    for pair in ciphertext_pairs:
        char1, char2 = pair
        pos1 = find_char_positions(key_matrix, char1)
        pos2 = find_char_positions(key_matrix, char2)

        if pos1[0][0] == pos2[0][0]:  # If both letters are in the same row
            new_pos1 = (pos1[0][0], (pos1[0][1] - 1) % 5)
            new_pos2 = (pos2[0][0], (pos2[0][1] - 1) % 5)
        elif pos1[0][1] == pos2[0][1]:  # If both letters are in the same column
            new_pos1 = ((pos1[0][0] - 1) % 5, pos1[0][1])
            new_pos2 = ((pos2[0][0] - 1) % 5, pos2[0][1])
        else:  # If the letters form a rectangle
            new_pos1 = (pos1[0][0], pos2[0][1])
            new_pos2 = (pos2[0][0], pos1[0][1])

        plaintext += key_matrix[new_pos1[0]][new_pos1[1]] + key_matrix[new_pos2[0]][new_pos2[1]]

    return plaintext

yes_no = True
while yes_no:
    choice = input("Playfair encryption or decryption? (e or d): ")

    if choice.lower() == 'e':
        key = input("Enter the key: ")  
        plaintext = input("Enter the Plain Text: ")
        key_matrix = generate_key_matrix(key)
        print("Key Matrix:")
        print(key_matrix)
        ciphertext = playfair_encrypt(plaintext, key_matrix)
        print("\nCiphertext:", ciphertext)

        choice = input("Do you want to perform another operation? (yes/no): ")
        if choice.lower() == 'no':
          yes_no = False

        
    elif choice.lower() == 'd':
        key = input("Enter the key: ")  
        ciphertext = input("Enter the Ciphertext: ")
        key_matrix = generate_key_matrix(key)
        print("Key Matrix:")
        print(key_matrix)
        decrypted_text = playfair_decrypt(ciphertext, key_matrix)
        print("\nDecrypted Text:", decrypted_text)
        choice = input("Do you want to perform another operation? (yes/no): ")
        if choice.lower() == 'no':
           yes_no = False
    
    else:
        print("Invalid choice!")

    