# Data
words = {'A': '._', 'B': '_...', 'C': '_._.', 'D': '_..', 'E': '.', 'F': '.._.',
         'G': '__.', 'H': '....', 'I': '..', 'J': '.___', 'K': '_._', 'L': '._..',
         'M': '__', 'N': '_.', 'O': '___', 'P': '.__.', 'Q': '__._', 'R': '._.',
         'S': '...', 'T': '_', 'U': '.._', 'V': '..._', 'W': '.__', 'X': '_.._',
         'Y': '_.__', 'Z': '__..', ' ': ' ',
         '1': '.____', '2': '..___', '3': '...__', '4': '...._', '5': '.....',
         '6': '_....', '7': '__...', '8': '___..', '9': '____.', '0': '_____',
         '.': '._._._', ',': '__..__', "''": '.____.', '=': '_..._', '?': '..__..'
         }
translate = {"._": 'A', "_...": 'B', "_._.": 'C', "_..": 'D', ".": 'E',
             ".._.": 'F', "__.": 'G', "....": 'H', "..": 'I', ".___": 'J',
             "_._": 'K', "._..": 'L', "__": 'M', "_.": 'N', "___": 'O', ".__.": 'P',
             "__._": 'Q', "._.": 'R', "...": 'S', "_": 'T', ".._": 'U', "..._": 'V',
             ".__": 'W', "_.._": 'X', "_.__": 'Y', "__..": 'Z'
             }

print("Option 1: English to Morse code \n"
      "Option 2: Morse code to English")
select = int(input())

if select == 1:
    enter = str(input("Enter a letter please: ")).upper()
    for i in enter:
        print(words[i], end=" ")
elif select == 2:
    print("Enter the Morse code:  ")
    for i in range(4):
        nt = str(input()).upper()
        side = ''
        empty = "  "
        for j in range(len(nt)):
            if nt[j] == len(nt) - 1:
                break
            elif nt[j] == ' ':
                if nt[j+1] == ' ':
                    print(translate[side], end="")
                    print("  ", end="")
                    side = ''
                    continue
                else:
                    if side == '':
                        side = ''
                        continue
                    print(translate[side], end="")
                    print("", end="")
                    side = ''
                    continue
            side = side + nt[j]
        print(translate[side], end="")
else:
    print("Wrong input! Enter option 1 or 2: ")
    select = int(input())
