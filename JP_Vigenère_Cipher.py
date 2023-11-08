import time
import random
import colorama
import argparse
import sys

def get_vig_key_val(vig_key):
    if 0x3040 <= ord(vig_key) <= 0x309F: #vig_key Hiragana
        vig_key_val = ord(vig_key) - (ord("ぁ")-1)
    elif 0x30A0 <= ord(vig_key) <= 0x30FF: #vig_key Katakana
        vig_key_val = ord(vig_key) - (ord("ァ")-1)
    elif 0x4E00 <= ord(vig_key) <= 0x9FFF: #vig_key Kanji
        vig_key_val = ord(vig_key) - ord("一")
    elif 0xFF61 <= ord(vig_key) <= 0xFF9F: #vig_key Half-width Katakana
        vig_key_val = ord(vig_key) - ord("｡")
    elif 0xFF65 <= ord(vig_key) <= 0xFF9D: #vig_key Half-width Hiragana
        vig_key_val = ord(vig_key) - ord("･")

    return vig_key_val

def vigenere_encrypt(plaintext, key):
    counter = 0
    encrypted_text = ""
    for char in plaintext:
        vig_key_val = 0
        char_point = ord(char)
        vig_key = key[counter]
        if 0x3040 <= char_point <= 0x309F: #Char Hiragana
            vig_key_val = get_vig_key_val(vig_key)

            vig_char = chr(((ord(char) - (ord("ぁ")-1) + vig_key_val) %96) + (ord("ぁ")-1))
            counter += 1

        elif 0x30A0 <= char_point <= 0x30FF: #Char Katakana
            vig_key_val = get_vig_key_val(vig_key)

            vig_char = chr(((ord(char) - (ord("ァ")-1) + vig_key_val) %96) + (ord("ァ")-1))
            counter += 1

        elif 0x4E00 <= char_point <= 0x9FFF: #Char Kanji
            vig_key_val = get_vig_key_val(vig_key)

            vig_char = chr(((ord(char) - ord("一") + vig_key_val) %20992) + ord("一"))
            counter += 1

        elif 0xFF61 <= char_point <= 0xFF9F: #Char Half-width Katakana
            vig_key_val = get_vig_key_val(vig_key)

            vig_char = chr(((ord(char) - ord("｡") + vig_key_val) %63) + ord("｡"))
            counter += 1

        elif 0xFF65 <= char_point <= 0xFF9D: #Char Half-width Hiragana
            vig_key_val = get_vig_key_val(vig_key)

            vig_char = chr(((ord(char) - ord("･") + vig_key_val) %41) + ord("･"))
            counter += 1

        else:
            vig_char = char

        if counter == len(key):
            counter = 0

        encrypted_text += vig_char

    return encrypted_text

def vigenere_decrypt(encrypted_text, key):
    counter = 0
    decrypted_text = ""
    for char in encrypted_text:
        vig_key_val = 0
        char_point = ord(char)
        vig_key = key[counter]
        if 0x3040 <= char_point <= 0x309F: #Char Hiragana
            vig_key_val = get_vig_key_val(vig_key)

            vig_char = chr((((ord(char) - (ord("ぁ")-1)) - vig_key_val) %96) + (ord("ぁ")-1))
            counter += 1

        elif 0x30A0 <= char_point <= 0x30FF: #Char Katakana
            vig_key_val = get_vig_key_val(vig_key)

            vig_char = chr((((ord(char) - (ord("ァ")-1)) - vig_key_val) %96) + (ord("ァ")-1))
            counter += 1

        elif 0x4E00 <= char_point <= 0x9FFF: #Char Kanji
            vig_key_val = get_vig_key_val(vig_key)

            vig_char = chr((((ord(char) - ord("一")) - vig_key_val) %20992) + ord("一"))
            counter += 1

        elif 0xFF61 <= char_point <= 0xFF9F: #Char Half-width Katakana
            vig_key_val = get_vig_key_val(vig_key)

            vig_char = chr((((ord(char) - ord("｡")) - vig_key_val) %63) + ord("｡"))
            counter += 1

        elif 0xFF65 <= char_point <= 0xFF9D: #Char Half-width Hiragana
            vig_key_val = get_vig_key_val(vig_key)

            vig_char = chr((((ord(char) - ord("･")) - vig_key_val) %41) + ord("･"))
            counter += 1

        else:
            vig_char = char

        if counter == len(key):
            counter = 0

        decrypted_text += vig_char

    return decrypted_text

def gen_ran_char(char):
    char_code = ord(char)
    if 0x3040 <= char_code <= 0x309F:
        rand_char = chr(random.randint(0x3041, 0x3096))
    elif 0x30A0 <= char_code <= 0x30FF:
        rand_char = chr(random.randint(0x30A1, 0x30F6))
    elif 0x4E00 <= char_code <= 0x9FFF:
        rand_char = chr(random.randint(0x4E00, 0x9FFF))
    elif 0xFF61 <= char_code <= 0xFF9F:
        rand_char = chr(random.randint(0xFF66, 0xFF9D))
    elif 0xFF65 <= char_code <= 0xFF9D:
        rand_char = chr(random.randint(0xFF61, 0xFF9F))
    else:
        rand_char = char

    return rand_char

def Decrypt_Animation(from_, to_):
    for i in range(len(to_)):
        chars = list(from_)  # 文字置換用のリストに変換
        if (0x3040 <= ord(chars[i]) <= 0x309F) or (0x30A0 <= ord(chars[i]) <= 0x30FF) or (0x4E00 <= ord(chars[i]) <= 0x9FFF) or (0xFF61 <= ord(chars[i]) <= 0xFF9F) or (0xFF65 <= ord(chars[i]) <= 0xFF9D):
            for _ in range(10):
                chars[i] = gen_ran_char(chars[i])  # ランダム文字
                # 印刷する行を準備する
                line = colorama.Fore.GREEN + "".join(chars[:i]) + colorama.Fore.RESET + colorama.Fore.BLUE + "".join(chars[i]) + colorama.Fore.RESET + colorama.Fore.RED + "".join(chars[i+1:]) + colorama.Fore.RESET

                print("\r復号化されたテキスト：" + line, end='', flush=True)  # Use carriage return instead of clearing the screen
                time.sleep(0.1)
            chars[i] = to_[i]  # Replace to original character

        print("\r復号化されたテキスト：" + colorama.Fore.GREEN + to_ + colorama.Fore.RESET, end='', flush=True)  # Use carriage return instead of clearing the screen
        time.sleep(0.1)
        from_ = "".join(chars)

def Encrypt_Animation(from_, to_):
    for i in range(len(to_)):
        chars = list(from_)  # 文字置換用のリストに変換
        if (0x3040 <= ord(chars[i]) <= 0x309F) or (0x30A0 <= ord(chars[i]) <= 0x30FF) or (0x4E00 <= ord(chars[i]) <= 0x9FFF) or (0xFF61 <= ord(chars[i]) <= 0xFF9F) or (0xFF65 <= ord(chars[i]) <= 0xFF9D):
            for _ in range(10):
                chars[i] = gen_ran_char(chars[i])  # ランダム文字
                # 印刷する行を準備する
                line = colorama.Fore.RED + "".join(chars[:i]) + colorama.Fore.RESET + colorama.Fore.BLUE + "".join(chars[i]) + colorama.Fore.RESET + colorama.Fore.GREEN + "".join(chars[i+1:]) + colorama.Fore.RESET

                print("\r復号化されたテキスト：" + line, end='', flush=True)  # Use carriage return instead of clearing the screen
                time.sleep(0.1)
            chars[i] = to_[i]  # Replace to original character

        print("\r復号化されたテキスト：" + colorama.Fore.RED + to_ + colorama.Fore.RESET, end='', flush=True)  # Use carriage return instead of clearing the screen
        time.sleep(0.1)
        from_ = "".join(chars)

def noArgs():
    # Define the menu
    menu = """
    1. メッセージを暗号化：
    2. メッセージの復号化：
    3. 鍵を挿入：
    """

    #　coloramaの初期化
    colorama.init()
    # メニューオプションに色を付ける
    print(colorama.Fore.YELLOW + menu + colorama.Fore.RESET)

    # ユーザーの選択を得る
    choice = input("\n選択肢を入力：")
    key = ""
    # 手術の実施
    if choice == "1" or choice == "１":
        plaintext = input("\nテキストメッセージを入力：")
        if key != "":
            encrypted_text = vigenere_encrypt(plaintext, key)
            # print("\n暗号化されたテキスト：" + colorama.Fore.BLUE + encrypted_text + colorama.Fore.RESET)
            Encrypt_Animation(plaintext, encrypted_text)
            print("\n鍵：" + colorama.Fore.RED + key + colorama.Fore.RESET+"\n*鍵を覚えておいてください！！！")

        else:
            key = input("鍵を入力：")
            encrypted_text = vigenere_encrypt(plaintext, key)
            # print("\n暗号化されたテキスト：" + colorama.Fore.BLUE + encrypted_text + colorama.Fore.RESET)

            Encrypt_Animation(plaintext, encrypted_text)
            print("\n鍵：" + colorama.Fore.RED + key + colorama.Fore.RESET+"\n*鍵を覚えておいてください！！！")
    elif choice == "2" or choice == "２":
        encrypted_text = input("\n暗号化されたメッセージを入力：")
        if key != "":
            decrypted_text = vigenere_decrypt(encrypted_text, key)
            Decrypt_Animation(encrypted_text, decrypted_text)
            print("\n鍵：" + colorama.Fore.GREEN + key + colorama.Fore.RESET+"\n\n")

        else:
            key = input("鍵を入力：")
            decrypted_text = vigenere_decrypt(encrypted_text, key)
            Decrypt_Animation(encrypted_text, decrypted_text)
            print("\n鍵：" + colorama.Fore.GREEN + key + colorama.Fore.RESET+"\n\n")
    elif choice == "3" or choice == "３":
        key = input("\n鍵を入力：")
    else:
        print("\n無効な選択...!")

    # ユーザーに続けるかどうか尋ねる
    while input("\n続けるか？(はい/いいえ）：") == "はい":

        print(colorama.Fore.YELLOW + menu + colorama.Fore.RESET)

        # ユーザーの選択を得る
        choice = input("\n選択肢を入力：")
        key = ""
        # 手術の実施
        if choice == "1" or choice == "１":
            plaintext = input("\nテキストメッセージを入力：")
            if key != "":
                encrypted_text = vigenere_encrypt(plaintext, key)
                # print("\n暗号化されたテキスト：" + colorama.Fore.BLUE + encrypted_text + colorama.Fore.RESET)
                Encrypt_Animation(plaintext, encrypted_text)
                print("\n鍵：" + colorama.Fore.RED + key + colorama.Fore.RESET+"\n*鍵を覚えておいてください！！！")

            else:
                key = input("鍵を入力：")
                encrypted_text = vigenere_encrypt(plaintext, key)
                # print("\n暗号化されたテキスト：" + colorama.Fore.BLUE + encrypted_text + colorama.Fore.RESET)
                Encrypt_Animation(plaintext, encrypted_text)
                print("\n鍵：" + colorama.Fore.RED + key + colorama.Fore.RESET+"\n*鍵を覚えておいてください！！！")
        elif choice == "2" or choice == "２":
            encrypted_text = input("\n暗号化されたメッセージを入力：")
            if key != "":
                decrypted_text = vigenere_decrypt(encrypted_text, key)
                Decrypt_Animation(encrypted_text, decrypted_text)
                print("\n鍵：" + colorama.Fore.RED + key + colorama.Fore.RESET+"\n")

            else:
                key = input("鍵を入力：")
                decrypted_text = vigenere_decrypt(encrypted_text, key)
                Decrypt_Animation(encrypted_text, decrypted_text)
                print("\n鍵：" + colorama.Fore.RED + key + colorama.Fore.RESET+"\n")

        elif choice == "3" or choice == "３":
            key = input("\n鍵を入力：")
        else:
            print("\n無効な選択...!")


def main():

    if len(sys.argv) == 1:
        noArgs()
        return

    # 引数パーサーを作成
    parser = argparse.ArgumentParser(description="テキストの暗号化と復号化")

    # 操作（暗号化または復号化）を定義
    parser.add_argument("-o", "--operation", required=True, choices=["暗号化", "復号化"], help="操作: 暗号化または復号化")

    # 鍵引数を定義
    parser.add_argument("-k", "--key", required=True, help="暗号化鍵/復号化鍵")

    # テキスト引数を定義
    parser.add_argument("-t", "--text", required=True, help="暗号化または復号化するテキスト")

    # コマンドライン引数を解析
    args = parser.parse_args()


    if args.operation == "暗号化":
        encrypted_text = vigenere_encrypt(args.text, args.key)
        # Crypt_Animation(args.text, encrypted_text)
        # print("\n鍵：" + colorama.Fore.RED + args.key + colorama.Fore.RESET+"\n*鍵を覚えておいてください！！！")
        print(encrypted_text)
    elif args.operation == "復号化":
        decrypted_text = vigenere_decrypt(args.text, args.key)
        # Crypt_Animation(args.text, decrypted_text)
        # print("\n鍵：" + colorama.Fore.RED + args.key + colorama.Fore.RESET+"\n*鍵を覚えておいてください！！！")
        print(decrypted_text)

if __name__ == "__main__":
    main()



# coloramaの初期化解除
colorama.deinit()


# ひらがな: 3040 - 309f (12352-12447 in ASCII)
# カタカナ: 30a0 - 30ff (12448-12543 in ASCII)
# 漢字: 4e00-4DB5 (19968-19893 ASCII)
