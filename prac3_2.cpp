#include <iostream>
#include <string>
using namespace std;
string alphabet = "abcdefghijklmnopqrstuvwxyz";
string caesar(const string &text, int key, bool encrypt = true)
{
   string result = "";
   for (int i = 0; i < text.length(); ++i){
       char c = text[i];
       if (isalpha(c)){
           char letter = c;
           int index = alphabet.find(tolower(letter));
           if (encrypt){
               index = (index + key) % 26;
           } else{
               index = (index - key + 26) % 26;
           }
           if (isupper(c)){
               letter = toupper(alphabet[index]);
           } else{
               letter = alphabet[index];
           }
           result += letter;
       }
       else{
           result += c;
} }
   return result;
}
int main() {
   string ciphertext;
   cout << "Enter the ciphertext to be decrypted: ";
   getline(cin, ciphertext);
   cout << "Brute force decryption:" << endl;
   for (int key = 1; key <= 25; key++){
      cout << "Key: " << key << " Decrypted Text: " << caesar(ciphertext, key, false)<<endl;
   }
 return 0; }