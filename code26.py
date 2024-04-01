questions=[[
  
"Which language is used to create fb?","pyhton","French","javascript","php",4],

[
  
"who created fb?","jeff ","eiston","elon","mark",4],

[
  
". Which type of Programming does Python support?","object-oriented programming","structured programming","functional programming"," all of the mentioned",4],

[
  
"Is Python case sensitive when dealing with identifiers?","no","yes","machine dependent","none of the mentioned",2],
[
  
"Which of the following is the correct extension of the Python file?","pyhton","French","javascript","php",3],
[
  
"All keywords in Python are in _________"," Capitalized","lower case","UPPER CASE","None of the mentioned",4]
]
levels=[1000,2000,3000,5000,10000,20000,40000,80000,100000,320000]

i=0
money=0
for i in range(0,len(questions)):
    print(len(questions))
    question =questions[i]
    # print(question[0])
    print(f"Question for rs,{levels[i]}")
    print(f"a.{question[1]}             b.{question[2]}")
    print(f"c.{question[3]}             d.{question[4]}")
    reply=int(input("Enter your choose(Form Option):"))
    if reply==question[-1]:
        print("Correct Answer!! ,you have won ",levels[i])
        if(i==4):
            money=1000
        elif(i==9):
            money=32000
        elif(i==14):
            money=100000
    else:
        print("wrong answer!!")
        break 
print(f"Your take home money is{money}")