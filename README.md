# Vigenère Cipher

[![Logo](./static/icon.png)](https://github.com/sky9262/Vigenere-Cipher)


[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/your-username/vigenere-cipher-web-app/blob/master/LICENSE)

🔐📊🚀

[![Live](./static/Live-Click%20Here.svg)](https://vigenerecipher.pythonanywhere.com/)

## Table of Contents

- [About](#about)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Run](#Run)
    - [Web Server](#webserver)
    - [Terminal](#terminal)
- [Usage](#usage)
- [Contributing](#contributing)
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
- Web server (for server-side encryption and decryption, if required)

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

<h3 align="center">
:: Workflow ::
</h3>
