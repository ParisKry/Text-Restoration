sf = open("story_mod.txt.IB1.O.gr.k1.out.collectedgbr", "r")
f = open("story_unmerged_gutenberg_brown_reuters.txt", "w+")
story = ""

for word in sf:
   story += (word.rstrip("\n") + " ")

f.write(story)
