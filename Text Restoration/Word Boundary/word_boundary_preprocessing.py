from nltk.corpus import brown
from nltk.corpus import gutenberg
from nltk.corpus import reuters

stext = ''
stext_nospace = ''

punc = ['-', ';', '(', ')']

for word in gutenberg.words():
    flag = True
    for char in word:
        if not char.isalpha() and not char in punc:
            flag = False
            break
    if flag:
        stext += word.lower() + ' '
        stext_nospace += word.lower()

for word in brown.words():
    flag = True
    for char in word:
        if not char.isalpha() and not char in punc:
            flag = False
            break
    if flag:
        stext += word.lower() + ' '
        stext_nospace += word.lower()
            

for file in reuters.fileids():
    if file.startswith('test'):
        for word in reuters.words(file):
            flag = True
            for char in word:
                if not char.isalpha() and not char in punc:
                    flag = False
                    break
            if flag:
                stext += word.lower() + ' '
                stext_nospace += word.lower()
    
            
f = open("gutenberg_brown_reuters.txt", "w+")


cm7, cm6, cm5, cm4, cm3, cm2, cm1 = '_', '_', '_', '_', '_', '_', '_'

for i, char in enumerate(stext):
    if char != ' ':
        f.write(cm7 + ' ')
        f.write(cm6 + ' ')
        f.write(cm5 + ' ')
        f.write(cm4 + ' ')
        f.write(cm3 + ' ')
        f.write(cm2 + ' ')
        f.write(cm1 + ' ')
        c = 7
        x = i
        
        while c < 15:
            if stext[x] != ' ':
                f.write(stext[x] + ' ')
                c += 1
            x += 1
        
        if stext[i+1] == ' ':
            f.write('1\n')
        else:
            f.write('0\n')
            
        cm7 = cm6
        cm6 = cm5
        cm5 = cm4
        cm4 = cm3
        cm3 = cm2
        cm2 = cm1
        cm1 = char

f.close()