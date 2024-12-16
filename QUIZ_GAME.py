import os

# import the pandas
import pandas as pd

# count how many times this iteration happens
round_count=1

while (True):


    #==================================================================================================================
    #interface
    #==================================================================================================================

    print("")
    print(""*80)
    title="WELCOME TO THE QUIZ GAME - ALL SAINT COLLEGE"
    print(title.center(80))
    print(""*80)
    print("")
    print(" || Game Requirements || ".center(80))

    print('')
    print("1.  Eligibility: Only players aged 13-19 are eligible.")
    print('')
    print("2.  School Registration Number: Required for participation.")
    print('')
    print("3.  Game Mechanics: ")
    print('')
    print("       - Five rounds, each with one question. ")
    print('')
    print("       - Each correct answer allows access to the next question. ")
    print('')
    print("       - Each question is worth 20 points (total score of 100).  ")
    print('')
    print("4. Index No, Name and Age are compulsory. ")

    print("")
    print("-"*80)
    print("LET'S START THE GAME!!!".center(80))
    print("-"*80)
    print("")

    #==================================================================================================================
    # Check if there is a file named "GAME_SUMMARY"
    file_name="GAME_SUMMARY.csv"

    if (os.path.isfile(file_name)):
        data=pd.read_csv(file_name)
    else:

    # Initialize the DataFrame
        data = pd.DataFrame(columns=["Index No","Name","Age","Points"])

    #==================================================================================================================
    # user inputs- Reg No, Name & Age
    # Exception handling
    #==================================================================================================================
    
    try:
        indexno=int(input("Enter Your Index No* : ").strip())
    except ValueError:
        print("")
        indexno=int(input("--Index number should be a number--\n\nEnter Your Index No* : ").strip())
    
    name=input("Enter Your Name*     : ").strip()
        
    try:
        age=int(input("Enter Your Age*      : ").strip())
    except ValueError:
        print("")
        age=int(input("--Age should be a number--\n\nEnter Your Age*      : ").strip())
    print("")

    #==================================================================================================================

    # count the questions(only 5 questions can be asked)
    q_count=1

    # check whether the user is teenager or not
    if (age>=13 and age<=19):

        # all the questions are randomly selected
        import random

        global points
        points=0
       
        ran_questions=[]
        while (q_count<=5):
            question_list=[ "Which scientist is known for the Theory of relativity?",
                    "Who is the author of the “Harry Potter” series?",
                    "Who painted the “Mona Lisa”?",
                    "Who won the FIFA World Cup in 2022?",
                    "Who is the CEO of Tesla?",
                    "Who played Iron Man in the Marvel Cinematic Universe?",
                    "What is the name of the tallest building in the world?",
                    "Which planet is known as the Red Planet?",
                    "What is the most popular social media platform in 2022?",
                    "What is the longest river in the world?",
                    "Who created Facebook?",
                    "Who is the author of “The Fault in Our Stars”?",
                    "What is another term for the number 0 in a game of cricket?",
                    "What is the coldest planet in our solar system?",
                    "What is the name of the largest ocean on earth?",
                    "Who is the CEO of Spotify?",
                    "Who is the music composer of “Titanic”?",
                    "What is the highest-grossing movie of all time?",
                    "How many bones are in the human body(In numbers)?",
                    "What is the largest animal on Earth?",
                    "What is the name of the highest mountain in Africa?",
                    "Which country has won the most FIFA World Cup titles?",
                    "Which country has won the most cricket World Cup titles?",
                    "Who was the youngest person to win a Nobel Prize?",
                    "What is the most common letter in the English alphabet",
                    "Which animal has the largest brain compared to its body size?",
                    "What’s the rarest blood type?",
                    "How many sides does a hexagon have(In numbers)?",
                    "Who was the first African U.S. president?",
                    "What city was the first to be attacked with an atomic bomb?",
                    "Which animal sleeps standing up?",
                    "Which animal has the longest lifespan in the world?",
                    "Which social media app is known for its “ghost” logo?",
                    "Which car company is known for the slogan “The Ultimate Driving Machine”?",
                    "Which company owns Lamborghini, Ducati, Porsche, Audi and Bugatti?",
                    "Who is known as the 'Father of the Nation' in India?",
                    "Which famous detective was created by Arthur Conan Doyle?",
                    "What is the name of the President of India?",
                    "Which country won the first-ever Cricket World Cup in 1975?",
                    "Which country is Mount Everest located in?",
                    "Name the largest organ in the human body?",
                    "What is the world’s smallest country?",
                    "How many Harry Potter films have been made (in numbers )?",
                    "The place where Jesus was born?",
                    "Which festival is known as the festival of colors?",
                    "What country first granted women the right to vote?",
                    "What is the best-selling book series of the 21st century?",
                    "Who is the highest-paid football player of all time?",
                    "Who was the first woman to become Prime Minister of India?",
                    "Which country is known for originating the sport of cricket?"]



            Answer_list=["Albert Einstein","J.K.Rowling","Leonardo Da Vinci","Argentina","Elon Musk","Robert Downey Jr","Burj Khalifa","Mars","Instagram","Nile","Mark Zuckerburg","John Green","Duck","Neptune","Pacific","Daniel Ek","James Horner","Avengers Endgame","206","Blue Whale","Kilimanjaro","Brazil","Australia","Malala Yousafzai","E","Ant","AB Negative","6","Barack Obama","Hiroshima","Horse","Tortoise","Snapchat","BMW","Volkswagen","Mahatma Gandhi","Sherlock Holmes","Ram Nath Kovind", "West Indies","Nepal","Skin","Vatican","8","Bethlehem","Holi","New Zealand","Harry Potter","Lionel Messi","Indira Gandhi","England"]

            # choose a question randomly.    
            ran_question=random.choice(question_list)

            # index of selected question is equal to the index of the answer.
            index=question_list.index(ran_question)
            Answer=Answer_list[index]


            #--------------------------------------------------------------------------------------------------------------
            # this execution is for avoid repeating the same question in a round
            #--------------------------------------------------------------------------------------------------------------

            if (ran_question in ran_questions):
                random_question=random.choice(question_list)
            else:
                random_question=ran_question

            ran_questions.append(ran_question)
            
            #--------------------------------------------------------------------------------------------------------------
            # funtion - is for execute the questions and answers
            #--------------------------------------------------------------------------------------------------------------

            
            def game(question,Answer):
                global points

                print("~-"*40)
                question_display=f"{name}, Your question {q_count}"
                print(question_display.center(80))
                print("~-"*40)
                print("")
                print(question)
                
                user_input=input("Enter the answer: ").strip()

                #----------------------------------------------------------------------------------------------------------
                # check whether user answer is correct or not
                #----------------------------------------------------------------------------------------------------------

                if (user_input.lower()==Answer.lower()):
                    print("")
                    print(f"{name.upper()}, CONGRATULATIONS!!! YOUR ANSWER IS CORRECT".center(80))
                    print("")
                    
                    points=points+20
                    
                    return True # continue the loop 
                else:
                    print("")
                    print(f"{name.upper()} , UNFORTUNATELY YOUR ANSWER IS INCORRECT".center(80))
                    print(f"The correct answer is ,{Answer}".center(80))
                    print(" ")
                    return False # exit the loop

            if not game(random_question,Answer):
                break # stop if the answer is incorrect

            q_count+=1

        #==================================================================================================================
        # Display the score of the Player

        print(":"*80)   
        print(f"YOUR TOTAL POINTS {points}".center(80))
        print("YOUR GAME IS OVER!!".center(80))
        print(":"*80)

        #----------------------------------------------------------------------------------------------------------
        # Check the file is empty or not
        #----------------------------------------------------------------------------------------------------------

        records=len(data.index)
        
           # if it is empty, initialize the dataframe
        if (records==0):
            data = pd.DataFrame(columns=["Index No","Name","Age","Points"])

            data=pd.concat([pd.DataFrame({"Index No": [indexno],"Name":[name],"Age":[age],"Points": [points]})])
            data.to_csv(file_name,index=False,header=True)

             # if not :
        elif(records>0):
            data=pd.concat([pd.DataFrame({"Index No": [indexno],"Name":[name],"Age":[age],"Points": [points]})])
            data.to_csv(file_name,index=False,mode="a",header=False)

        
        #==================================================================================================================

        #----------------------------------------------------------------------------------------------------------   
        # Ask the player to replay the game
        #----------------------------------------------------------------------------------------------------------

        print("")

        #----------------------------------------------------------------------------------------------------------
        # Use a loop until gets a valid input
        #----------------------------------------------------------------------------------------------------------
        
        while True:
            opinion = input("Do you want to replay (yes/no)? ")
            if opinion.lower() not in ("yes","no"):
                print("Invaild input. Please type 'yes' or 'no'.")
                print("")
            else:
                break
        
        print("")

        
        if (opinion.lower()=="no"):
            print("")
            print("."*80)
            print("See you, next time!!!".center(80))
            print("."*80)
            break   

        elif (opinion.lower()=="yes"):
            round_count+=1
            continue  

    #======================================================================================================================

    #if the player is not a teenager.    
                        
    else:
      
        file_name="GAME_SUMMARY.csv"

        print("|| You are not a teenager, Better luck next time!!! ||".center(80))
        print("")

        #----------------------------------------------------------------------------------------------------------
        #check the file is empty or not
        #----------------------------------------------------------------------------------------------------------

        records=len(data.index)
        
        #----------------------------------------------------------------------------------------------------------
        #if it is empty, initialize the dataframe
        #----------------------------------------------------------------------------------------------------------

        if (records==0):
            data = pd.DataFrame(columns=["Index No","Name","Age","Points"])

            data=pd.concat([pd.DataFrame({"Index No": [indexno],"Name":[name],"Age":[age],"Points": '-'})])
            data.to_csv(file_name,index=False,header=True)

        #if not :
        elif(records>0):
            data=pd.concat([pd.DataFrame({"Index No": [indexno],"Name":[name],"Age":[age],"Points": '-'})])
            data.to_csv(file_name,index=False,mode="a",header=False)




        #----------------------------------------------------------------------------------------------------------
        # Use a loop until gets a valid input
        #----------------------------------------------------------------------------------------------------------
        
        while True:
            opinion = input("Do you want to replay (yes/no)? ")
            if opinion.lower() not in ("yes","no"):
                print("Invaild input. Please type 'yes' or 'no'.")
                print("")
            else:
                break
        
        print("") 

        if (opinion.lower()=="no"):
            print("."*80)
            print("See you, next time!!!".center(80))
            print("."*80)

            break   

        elif (opinion.lower()=="yes"):

            #round_count+=1
            continue       



    #====================================================================================================================      



print("")
print("Data has been written to ",file_name)
print("")

#----------------------------------------------------------------------------------------------------------
# Read and display the data
# Use a loop until gets a valid input
#----------------------------------------------------------------------------------------------------------
        
while True:
    opinion_2 = input("Do you want to display the Game Summary (yes/no)? ")
    if opinion_2.lower() not in ("yes","no"):
        print("Invaild input. Please type 'yes' or 'no'.")
        print(" ")
    else:
        break
        
#----------------------------------------------------------------------------------------------------------
# If there are duplicate values, this will work out. Remove all the duplicates.    
#----------------------------------------------------------------------------------------------------------

if (opinion_2.lower()=="yes"):
    df=pd.read_csv("GAME_SUMMARY.csv")
    new_df=df.drop_duplicates()
    new_df=pd.read_csv(file_name)
    print("")
    print("="*35)
    print(new_df.to_string(index=False))
    print("="*35)

    print("")

#----------------------------------------------------------------------------------------------------------
# All the non teenagers points will replace with 0
#----------------------------------------------------------------------------------------------------------

    new_df["Points"] = pd.to_numeric(new_df["Points"], errors="coerce").fillna(0)

    #----------------------------------------------------------------------------------------------------------
    # Sort the file
    #---------------------------------------------------------------------------------------------------------- 

    sorted_file=new_df.sort_values(by="Points",ascending=False)

    print(" Since there are no points for Non teenagers, it is replaces by 0. ".center(80))

    print("")

    #----------------------------------------------------------------------------------------------------------
    # Disply the sorted file
    #----------------------------------------------------------------------------------------------------------
    
    print("-"*80)
    print("SORTED FILE".center(80))
    print("-"*80)
    print("")
    print("="*35)
    print(sorted_file.to_string(index=False))
    print("="*35)

    print("")

    #----------------------------------------------------------------------------------------------------------
    # Display the highest score
    #----------------------------------------------------------------------------------------------------------

    max=new_df["Points"].max()
    if max>0:
        name_of_max=new_df['Name'][new_df["Points"]== new_df['Points'].max()]

        size_of_max_names=len(new_df['Name'][new_df["Points"]== new_df['Points'].max()])



        print("<>"*40)
        print(f"HIGHTEST SCORE - {max}".center(80))
        print("<>"*40)

        #----------------------------------------------------------------------------------------------------------
        # Print the player's name who got highest score
        #----------------------------------------------------------------------------------------------------------

        print("")
        print('.'*80)
        if (size_of_max_names==1):
            print(f"CONGRATULATIONS!!!  {name_of_max.to_string(index=False)}".center(80).upper())
        elif (size_of_max_names>1):
            names_list = ", ".join(name_of_max)
            print(f"CONGRATULATIONS!!!  {names_list}".center(80).upper())
        print("."*80)
        print("")
    else:
        print("<>"*40)
        print(f"NO HIGHTEST SCORE".center(80))
        print("<>"*40)
        print("")

print(" ")
#----------------------------------------------------------------------------------------------------------
# Asking the user to delete the records in the CSV file
#----------------------------------------------------------------------------------------------------------

while True:
    opinion_3 = input("Do you want to delete all the records (yes/no)? ")
    if opinion_3.lower() not in ("yes","no"):
        print("Invaild input. Please type 'yes' or 'no'.")
        print(" ")
    else:
        break

if (opinion_3.lower()=="yes"):
    new_df=new_df.iloc[0:0]
    new_df.to_csv(file_name,index=False)
    print("")
    print("All records have been deleted.".center(80))

else:
    print("")
    print("All records have not been deleted.".center(80))

#----------------------------------------------------------------------------------------------------------
# END.
#----------------------------------------------------------------------------------------------------------

print("")
    
