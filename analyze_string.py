def analyze_string(text):
    """
    تحلیل رشته: تعداد کلمات، تعداد کاراکترها،
    پرتکرارترین کاراکتر، و تعداد تکرار هر کلمه
    """
    # ۱. تعداد کاراکترها (شامل فاصله‌ها)
    char_count = len(text)

    # ۲. تعداد کلمات
    words = text.split()
    word_count = len(words)

    # ۳. پرتکرارترین کاراکتر (بدون احتساب فاصله‌ها)
    char_freq = {}
    for ch in text:
        if ch != ' ':
            char_freq[ch] = char_freq.get(ch, 0) + 1

    if char_freq:
        most_common_char = max(char_freq, key=char_freq.get)
        most_common_count = char_freq[most_common_char]
    else:
        most_common_char = None
        most_common_count = 0

    # ۴. تعداد تکرار هر کلمه
    word_freq = {}
    for w in words:
        word_freq[w] = word_freq.get(w, 0) + 1

    # --- چاپ نتایج ---
    print("\n===== نتیجه تحلیل رشته =====")
    print(f"تعداد کاراکترها: {char_count}")
    print(f"تعداد کلمات: {word_count}")
    print(f"پرتکرارترین کاراکتر: '{most_common_char}' (تعداد: {most_common_count})")
    print("\nتکرار هر کلمه:")
    for w, c in word_freq.items():
        print(f"  '{w}' -> {c} بار")


# --- تست ---
if __name__ == "__main__":
    text = input("یک رشته وارد کنید: ")
    analyze_string(text)