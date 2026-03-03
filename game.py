import random

def play_game():
    target_number = random.randint(1, 100)
    attempts = 0
    print("--- 歡迎來到 AI 猜數字遊戲 ---")
    print("我已經想好了一個 1 到 100 之間的數字，你猜是多少？")

    while True:
        try:
            guess = int(input("請輸入你的預測值: "))
            attempts += 1

            if guess < target_number:
                print("太小了，再試一次！")
            elif guess > target_number:
                print("太大了，再試一次！")
            else:
                print(f"恭喜你！你花了 {attempts} 次猜中了數字 {target_number}！")
                break
        except ValueError:
            print("請輸入有效的數字喔！")

if __name__ == "__main__":
    play_game()