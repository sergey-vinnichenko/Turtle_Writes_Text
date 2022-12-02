Run program  –  python3 path/index.py

Written in Python 3.11.0

This little program was written by me while learning to program in Python.

This program can draw text in the Turtle module. This text must be entered through the Terminal.

The 'symbols' folder contains the 'symbols.py' file. This file contains the 'how_to_draw_all_symbols.py' dictionary. This dictionary describes the coordinates of the points on which to write each letter. Each letter is drawn on a 2x4 grid. Here is an example:

'A': [
        [0, 2],
        [1, 2],
        [1, 0],
        [0, -2],
        [-2, 0],
        [2, 0],
        [0, -2]
    ],

By changing this file, we can add new characters to the library, as well as change the entire font or the style of individual characters.

I could have drawn a much more beautiful and complicated font, but my task was not to draw beautiful fonts, but to learn to code.

If you will write 'ABC' in the terminal, the program will write all the characters that are in the dictionary.

Before the program starts drawing text, it draws circles to create a beautiful background for the text. Their number, size and color are set randomly.

##RGB Generator

In this program, the color of the background circles and the color of the text are set randomly. To do this, I wrote a special module for working with RGB colors. This module generates random RGB colors with a given brightness. It is located in the  folder named 'colors' in the 'random_rgb.py' file.R (red), G (green), B(blue) can be specified in the range from 1 to 255. Thus, the sum of R+G+B can be from 3 to 765. The 'random_rgb.py' module generates a random color with the specified sum. For example, R, G, and B can be any value, but their sum must be 300.

If you enter 'COLORTEST' in the Terminal when starting the program, then the program will draw a table with random RGB colors and arrange them in lines from lighter to darker..

