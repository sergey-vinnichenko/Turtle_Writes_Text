__all__ = ['random_rgb']

from random import randint


def random_rgb(rgb_total):
    '''This module creates a random RGB color,
    with the sum of R + G + B is equal to the given value'''
    if rgb_total < 257:
        rgb_r = randint(1, rgb_total-2)
        rgb_g = randint(1, rgb_total - rgb_r - 1)

    elif rgb_total < 511:
        rgb_r = randint(1, 255)

        if rgb_total - rgb_r < 256:
            rgb_g = randint(1, rgb_total - rgb_r - 1)

        else:
            rgb_g = randint(rgb_total - rgb_r - 255, 255)

    elif rgb_total < 765:
        rgb_r = randint(rgb_total - 510, 255)
        rgb_g = randint(rgb_total - rgb_r - 255, 255)

    else:
        print('The rgb_total is ', rgb_total)
        exit()

    rgb_b = (rgb_total - rgb_r) - rgb_g
    print(f'R={rgb_r}, G{rgb_g}, B{rgb_b}, rgb_total = {rgb_total}')

    # checking the value
    if rgb_r > 255 or rgb_g > 255 or rgb_b > 255 or rgb_r < 1 or rgb_g < 1 or rgb_b < 1:
        print(f'Error: the value is wrong. R={rgb_r}, G{rgb_g}, B{rgb_b}')
        exit()
    if rgb_r + rgb_g + rgb_b != rgb_total:
        print(f'Error: the sum is wrong. rgb_total = {rgb_total}, R={rgb_r}, G{rgb_g}, B{rgb_b}')
        exit()

    return rgb_r, rgb_g, rgb_b
