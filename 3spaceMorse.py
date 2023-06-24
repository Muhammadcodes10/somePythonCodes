# Data
words = {'A': '._', 'B': '_...', 'C': '_._.', 'D': '_..', 'E': '.', 'F': '.._.',
         'G': '__.', 'H': '....', 'I': '..', 'J': '.___', 'K': '_._', 'L': '._..',
         'M': '__', 'N': '_.', 'O': '___', 'P': '.__.', 'Q': '__._', 'R': '._.',
         'S': '...', 'T': '_', 'U': '.._', 'V': '..._', 'W': '.__', 'X': '_.._',
         'Y': '_.__', 'Z': '__..', ' ': ' ',
         '1': '.____', '2': '..___', '3': '...__', '4': '...._', '5': '.....',
         '6': '_....', '7': '__...', '8': '___..', '9': '____.', '0': '_____',
         '.': '._._._', ',': '__..__', "'": '.____.', '=': '_..._', '?': '..__..'
         }
translate = {"._": 'A', "_...": 'B', "_._.": 'C', "_..": 'D', ".": 'E',
             ".._.": 'F', "__.": 'G', "....": 'H', "..": 'I', ".___": 'J',
             "_._": 'K', "._..": 'L', "__": 'M', "_.": 'N', "___": 'O', ".__.": 'P',
             "__._": 'Q', "._.": 'R', "...": 'S', "_": 'T', ".._": 'U', "..._": 'V',
             ".__": 'W', "_.._": 'X', "_.__": 'Y', "__..": 'Z',
             ".____": '1', "..___": '2', "...__": '3', "...._": '4', ".....": '5',
             "_....": '6', "__...": '7', "___..": '8', "____.": '9', "_____": '0',
             "._._._": '.', "__..__": ',', ".____.": "'", "_..._": '=', "..__..": '?'
             }
print("\nNOTES: USE 1 OR 2 SPACES TO SIGNIFY A NEW LETTER, AND AT LEAST 3 SPACES TO SIGNIFY A NEW WORD\n"
      "OPTION 1: ENGLISH TO MORSE CODE \n"
      "OPTION 2: MORSE CODE TO ENGLISH\n"
      "\nSELECT AN OPTION: ", end="")
select = int(input())
if select == 1:
    enter = str(input("ENTER THE ENGLISH WORD(S): ")).upper()
    for i in enter:
        print(words[i], end=" ")
elif select == 2:
    print("ENTER THE MORSE CODE:  ")
    for i in range(4):
        nt = str(input()).upper()
        side = ''
        for j in range(len(nt)):
            if nt[j] == len(nt) - 1:
                break
            if nt[j] == ' ':
                if nt[j+1] == ' ':
                    if nt[j+2] == ' ':
                        if side == '':
                            side = ''
                            continue
                        print(translate[side], end="")
                        print(" ", end="")
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