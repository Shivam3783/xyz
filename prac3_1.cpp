#include <iostream>

using namespace std;

string alphabet = "abcdefghijklmnopqrstuvwxyz";

string caesar(const string &text, int key, bool encrypt = true)
{
  string result = "";

  for (int i = 0; i < text.length(); ++i){
    char c = text[i];

    if (isalpha(c)){
      char letter = c;

      int i = alphabet.find(tolower(letter));

      if (encrypt){
        i = (i + key) % 26;
      }
      else{
        i = (i - key + 26) % 26;
      }

      letter = alphabet[i];
      result += letter;
    }
    else{
      result += c; // maintain non-alphabetic characters
    }
  }

  return result;
}

int main()
{
  bool running = true;

  while (running){
    char direction;
    cout << "Encrypt(e) or Decrypt(d)? ";
    cin >> direction;

 
    string text;
    cout << "Enter text: ";
    cin.ignore(); // Clear input buffer
    getline(cin, text);

    int key;
    cout << "Enter key: ";
    cin >> key;

    if (direction == 'e'){
      cout << caesar(text, key) << endl;
    }
    else{
      cout << caesar(text, key, false) << endl;
    }

    char contin;
    cout << "Continue? (y/n) ";
    cin >> contin;

    if (contin != 'y'){
      running = false;
    }
  }

  cout << "Done" << endl;

  return 0;
}
