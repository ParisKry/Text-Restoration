'''
This file is very similar to sentence_boundary_train_test.py, since it serves
the exact same purpose, only for the capitalisation task. As a result, comments
will only be used to specify changes to the code.
'''

from nltk.corpus import gutenberg

emma = gutenberg.words('austen-emma.txt')

emma_case_sensitive = []
punc = [';', '(', ')', '.']

for word in emma:
    flag = True
    for char in word:
        if not char.isalpha() and not char in punc:
            flag = False
            break
    if flag:
        #The words are not turned to lowercase this time because then the
        #response variable would always have the value of 0.
        emma_case_sensitive.append(word)

f1 = open("austen_cap.txt", "w+")

#Since no secondary loop is necessary to ensure that periods do not slip into
#the training data, the method that uses 10 helper variables is used instead.
wm10 = wm9 = wm8 = wm7 = wm6 = '_'
wm5 = emma_case_sensitive[0]
wm4 = emma_case_sensitive[1]
wm3 = emma_case_sensitive[2]
wm2 = emma_case_sensitive[3]
wm1 = emma_case_sensitive[4]

for i, word in enumerate(emma_case_sensitive):
    #The words are turned to lowercase here so as to match the test data.
    f1.write(wm10.lower() + ' ')
    f1.write(wm9.lower() + ' ')
    f1.write(wm8.lower() + ' ')
    f1.write(wm7.lower() + ' ')
    f1.write(wm6.lower() + ' ')
    f1.write(wm5.lower() + ' ')
    f1.write(wm4.lower() + ' ')
    f1.write(wm3.lower() + ' ')
    f1.write(wm2.lower() + ' ')
    f1.write(wm1.lower() + ' ')
    f1.write(word.lower() + ' ')
    
    #Checks if a word contains uppercase letters and calculates the response
    #variable accordingly.
    if wm5.lower() != wm5:
        f1.write('1')
    else:
        f1.write('0')
    
    wm10 = wm9
    wm9 = wm8
    wm8 = wm7
    wm7= wm6
    wm6 = wm5
    wm5 = wm4
    wm4 = wm3
    wm3 = wm2
    wm2 = wm1
    wm1 = word
    
    f1.write('\n')

f1.close()



f2 = open('comma_prediction_output.txt', 'r')

text = ' '
for line in f2:
    text += line

f2.close()

text = text.split()

f3 = open('story_cap_test.txt', 'w+')

'''
Similarly to sentence_boundary_train_test.py, a few lines have to be manually
added to avoid omitting some words at the end of the file.

; and my eyes burned with anguish and anger , _ 0
and my eyes burned with anguish and anger , _ _ 0
my eyes burned with anguish and anger , _ _ _ 0
eyes burned with anguish and anger , _ _ _ _ 0
burned with anguish and anger , _ _ _ _ _ 0

'''
wm10, wm9, wm8, wm7, wm6 = '_', '_', '_', '_', '_'
wm5 = text[0]
wm4 = text[1]
wm3 = text[2]
wm2 = text[3]
wm1 = text[4]

for i, word in enumerate(text):
    if i > 4:
        f3.write(wm10 + ' ')
        f3.write(wm9 + ' ')
        f3.write(wm8 + ' ')
        f3.write(wm7 + ' ')
        f3.write(wm6 + ' ')
        f3.write(wm5 + ' ')
        f3.write(wm4 + ' ')
        f3.write(wm3 + ' ')
        f3.write(wm2 + ' ')
        f3.write(wm1 + ' ')
        f3.write(word + ' ')
        f3.write('0\n')
        wm10 = wm9
        wm9 = wm8
        wm8 = wm7
        wm7= wm6
        wm6 = wm5
        wm5 = wm4
        wm4 = wm3
        wm3 = wm2
        wm2 = wm1
        wm1 = word

f3.close()
