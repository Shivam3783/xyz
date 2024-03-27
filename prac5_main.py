import numpy as np
import math

def result_output1(label, phrase, index_to_char):
    result = label
    for i in range(0, len(phrase), 2):
        char1 = index_to_char[phrase[i]] if phrase[i] != 26 else 'Z'
        char2 = index_to_char[phrase[i + 1]] if phrase[i + 1] != 26 else 'Z'

        result += char1 + char2
        if i + 2 < len(phrase):
            result += "-"
    print(result)    

def result_output(label, phrase, index_to_char):
    print(label)
    for i in range(0, len(phrase), 2):
        char1 = index_to_char[(phrase[i]) % 26] if phrase[i] != 26 else 'Z'
        char2 = index_to_char[(phrase[i + 1]) % 26] if phrase[i + 1] != 26 else 'Z'
        index1 = phrase[i] 
        index2 = phrase[i + 1] 
        
        print(f"{char1} ({index1}), {char2} ({index2})")

  
def encrypt_with_startswith1(phrase,isOne):
    if isOne == True:
        index_to_char = {
            1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J',
            11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T',
            21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'
        }
    else:
        index_to_char = {
            0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J',
            10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T',
            20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z'
        }
    
    char_to_index = {}
    for key, value in index_to_char.items():
        char_to_index[value] = key
        

    def encrypt(phrase,isOne):
        phrase = ''.join(filter(str.isalpha, phrase)).upper()
        if len(phrase) % 2 == 1:
            phrase += "X"
        
        key = input("Enter key: ").replace(" ", "").upper()
        keyMatrix = np.zeros((2, 2), dtype=int)
        k = 0
        for i in range(2):
            for j in range(2):
                keyMatrix[i, j] = char_to_index[key[k]]  # Convert key characters to indices
                k += 1

        print("-----------------------------------------")
        print("Key Matrix values:")
        print(keyMatrix)
        print("-----------------------------------------")
        
        print("Plain Text Values:")
        for i in range(0, len(phrase), 2):
            print(f"{index_to_char[char_to_index[phrase[i]]]} ({char_to_index[phrase[i]]})", 
                  f"{index_to_char[char_to_index[phrase[i + 1]]]} ({char_to_index[phrase[i + 1]]})")

        phraseToNum = [(char_to_index[c]) % 26 for c in phrase]

        phraseEncoded = []
        for i in range(0, len(phraseToNum), 2):
            # print("phraseToNum[i]")
            # print(phraseToNum[i])
            # print("phraseToNum[i+1]")
            # print(phraseToNum[i+1])
            x = (keyMatrix[0, 0] * phraseToNum[i] + keyMatrix[0, 1] * phraseToNum[i + 1]) % 26
            if isOne == True :
                if(x==0): x=26
            # print("x")
            # print(x)
            y = (keyMatrix[1, 0] * phraseToNum[i] + keyMatrix[1, 1] * phraseToNum[i + 1]) % 26
            if isOne == True:
               if(y==0): y=26
            # print("y")
            # print(y)

            phraseEncoded.extend([x, y])
       
        print("-----------------------------------------")
        result_output("Encrypted pair: ", phraseEncoded, index_to_char)
        print("-----------------------------------------")
        result_output1("Encrypted text: ", phraseEncoded, index_to_char)

    encrypt(phrase,isOne)


def decrypt_starts_with1(phrase,isOne):
    if isOne == True:
        index_to_char = {
            1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J',
            11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T',
            21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'
        }
    else:
        index_to_char = {
            0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J',
            10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T',
            20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z'
        }
    
    char_to_index = {}
    for key, value in index_to_char.items():
        char_to_index[value] = key

            
    def decrypt(phrase, isOne):
        phrase = ''.join(filter(str.isalpha, phrase)).upper()
        if len(phrase) % 2 == 1:
            phrase += "X"
        
        key = input("Enter key: ").replace(" ", "").upper()
        keyMatrix = np.zeros((2, 2), dtype=int)
        k = 0
        for i in range(2):
            for j in range(2):
                keyMatrix[i, j] = char_to_index[key[k]]  # Convert key characters to indices
                k += 1
    
        print("-----------------------------------------")
        print("Key Matrix values:")
        print(keyMatrix)
        print("-----------------------------------------")
        
        print("Cipher Text Values:")
        
        for i in range(0, len(phrase), 2):
            print(f"{index_to_char[char_to_index[phrase[i]]]} ({char_to_index[phrase[i]]})", 
                  f"{index_to_char[char_to_index[phrase[i + 1]]]} ({char_to_index[phrase[i + 1]]})")
                  
        det = keyMatrix[0, 0] * keyMatrix[1, 1] - keyMatrix[1, 0] * keyMatrix[0, 1]  # ad-cb 
        mod_det = det % 26
        
        if math.gcd(mod_det, 26) != 1:
            print("Error: The matrix is not invertible MOD 26. Cannot decrypt.")
            return
        
        kInverse = 1
        while (mod_det * kInverse) % 26 != 1:
            kInverse += 1
        
        kInverseMatrix = np.array([[keyMatrix[1, 1], -keyMatrix[0, 1]], [-keyMatrix[1, 0], keyMatrix[0, 0]]])
        kInverseMatrix = (kInverseMatrix * kInverse) % 26
        
        print("-----------------------------------------")
        print("Inverse Key Matrix:")
        print(kInverseMatrix)
    
        phraseToNum = [(char_to_index[c]) % 26 for c in phrase]
        phraseDecoded = []
        for i in range(0, len(phraseToNum), 2):
            x = (kInverseMatrix[0, 0] * phraseToNum[i] + kInverseMatrix[0, 1] * phraseToNum[i + 1]) % 26
            if isOne == True:
             if x == 0: x = 26
            y = (kInverseMatrix[1, 0] * phraseToNum[i] + kInverseMatrix[1, 1] * phraseToNum[i + 1]) % 26
            if isOne == True:
                 if y == 0: y=26
            phraseDecoded.extend([x, y])
    
        print("-----------------------------------------")
        result_output("Decrypted pair: ", phraseDecoded,index_to_char)
        print("--------------------------------------")
        result_output1("Decrypted text: ", phraseDecoded,index_to_char)
        
    decrypt(phrase,isOne)
    
    

print("Hill Cipher Implementation (2x2)")
print("-------------------------")
print("1. Encrypt text (A=0,B=1,...Z=25)")
print("2. Encrypt text (A=1,B=2,...Z=26)")
print("3. Decrypt text (A=0,B=1,...Z=25)")
print("4. Decrypt text (A=1,B=2,...Z=26)")

print()

opt = input("Select your choice: ")
# phrase = input("Enter plaintext: ")

if opt == "1":
    phrase = input("Enter plaintext: ")
    isOne = False
    encrypt_with_startswith1(phrase, isOne)
elif opt == "2":
    phrase = input("Enter plaintext: ")
    isOne = True
    encrypt_with_startswith1(phrase, isOne)    
elif opt == "3":
    phrase = input("Enter Ciphertext: ")
    isOne = False
    decrypt_starts_with1(phrase, isOne)
elif opt == "4":
    phrase = input("Enter Ciphertext: ")
    isOne = True
    decrypt_starts_with1(phrase, isOne) 
else:
    print("Invalid choice")
