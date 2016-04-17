#!/usr/bin/python
# -*- coding: windows-1253 -*-

"""
Contains variables and data structures that are used as settings for the subtitle checker.
They are in a different file so they can be modified indepedently.
"""

# Wrong words
regExp = (
             '\.\.\.\.?', '(^|\s|\n|�)"(\D+)', '(\D+|�)"', '\?', '!',
             '(\n|\s)([��]���)(\n|\s)', "(^|\n|\s)([����])�(\n|\s)'([��]���)(\n|\s)", "('[��])��",
             "(\n|\s'?�)�(\n|\s)", "(\n|\s'?�)�(\n|\s)", "(\n|\s)([��]�|��)(\n|\s)",
             '([��]������)�(�|�)', '(^|\s|\n)([��])��(�|�)', '([��]�)����', '([��]�)����', '([��]��)(����)', '(^|\n|\s)([��]����)(��)', '(^|\n|\s)([��]���)(��)',
             '(^|\n|\s)([��]�|[����]�|[��]��)�(\n�?|\s�?)(�|�[^�]|�|�|�|�|�|�|�|�|�[^�]|�[^�]|�|�[^�]|�|�|�|�|�|�|�|�|�[^�]|�[^�])',
             '(^|\n|\s)([��]�|[����]�|[��]��)(\n�?|\s�?)(�|��|�|�|�|�|��|��|�|�|�|�|�|�|�|�|�|�|�|�|�|�|�|��|�|�|�|�|��|��|�|�|�|�|�|�|�|�|�|�|�|�|�|�)'
           )

# Right words to subtitute the wrong ones
# They are in the exact same order as the wrong words.
rightExp = (
                '�', r'\1�\2', r'\1�', ';', '.',
                r"\1'\2\3", r"\1\2'\3�\4\5", "\1��",
                r'\1�\2', r'\1�\2', r"\1'\2\3",
                r'\1��\2', r'\1\2��\3', r'\1���', r'\1����', r'\1�\2', r'\1\2�\3', r'\1\2�\3',
                r'\1\2\3\4',
                r'\1\2�\3\4'
           )

# Characters that are not permited as they are
# and the user must correct by hand.
swChars = (
                '^(<[i|b|u]>)?-[^\s]', '�', '@', '#', '\*', '\.\.', ';;', '\\\\', '--',
                '//', '^(<[i|b|u]>)?[\n|\s]', '\s\s', '\s[\.|;|�](<[i|b|u]>)?$', '[\.|;|�]\s(?=<[i|b|u]>)?$',
                '\n\s', '\s\n', '^�[,\.]\D+', '[,\.]�$', ',$'
           )


# Special characters that may be in a subtitle line
# but are not counted for the line lenght
special = (
            '<i>', '</i>',
            '<b>', '</b>',
            '<u>', '</u>'
           )

# Max duration of the subtitle in seconds
max_dur = 6

# Min duration of the subtitle in seconds
min_dur = 1

# Max characters for a single line
single = 30

# Max characters for a double line
double = 40

# Min gap between subs in milliseconds
gap = 0.12

# Max characters per second
cps = 18

# Easter Egg characters
greek   = ( '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�[�-Ƣ������]', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�[�-Ƣ������]', '�', '�',
            '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�',
            ';', '�', '�' )

english = ( 'A', 'A', 'V', 'G', 'D', 'E', 'E', 'Z', 'I', 'I', 'Th', 'TH', 'I', 'I', 'I', 'K', 'L', 'M', 'N', 'X', 'O', 'O', 'P', 'R', 'S', 'T', 'Y', 'Y', 'F', 'X', 'Ps', 'PS', 'O', 'O',
            'a', 'a', 'v', 'g', 'd', 'e', 'e', 'z', 'i', 'i', 'th', 'i', 'i', 'i', 'i', 'k', 'l', 'm', 'n', 'x', 'o', 'o', 'p', 'r', 's', 't', 'u', 'u', 'f', 'x', 'ps', 'o', 'o', 's',
            '?', 'u', 'Y' )        

if __name__ == "__main__":
    print( len( greek ) )
    print( len( english ) )
    
