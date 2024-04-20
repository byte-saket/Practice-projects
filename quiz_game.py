print("Welcome to quiz game?")

question = input("Do you wanna play? ")

if question.lower() != "yes":
    quit()

print(" okay! let's play😊 ")
score = 0

ans = input("Full form of cpu? ")
if ans.lower() == "central processing unit":
    print("you are correct")
    score+=1
else:
    print("you are incorrect") 

ans = input("What does RAM stand for? ")   
if ans.lower() == "random access memory":
    print("you are correct")
    score+=1
else:
    print("you are incorrect") 

ans = input("Full form of gta? ")
if ans.lower() == "grand theft auto":
    print("you are correct ")
    score += 1
else:
     print("you are incorrect") 

ans = input("Full form of ROM? ")
if ans.lower() == "read only memory":
    print("you are correct")
    score += 1
else:
     print("you are incorrect") 

print("Your score is" + str(score) + "questions correct")
percentage_score = (score/3) * 100
print(f"you got {percentage_score : .2f}% ")




