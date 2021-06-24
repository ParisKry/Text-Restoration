#!/usr/bin/env python3
# -*- coding: utf-8 -*-

story = open("story.merged", "r")
text = ""

for line in story:
    text += line

file = open("story_mod.txt", "w+")
c7, c6, c5, c4, c3, c2, c1 = "=","=","=","=","=","=","="

for i, char in enumerate(text):
    file.write(c7 + " ")
    file.write(c6 + " ")
    file.write(c5 + " ")
    file.write(c4 + " ")
    file.write(c3 + " ")
    file.write(c2 + " ")   
    file.write(c1 + " ")
    file.write(char + " ")
    
    c7 = c6
    c6 = c5
    c5 = c4
    c4 = c3
    c3 = c2
    c2 = c1
    c1 = char
    
    if i+7 < len(text)-1:
        file.write(text[i+1] + " ")
        file.write(text[i+2] + " ")
        file.write(text[i+3] + " ")
        file.write(text[i+4] + " ")
        file.write(text[i+5] + " ")
        file.write(text[i+6] + " ")
        file.write(text[i+7] + " ")
        file.write("0\n")
        
    else:
        fill = "="
        if len(text)-1 == i+7:
            file.write(text[i+1] + " ")
            file.write(text[i+2] + " ")
            file.write(text[i+3] + " ")
            file.write(text[i+4] + " ")
            file.write(text[i+5] + " ")
            file.write(text[i+6] + " ")
            file.write(fill + " ")
            file.write("0\n")
            
        elif len(text)-1 == i+6:
            file.write(text[i+1] + " ")
            file.write(text[i+2] + " ")
            file.write(text[i+3] + " ")
            file.write(text[i+4] + " ")
            file.write(text[i+5] + " ")
            file.write(fill + " ")
            file.write(fill + " ")
            file.write("0\n")
            
        elif len(text)-1 == i+5:
            file.write(text[i+1] + " ")
            file.write(text[i+2] + " ")
            file.write(text[i+3] + " ")
            file.write(text[i+4] + " ")
            file.write(fill + " ")
            file.write(fill + " ")
            file.write(fill + " ")
            file.write("0\n")
            
        elif len(text)-1 == i+4:
            file.write(text[i+1] + " ")
            file.write(text[i+2] + " ")
            file.write(text[i+3] + " ")
            file.write(fill + " ")
            file.write(fill + " ")
            file.write(fill + " ")
            file.write(fill + " ")
            file.write("0\n")

        elif len(text)-1 == i+3:
            file.write(text[i+1] + " ")
            file.write(text[i+2] + " ")
            file.write(fill + " ")
            file.write(fill + " ")
            file.write(fill + " ")
            file.write(fill + " ")
            file.write(fill + " ")
            file.write("0\n")    
            
        elif len(text)-1 == i+2:
            file.write(text[i+1] + " ")
            file.write(fill + " ")
            file.write(fill + " ")
            file.write(fill + " ")
            file.write(fill + " ")
            file.write(fill + " ")
            file.write(fill + " ")
            file.write("0\n") 
            
        elif len(text)-1 == i+1:
            file.write(fill + " ")
            file.write(fill + " ")
            file.write(fill + " ")
            file.write(fill + " ")
            file.write(fill + " ")
            file.write(fill + " ")
            file.write(fill + " ")
            file.write("0\n")     
            break

file.close()

