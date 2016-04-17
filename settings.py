#!/usr/bin/python
# -*- coding: windows-1253 -*-

"""
Contains variables and data structures that are used as settings for the subtitle checker.
They are in a different file so they can be modified indepedently.
"""

# Wrong words
regExp = (
             '\.\.\.\.?', '(^|\s|\n|…)"(\D+)', '(\D+|…)"', '\?', '!',
             '(\n|\s)([μσ]ένα)(\n|\s)', "(^|\n|\s)([μΜσΣ])ε(\n|\s)'([σμ]ένα)(\n|\s)", "('[σμ])ας",
             "(\n|\s'?γ)ω(\n|\s)", "(\n|\s'?σ)υ(\n|\s)", "(\n|\s)([γδ]ώ|σύ)(\n|\s)",
             '([Κκ]αινούρ)ι(ο|α)', '(^|\s|\n)([Αα])βγ(ό|ο)', '([Ττ]ρ)αίνο', '([Κκ]τ)ίριο', '([Σσ]υγ)(νώμη)', '(^|\n|\s)([Εε]ταιρ)(ία)', '(^|\n|\s)([Κκ]λασ)(ικ)',
             '(^|\n|\s)([Δδ]ε|[ΜμΤτ]η|[Σσ]τη)ν(\n«?|\s«?)(β|γ[^κ]|δ|ζ|θ|λ|ρ|σ|φ|χ|μ[^π]|ν[^τ]|Β|Γ[^κ]|Δ|Ζ|Θ|Λ|Ρ|Σ|Φ|Χ|Μ[^π]|Ν[^τ])',
             '(^|\n|\s)([Δδ]ε|[ΜμΤτ]η|[Σσ]τη)(\n«?|\s«?)(α|γκ|ε|η|ι|κ|μπ|ντ|ξ|ο|π|τ|υ|ψ|ω|ά|έ|ή|ί|ό|ύ|ώ|Α|Γκ|Ε|Η|Ι|Κ|Μπ|Ντ|Ξ|Ο|Π|Τ|Υ|Ψ|Ω|Ά|Έ|Ή|Ί|Ό|Ύ|Ώ)'
           )

# Right words to subtitute the wrong ones
# They are in the exact same order as the wrong words.
rightExp = (
                '…', r'\1«\2', r'\1»', ';', '.',
                r"\1'\2\3", r"\1\2'\3ε\4\5", "\1άς",
                r'\1ώ\2', r'\1ύ\2', r"\1'\2\3",
                r'\1γι\2', r'\1\2υγ\3', r'\1ένο', r'\1ήριο', r'\1γ\2', r'\1\2ε\3', r'\1\2σ\3',
                r'\1\2\3\4',
                r'\1\2ν\3\4'
           )

# Characters that are not permited as they are
# and the user must correct by hand.
swChars = (
                '^(<[i|b|u]>)?-[^\s]', '΄', '@', '#', '\*', '\.\.', ';;', '\\\\', '--',
                '//', '^(<[i|b|u]>)?[\n|\s]', '\s\s', '\s[\.|;|…](<[i|b|u]>)?$', '[\.|;|…]\s(?=<[i|b|u]>)?$',
                '\n\s', '\s\n', '^…[,\.]\D+', '[,\.]…$', ',$'
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
greek   = ( 'Α', 'Ά', 'Β', 'Γ', 'Δ', 'Ε', 'Έ', 'Ζ', 'Η', 'Ή', 'Θ', 'Θ[Α-ΖΆΈΉΊΌΎΏ]', 'Ι', 'Ί', 'Ϊ', 'Κ', 'Λ', 'Μ', 'Ν', 'Ξ', 'Ο', 'Ό', 'Π', 'Ρ', 'Σ', 'Τ', 'Υ', 'Ύ', 'Φ', 'Χ', 'Ψ', 'Ψ[Α-ΖΆΈΉΊΌΎΏ]', 'Ω', 'Ώ',
            'α', 'ά', 'β', 'γ', 'δ', 'ε', 'έ', 'ζ', 'η', 'ή', 'θ', 'ι', 'ί', 'ϊ', 'ΐ', 'κ', 'λ', 'μ', 'ν', 'ξ', 'ο', 'ό', 'π', 'ρ', 'σ', 'τ', 'υ', 'ύ', 'φ', 'χ', 'ψ', 'ω', 'ώ', 'ς',
            ';', 'ΰ', 'Ϋ' )

english = ( 'A', 'A', 'V', 'G', 'D', 'E', 'E', 'Z', 'I', 'I', 'Th', 'TH', 'I', 'I', 'I', 'K', 'L', 'M', 'N', 'X', 'O', 'O', 'P', 'R', 'S', 'T', 'Y', 'Y', 'F', 'X', 'Ps', 'PS', 'O', 'O',
            'a', 'a', 'v', 'g', 'd', 'e', 'e', 'z', 'i', 'i', 'th', 'i', 'i', 'i', 'i', 'k', 'l', 'm', 'n', 'x', 'o', 'o', 'p', 'r', 's', 't', 'u', 'u', 'f', 'x', 'ps', 'o', 'o', 's',
            '?', 'u', 'Y' )        

if __name__ == "__main__":
    print( len( greek ) )
    print( len( english ) )
    
