#Code that converts TiMBL output to a readable txt file.

f_in = open("story_sent_test.txt.IB1.O.gr.k1.out", "r")
f_out = open("sentence_boundary_prediction_output.txt", "w+")

#Because the focused word always appears after exactly five spaces, there is a
#counter that ensures those five spaces are consumed before reading the word.

for line in f_in:
    word = ''
    space_counter = 0
    
    for char in line:
        if space_counter == 5:
            #Collection of the word character by character. The char!= '_' part
            #is necessary in case the POS tagged version is involved, while it
            #does nothing in the normal version.
            if char != ' ' and char!= '_':
                word += char
            else:
                break
        elif char == ' ':
            space_counter += 1
    
    #A period is only added if the response variable is equal to 1.
    f_out.write(word)
    if line[-2] == '1':
        f_out.write('.')
    f_out.write(' ')

f_in.close()
f_out.close()