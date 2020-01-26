import random
print("Welcome to EXCUSE generator")
print("This is a generator that creates random Excuse for You")
print("What do you need an excuse for?")
print("1: I forgot")
print("2: I lost")
print("3: I didn't do")
QuestionOne = int(input())
if QuestionOne == 1:
    print("What did you Forgot?")
    print("1: Homework")
    print("2: An object")
    print("3: A concept")
    QuestionOneOne = int(input())
elif QuestionOne == 2:
    print("What did You Lose")
    print("1: Something expensive")
    print("2: Something cheap")
    print("3: Someone")
    QuestionOneTwo = int(input())
elif QuestionOne == 3:
    print("What didn't you do")
    print("1: Your homework")
    print("2: An errand")
    print("3: Something important")
    QuestionOneThree = int(input())
print("What is the specific name for this")
Thing = str(input())
ForgotExcusesList = ("brainwashed", "mind wiped", "electrocuted", "on Mars", "fighting Zeus", "killed in melee combat")
LostExcusesList = ("dissapeared", "popped out of existence", "exploded", "evaporated", "imploded", "turned to ashes", "flew into space", "was misplaced")
ToBlameList = ("an alien", "my freind", "my brother", "Superman", "a zombie", "you")
ToBlameDidList = ("flamethrowered", "bombed", "exploded", "impaled", "burnt", "altered")
TookList = ("stole", "took","grabbed", "seized", "snagged")
WhenList = ("Yesterday", "Last Year", "This Evening", "Last Hour")
ForgotExcuses = random.choice(ForgotExcusesList)
LostExcuses = random.choice(LostExcusesList)
ToBlame = random.choice(ToBlameList)
ToBlameDid = random.choice(ToBlameDidList)
Took = random.choice(TookList)
When = random.choice(WhenList)
if QuestionOne == 1:
    print("Your Excuse is: ")
    print("I FORGOT MY", Thing.upper(), "BECAUSE I WAS", ForgotExcuses.upper(), "AND" , ToBlame.upper(), "IT", When.upper(), "IT. ")

if QuestionOne == 2:
    print("Your excuse is:")
    print("MY", Thing.upper(), LostExcuses.upper(), "BECAUSE", ToBlame.upper(), Took.upper(), "IT", When.upper())
if QuestionOne == 3:
    print("I DIDN'T DO MY", Thing.upper(), "BECAUSE", ToBlame.upper(), Took.upper(), "IT AND", ToBlameDid.upper(),
          "IT SO UNTIL", When.upper(), "I DIDN'T HAVE IT")




