#!/usr/bin/env python3

from random import randint
import time
import os

#colors
yellow = '\033[93m'
green = '\033[92m'
info = '\033[93m[!]\033[0m'
good = '\033[92m[+]\033[0m'

#variables
CUPS = [1, 2, 3]
SWAPS = [(0, 1), (0, 2), (1, 2)]
ANIMATIONS = ['a', 'b', 'c', 'd', 'e', 'f']
ANIM_CD = 0.15
B = '©'


#lets begin
def clear():
    os.system('clear')


def draw_cups():
    clear()
    print('░░░░░')
    print('█░█░█')


def show_ball(n):
    clear()
    if n == 1:
        print('█░░░░')
        print(f'{B}░█░█')
    elif n == 2:
        print('░░█░░')
        print(f'█░{B}░█')
    elif n == 3:
        print('░░░░█')
        print(f'█░█░{B}')


def swap(n):
    CUPS[SWAPS[n][0]], CUPS[SWAPS[n][1]] = CUPS[SWAPS[n][1]], CUPS[SWAPS[n][0]]


def shuffle(n):
    for i in range(n):
        swap_n = randint(0, len(SWAPS) - 1)
        swap(swap_n)
        play_animation(swap_n)


def play_animation(n):
    animation_n = n * 2 + randint(0, 1)
    assert animation_n in [0, 1, 2, 3, 4, 5]
    clear()
    if ANIMATIONS[animation_n] == 'a':
        print('█░░░░')
        print('░░█░█')
        time.sleep(ANIM_CD)
        clear()
        print('░█░░░')
        print('░░█░█')
        time.sleep(ANIM_CD)
        clear()
        print('░░█░░')
        print('░█░░█')
    elif ANIMATIONS[animation_n] == 'b':
        print('░░█░░')
        print('█░░░█')
        time.sleep(ANIM_CD)
        clear()
        print('░█░░░')
        print('█░░░█')
        time.sleep(ANIM_CD)
        clear()
        print('█░░░░')
        print('░█░░█')
    elif ANIMATIONS[animation_n] == 'c' or ANIMATIONS[animation_n] == 'd':
        print('█░░░█')
        print('░░█░░')
        time.sleep(ANIM_CD)
        clear()
        print('░█░█░')
        print('░░█░░')
        time.sleep(ANIM_CD)
        clear()
        print('░░█░░')
        print('░░█░░')
        time.sleep(ANIM_CD)
        clear()
        print('░█░█░')
        print('░░█░░')
        time.sleep(ANIM_CD)
        clear()
        print('█░░░█')
        print('░░█░░')
    elif ANIMATIONS[animation_n] == 'e':
        print('░░█░░')
        print('█░░░█')
        time.sleep(ANIM_CD)
        clear()
        print('░░░█░')
        print('█░░░█')
        time.sleep(ANIM_CD)
        clear()
        print('░░░░█')
        print('█░░█░')
    elif ANIMATIONS[animation_n] == 'f':
        print('░░░░█')
        print('█░█░░')
        time.sleep(ANIM_CD)
        clear()
        print('░░░█░')
        print('█░█░░')
        time.sleep(ANIM_CD)
        clear()
        print('░░█░░')
        print('█░░█░')
    time.sleep(ANIM_CD)
    draw_cups()
    time.sleep(ANIM_CD)


def main():
    global ANIM_CD
    shuffles = 5
    score = 0
    draw_cups()
    for level in range(3):
        ball = randint(1, 3)
        print(green,f'Your score: {score}')
        print(yellow,f'Level: {level+1}/3')
        start = input(f'Press Enter to start... ')
        show_ball(CUPS.index(ball) + 1)
        time.sleep(1)
        draw_cups()
        time.sleep(0.5)
        shuffle(shuffles)
        possible_score = 10 * (level + 1)
        penalty = possible_score // 2
        while True:
            guess = input('Where\'s the ball (1, 2, 3)? ''\033[93m')
            while True:
                if int(guess) not in [1, 2, 3]:
                    guess = input('Choose 1, 2 or 3: ''\033[93m')
                else:
                    break
            if CUPS[int(guess) - 1] == ball:
                show_ball(CUPS.index(ball) + 1)
                print(good,"That's right!")
                score += possible_score
                break
            else:
                possible_score -= penalty
                if possible_score < 0:
                    possible_score = 0
                print(info,"Wrong!")

        shuffles += 5
        ANIM_CD -= 0.05
    print(good,f'Final score: {score}')


if __name__ == '__main__':
    main()
