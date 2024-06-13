# def ag(a,b,c):    return (a+b+c)/3
# mun1=float(input("请输入第一个数:"))
# mun2=float(input("请输入第二个数:"))
# mun3=float(input("请输入第三个数:"))
# r=ag(mun1,mun2,mun3)
# print("平均值为:",r)


# a = int(input("输入头的数量:"))
# b = int(input("输入脚的数量:"))
# s = (b - 2 * a)/2
# q = a - s
# print("鸡有%d只,兔有%d只"%(s,q))

# import random
# list1=[]
# for _ in range(10):
#     random_mun=random.randint(1,50)
#     list1.append(random_mun)
#     print("生成的列表",list)
#     list1=sorted(list1[0:5],reverse=True)
#     list1[5:]=sorted(list1[5:])
#     print("排序后的列表:",list1)


# import os
# import time
# import random
#
# def clear_screen():
#     # Clear the terminal screen by printing a special character sequence
#     print("\033[H\033[J", end='')
#
# def move_text(text, width, height):
#     # Random initial position
#     x, y = random.randint(0, width - len(text)), random.randint(0, height - 1)
#     dx, dy = 1, 1  # Movement direction
#
#     while True:
#         clear_screen()
#         # Print text at the current position
#         print('\n' * y + (' ' * x) + text)
#
#         # Update position
#         x += dx
#         y += dy
#
#         # Change direction upon hitting the boundary
#         if x <= 0 or x >= width - len(text):
#             dx = -dx
#         if y <= 0 or y >= height - 1:
#             dy = -dy
#
#         # Wait for a short period to control the speed of the animation
#         time.sleep(0.1)
#
# def main():
#     text = "Python是我最喜欢的语言"
#     width, height = 80, 24  # Adjust according to your terminal size
#
#     try:
#         move_text(text, width, height)
#     except KeyboardInterrupt:
#         clear_screen()
#         print("动画已终止。")
#
# if __name__ == "__main__":
#     main()


import os
import time
import random
from colorama import init, Fore
os.environ['TERM'] = 'xterm'

def clear_screen():
    # Clear the terminal screen by printing a special character sequence
    os.system('cls' if os.name == 'nt' else 'clear')


def move_text(text, width, height):
    init(autoreset=True)  # Initialize Colorama for automatic reset

    # Random initial position
    x, y = random.randint(0, width - len(text)), random.randint(0, height - 1)
    dx, dy = 1, 1  # Movement direction

    while True:
        clear_screen()

        # Randomly choose a color for the text
        color = random.choice([Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN])

        # Print text at the current position with the chosen color
        print('\033[{};{}H{}{}'.format(y + 1, x + 1, color, text))

        # Update position
        x += dx
        y += dy

        # Change direction upon hitting the boundary
        if x <= 0 or x >= width - len(text):
            dx = -dx
        if y <= 0 or y >= height - 1:
            dy = -dy

        # Wait for a short period to control the speed of the animation
        time.sleep(0.1)


def main():
    a = "Python是我最喜欢的语言"
    text = a
    width, height = 80, 24  # Adjust according to your terminal size

    try:
        move_text(text, width, height)
    except KeyboardInterrupt:
        clear_screen()
        print("动画已终止。")


if __name__ == "__main__":
    main()
