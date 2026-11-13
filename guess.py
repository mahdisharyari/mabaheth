import random

def play_guess_game():
    # سیستم یک عدد تصادفی بین 1 تا 100 انتخاب می‌کند
    secret_number = random.randint(1, 100)
    attempts_left = 10
    won = False

    print("--- به بازی حدس عدد خوش آمدید! ---")
    print("من یک عدد بین 1 تا 100 در نظر گرفته‌ام. شما 10 فرصت برای حدس آن دارید.")

    # حلقه تا زمانی که فرصت تمام نشده یا کاربر برنده نشده ادامه دارد
    while attempts_left > 0:
        print(f"\nفرصت‌های باقی‌مانده: {attempts_left}")
        
        try:
            # گرفتن حدس از کاربر
            guess = int(input("حدس شما چیست؟ "))
        except ValueError:
            print("لطفاً فقط یک عدد صحیح وارد کنید!")
            continue # این دور از حلقه رد می‌شود و فرصت کم نمی‌کند

        # بررسی حدس کاربر
        if guess == secret_number:
            print(f"\n🎉 تبریک! شما درست حدس زدید. عدد مورد نظر {secret_number} بود.")
            won = True
            break # خروج از حلقه چون برنده شده
        elif guess < secret_number:
            print("عدد شما کوچک‌تر از عدد من است. (برو بالاتر ⬆️)")
        else:
            print("عدد شما بزرگ‌تر از عدد من است. (بیا پایین ⬇️)")

        # کم کردن یک فرصت
        attempts_left -= 1

    # بررسی نهایی اینکه کاربر برنده شده یا باخته
    if not won:
        print(f"\n😔 متأسفانه فرصت‌های شما تمام شد. شما بازنده هستید.")
        print(f"عدد صحیح {secret_number} بود.")

# اجرای بازی
if __name__ == "__main__":
    play_guess_game()