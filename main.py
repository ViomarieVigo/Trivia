##### THIS IS  Custom Trivia########################


##### QUESTION ZONE ###############################################

question1 = ("\nWould you like to know a little about me ?")
question2 = ("\nWould you like to know why I am Applying?")
question3 = ("\nYou might be thinking why hire her?")
question4 = ("\nWould you like to know where i see my self in 5 years?")
question5 = ("\nWhat about outside of Tech?, What do I when i have time to myself?")

    
##### this is the list   questions

questions = [question1, question2, question3, question4, question5]


##### ANSWER ZONE ################################################

answer1 = ("yes")
answer2 = ("yes")
answer3 = ("yes")
answer4 = ("yes")
answer5 = ("yes")

##### this is the list answers

answers = [answer1, answer2, answer3, answer4, answer5]


###### REASONS WHY ZONE######################

reason1 = ("My name is Viomarie N. Vigo Osorio, I am a student at The University of Tampa and an aspiring IT professional.\n I am orginized, motivated, and eager to learn")
reason2 = ("I have always had a strong desire to know as much about technology as possible. I have loved growing up and being able to learn new technologies and how they work. So I know the Tech industry is where I belong.\nI am detail oriented and enjoy looking for ways to increase productivity")
reason3 = ("I am 'first- generation' in all aspects of my life and so i have had to develope a strong worth ethic and a even greater desire to do something great! I am looking for a company in which I can contribute my skills and passion towards the next step in innovation.\nI am do well in adapting to new enviornments and skills")
reason4 = ("I’m really excited by this position because in five years, I’d like to be seen as someone with deep expertise in the Informational technology sector, and I know that’s something that I would have an opportunity to do here. I would also be looking to take on more managerial responsibilities over the course of those 5 years and potentially even take the lead on some projects. \nI have great verbal and written")
reason5 = ("I enjoy a few different hobbies ranging from playing the guitar to hammocking. I enjoy crafting and building furniture and other home decor. I enjoy creating both digitally and physically.\nI have experience in Network security and several frameworks")




######## this is the list of reasons ######

reasons = [reason1, reason2, reason3, reason4, reason5 ]

##### GLOBAL GAME SETTINGS ###############################################


points = 0
name = None
yes = ['Yes', 'yes', 'YES']
no = ['No', 'no', 'NO']


##### RESET ZONE #########################################################


def game_reset():

    global points
    global name

    points = 0
    name = None
#end-function#
    

##### GAME INTRO ZONE ####################################################


def game_intro():

    print("\n ******** !! Welcome to Trivia !! ******** \n")
    
    global name

    while name == None:
        name = input("Hi there, What is your name? ")
        print("\nNice to meet you "+ name +", are you ready to play?")
        correct = input("\nYes or No? ")
        if yes.count(correct) == True: ##"Yes" or Y == "yes" or y == "YES":
            print("\nIt's a pleasure to meet you "+name+ ",let's go on!\n")
        else:
            print("Mh? Try again and confirm with Yes!")
            name = None
#end-function#
            

##### GAME PLAY ZONE #####################################################


def print_play_status(x):

    global points
    print("-------------------------------------------------")
    print("  At the moment your total points are: "+str(int(points)))
    print("\n         Challenge Level: "+ str(int(x+1)))
#end-function#
    

def play_quest(x):
    
    global points
    answerPlayer = input(questions[x]).lower()
    if answerPlayer == answers[x]:
        print("\nGreat, well "+ name + ": \n")
        points +=10
        print(reasons[x])
    else:
        print("Understood! on to the next question...\n")
#end-function#
        

def game_play():
    for x in range(len(questions)):
        print_play_status(x)
        play_quest(x)
#end-function#


##### GAME END ZONE ########################################################


def game_end():

    print("\nYou finished the game with a total of "+ str(int(points)) + "points! \n")

    again = None
    
    while again == None:
        again = input("One more time? ")
        if yes.count(again) == True:
            print("\nEnjoy :)\n")
            game_control()
        elif no.count(again) == True:
            print("                             Thanks for playing!")
            print("       ************ I look forward to hearing from you!  ************")
        else:
            print("Sorry only yes or no responses")
            again = None
#end-function#
        
    
##### GAME CONTROL ZONE ####################################################


def game_control():
    game_reset()
    game_intro()
    game_play()
    game_end()
#end-function#


##### FIRST GAME START ZONE ################################################


game_control()
