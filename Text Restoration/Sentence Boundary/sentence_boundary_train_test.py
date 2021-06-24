'''
This section generates the dataset that was used in TiMBL. When attempting to
solve the sentence boundary problem, the entire dataset was used for training
and the "story" file was used for testing. When calculating system accuracy,
this same dataset was split into a training (80%) and a testing (20%) set.
'''

#Collects the words of Jane Austen's "Emma" in a single list.
#For the run that used the Bible as a dataset, the only change that is required
#is for line 11 to say 'bible-kjv.txt' instead.
from nltk.corpus import gutenberg
emma = gutenberg.words('austen-emma.txt')

#List of punctuation symbols that are allowed in the dataset.
punc = ['-', ';', '(', ')', '.']

emma_processed = []

#Preprocessing of Emma in order to remove unwanted punctuation. Each word is
#scanned character by character to ensure that only alphabetical characters and
#certain punctuation symbols are retained. Each word is also turned to
#lowercase.
for word in emma:
    flag = True
    for char in word:
        if not char.isalpha() and not char in punc:
            flag = False
            break
    if flag:
        emma_processed.append(word.lower())

#Opens the file in which the dataset is stored.
f1 = open('austen_sent.txt', 'w+')

#These variables are initialised with filler values in order to fill the left
#side of the sliding window in the beginning of the file. Afterwards, they are
#still used to write the first 5 words of the window.
wm5 = wm4 = wm3 = wm2 = wm1 = '_'

#Control variable to ensure that no index out of bounds error occurs.
l = len(emma_processed)

for i, word in enumerate(emma_processed):
    #Ensures that no '.' is included in the training data.
    if word != '.' and i < l - 10:
        f1.write(wm5 + ' ')
        f1.write(wm4 + ' ')
        f1.write(wm3 + ' ')
        f1.write(wm2 + ' ')
        f1.write(wm1 + ' ')
        
        #word_counter is used to ensure that the window is always kept the same
        #size, while emma_index helps by allowing the program to "look forward"
        #and collect words that are used to fill the right side of the window.
        word_counter = 5
        emma_index = i
        while word_counter < 11:
            following_word = emma_processed[emma_index]
            if following_word != '.':
                f1.write(following_word + ' ')
                word_counter += 1
            emma_index += 1
        
        #Calculation of response variable.
        if emma_processed[i+1] == '.':    
            f1.write('1')
        else:
            f1.write('0')
        
        #Effectively shifts the left part of the window one word forward.
        wm5 = wm4
        wm4 = wm3
        wm3 = wm2
        wm2 = wm1
        wm1 = word
        
        f1.write('\n')

f1.close()



'''
This section generates the aforementioned "story" file for use as testing
dataset for TiMBL when attempting to solve the sentence boundary task.
'''

#Opens the file received from the word boundary detection task.
f2 = open('word_boundary_prediction_output.txt', 'r')

#Stores the contents of the file in a single string.
text = ' '
for line in f2:
    text += line

f2.close()

#Converts that string into a list of words.
text = text.split()

#Opens the file in which the dataset is stored.
f3 = open('story_sent_test.txt', 'w+')

'''
Same thinking as seen above, however this time the code does not treat the
window's left and right side separately. That causes a minor problem since,
in order to avoid an out of bounds error, a few of the words of the initial
file are omitted. Since this file only needed to be generated once and was
then used for testing purposes repeatedly, the omission was corrected manually
by inserting the following lines into the txt file.

vanity ; and my eyes burned with anguish and anger _ 0
; and my eyes burned with anguish and anger _ _ 0
and my eyes burned with anguish and anger _ _ _ 0
my eyes burned with anguish and anger _ _ _ _ 0
eyes burned with anguish and anger _ _ _ _ _ 0

'''
wm10 = wm9 = wm8 = wm7 = wm6 = '_'
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