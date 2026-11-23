def caesar_encrypt(plain_text, key):
    """
    رمزنگاری متن با روش سزار
    key: عدد کلید (تعداد جابجایی در الفبا)
    """
    encrypted = ""
    for char in plain_text:
        if char.isalpha():
            # تعیین محدوده حروف کوچک یا بزرگ
            if char.islower():
                base = ord('a')
            else:
                base = ord('A')
            # اعمال جابجایی با در نظر گرفتن چرخش الفبا
            shifted = (ord(char) - base + key) % 26 + base
            encrypted += chr(shifted)
        else:
            # کاراکترهای غیر حرفی (فاصله، عدد، علامت) بدون تغییر
            encrypted += char
    return encrypted


def caesar_decrypt(cipher_text, key):
    """
    رمزگشایی متن با روش سزار
    """
    return caesar_encrypt(cipher_text, -key)


# --- تست ---
if __name__ == "__main__":
    text = input("متن را وارد کنید (Plain Text): ")
    key = int(input("کلید (عدد) را وارد کنید: "))

    encrypted = caesar_encrypt(text, key)
    print(f"\nمتن رمز شده: {encrypted}")

    decrypted = caesar_decrypt(encrypted, key)
    print(f"متن رمزگشایی شده: {decrypted}")