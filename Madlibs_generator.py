#this is madlibs generator

"""with open("story.txt","w") as f :
    f.write("hello world")      #permette d'ecrire dans le fichier en ecrasant ce qui existe s'il existe
"""
with open("story.txt ", "r") as f :
    story = f.read()            #permette de lire le fichier
#print(story)

words=set() #words=[] khedama mais ata3tina f lekher kelmat meawdin mais set kataeti dekshy unique
target_start="<"
target_end=">"
start =-1

for i,char in enumerate(story):
    if char==target_start:
        start=i
    if char==target_end and start!=-1 :
        word=story[start:i+1]
        words.add(word) #hnaya derna add hitesh khdemt b set mashi liste eadiya , donc add blasst append
        start=-1
#print(words)

answers={}  #hada dictionaire 
for word in words :
    answer=input("enter a word for"+ word + ":") #f input kandiro + mashi , 
    answers[word]=answer #hadi katajouti kola haja dekheltiha l dek lkelma li f text o kadir hadshi f dict
#print(answers)          # xxxx[yyyy] kataficher lik o lazedty dik  =zzz katstocker

for word in words :
    story=story.replace(word,answers[word]) #hna khassek darouri story=story.... hitesh ghir 
                                            #story.replace() makafyash , tachanger bla matastocker
print(story)                                            