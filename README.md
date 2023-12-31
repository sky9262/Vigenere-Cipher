# Vigenère Cipher

[![Logo](./static/icon.png)](https://github.com/sky9262/Vigenere-Cipher)


[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/your-username/vigenere-cipher-web-app/blob/master/LICENSE)

🔐📊🚀

<a href="https://vigenerecipher.pythonanywhere.com/" target="_blank" rel="noopener noreferrer">
  <img src="./static/Live-Click%20Here.svg" alt="Live">
</a>




<h3 align="center">
:: Workflow ::
</h3>

## Web Demo
[WebDemo](https://github.com/sky9262/Vigenere-Cipher/assets/68050118/a88ef352-3d27-4b5c-b31b-47f4768f31d1)

## Terminal Demo
[TerminalDemo](https://github.com/sky9262/Vigenere-Cipher/assets/68050118/5840bc69-805c-46f1-ac54-491cc2a3a438)








## Table of Contents

- [About](#about)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Run](#Run)
    - [Web Server](#webserver)
    - [Api](#Api)
    - [Terminal](#terminal)
- [Usage](#usage)
- [License](#license)

## About

The <b>Vigenère Cipher</b> is a simple web-based tool that allows users to perform both <b>encryption and decryption</b> using the Vigenère cipher. The Vigenère cipher is a classical method of encrypting alphabetic text by using a simple form of polyalphabetic substitution.

This project provides a user-friendly interface for entering plaintext and keys and visualizes the encryption and decryption processes with animated transitions. The web app supports <b>Japanese and English</b> languages and provides a smooth user experience.

## Features

- Perform Vigenère encryption on input text with a key.
- Perform Vigenère decryption on encrypted text with the same key.
- Visualize the encryption and decryption processes with animations.
- Support for Japanese and English languages, with a language switch feature.
- Responsive design for various screen sizes.
- Easy integration with server-side logic for encryption and decryption.

## Getting Started

### Prerequisites

- Web browser (e.g., Chrome, Firefox, Safari)
- Python3
- Modules (flask, time, colorama, argparse, sys, random)

### Run

#### webserver
1. Clone the repository:

```bash
   git clone https://github.com/sky9262/Vigenere-Cipher.git
```

2. Navigate to the project directory:
```bash
    cd Vigenere-Cipher
```

3. Run the following command:
```bash
    py app.py
```

4. Enjoy !!!


#### Api

For Japanese Encryption:
```
https://vigenerecipher.pythonanywhere.com/encrypt?lang=jp&text=日本が本当に好きですよ&key=そら
```
* For Local: http://127.0.0.1:5000/encrypt?lang=jp&text=日本が本当に好きですよ&key=そら

For English Encryption:
```
https://vigenerecipher.pythonanywhere.com/encrypt?lang=en&text=I Really Love Japan!!!&key=sky
```
#### Here `lang`, `text` and `key` are parameters :
- `lang` --> Plain text language (<b>en/eng/english</b> or <b>jp/jap/japanese</b>)
- `text` --> Input text (plain text / encrypted text)
- `key` --> Key
* you can also specify response type json or plaintext:
```
http://127.0.0.1:5000/encrypt?lang=jp&text=日本が本当に好きですよ&key=そら&type=json
```

#### terminal
1. Clone the repository:

   ```bash
   git clone https://github.com/sky9262/Vigenere-Cipher.git

2. Navigate to the project directory:
    ```bash
    cd Vigenere-Cipher

3. Run the following command:
   ```bash
   #for japanese
   py JP_Vigenère_Cipher.py

         #OR

   #for english
   py EN_Vigenère_Cipher.py

### One lineer
```bash
py JP_Vigenère_Cipher.py -o encrypt -t "Hello World, How are you?" -k thisismykey
```
#### Here `-o`, `-t` and `-k` are options :
- `-o` --> Operation (encrypt / decrypt)
- `-t` --> Input text (plain text / encrypted text)
- `-k` --> Key


## Usage

1. Open the web app in your web browser.

2. Choose the language (English or Japanese) using the language switch feature.

3. Select the "Encryption" tab to encrypt plaintext or the "Decryption" tab to decrypt text.

4. Enter the input text in the "Plain Text" or "Encrypted Text" field.

5. Enter the encryption/decryption key in the "Key" field.

6. Click the "Encrypt" or "Decrypt" button to initiate the process. The text transition will be visualized with animations.

7. View the result in the "Encrypted Text" or "Plain Text" field, depending on whether you encrypted or decrypted the text.






## License

This project is licensed under the [MIT License](LICENSE), which means you can use and modify the code for your own purposes. Please see the [License](LICENSE) file for more details.

---
