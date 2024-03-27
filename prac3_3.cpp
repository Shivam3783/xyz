#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

unordered_map<char, char> createKeyMapping() {
    unordered_map<char, char> keyMap;
    keyMap['A'] = 'D';
    keyMap['B'] = 'E';
    keyMap['C'] = 'F';
    keyMap['D'] = 'G';
    keyMap['E'] = 'H';
    keyMap['F'] = 'I';
    keyMap['G'] = 'J';
    keyMap['H'] = 'K';
    keyMap['I'] = 'L';
    keyMap['J'] = 'M';
    keyMap['K'] = 'N';
    keyMap['L'] = 'O';
    keyMap['M'] = 'P';
    keyMap['N'] = 'Q';
    keyMap['O'] = 'R';
    keyMap['P'] = 'S';
    keyMap['Q'] = 'T';
    keyMap['R'] = 'U';
    keyMap['S'] = 'V';
    keyMap['T'] = 'W';
    keyMap['U'] = 'X';
    keyMap['V'] = 'Y';
    keyMap['W'] = 'Z';
    keyMap['X'] = 'A';
    keyMap['Y'] = 'B';
    keyMap['Z'] = 'C';
    return keyMap;
}

string encryptText(const string& plainText, const unordered_map<char, char>& keyMap) {
    string encryptedText = "";

    for (int i = 0; i < plainText.size(); ++i) {
        char c = plainText[i];
        char charKey = toupper(c);

        if (isalpha(c)) {
            if (islower(c)) {
                encryptedText += tolower(keyMap.at(charKey));
            } else {
                encryptedText += keyMap.at(charKey);
            }
        } else {
            encryptedText += c; // maintain non-alphabetic characters
        }
    }

    return encryptedText;
}

int main() {
    unordered_map<char, char> keyMap = createKeyMapping();
    
    string plainText;
    cout << "Enter the text to be encrypted: ";
    getline(cin, plainText);

    string encryptedText = encryptText(plainText, keyMap);

    cout << "Original text: " << plainText << endl;
    cout << "Encrypted text: " << encryptedText << endl;

    return 0;
}
