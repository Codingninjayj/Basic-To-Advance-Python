#create a program of displaying question to user like kbc
#use list data type to store the question and their correct answer
#display the final amount the person is taking home after playing the game 
prize_money=0
print("WELCOME TO Kaun Banega Crorepati")
# y=print(input("Are you intrsented in playing the game(Y/N):"))
# if (y=="yes"):
questions = [{
   "question": "What is the capital of India?",
   "options": ["1. Delhi", "2. Mumbai", "3. Kolkata", "4. Chennai"],
   "answer": 1
}]
for question in questions:
   print(question["question"])
   for option in question["options"]:
      print(option)

user_ans=int(input("Enter your answer(option number):"))
if(user_ans==question["answer"]):
   print("Correct Answer!!")
   prize_money+=1000

else:
   print("wrong answer!!")
   break 
print("prize money:",prize_money)