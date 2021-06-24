#Code that converts TiMBL output to a readable txt file.

f_in = open("story_cap_test.txt.IB1.O.gr.k1.out", "r")
f_out = open("capitalisation_prediction_output.txt", "w+")

#Again, a counter is used to ensure that the correct word is parsed.

for line in f_in:
    word = ''
    space_counter = 0
    
    character_counter = 0
    
    for char in line:
        
        character_counter += 1
        
        if space_counter == 5:
            if char != ' ':
                word += char
            else:
                break
        elif char == ' ':
            space_counter += 1
    
    #If the response variable is 1, the first letter of the word is
    #capitalised. Then, a space is only added to the word if it is not followed
    #by a period or a comma.
    if line[-2] == '0':
        f_out.write(word)
    else:
        f_out.write(word[0].upper() + word[1:])
    #if word + ' .' not in line and word + ' ,' not in line:
        #f_out.write(' ')
    if line[character_counter] not in [',' , '.']:
        f_out.write(' ')

f_in.close()
f_out.close()