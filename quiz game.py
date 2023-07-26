#the of the game is asking questions to the player and at the end showing how many true and false answers given.
#first let's define the function for the list of questions


def questions():
    score = 0 # to keep track of true answers
    i = 0 #to increment questions one by one
    j = 0 #to increment answers one by one
    while i<=9: #total number of questions
        with open('quiz_questions.txt', 'r') as qq: #read questions file
            content = qq.readlines() #read lines from the file
            for content[i] in content: #loop for lines
                print(content[i].strip()) #stripping \n from questions
                i+=1
                answer = input('Enter your answer: ') #take answer
                with open('answers.txt', 'r') as aw: #open answers file
                    answers = aw.readlines() #read lines from the file
                    if answer.lower() == answers[j].strip(): #check if given answer is true
                        score += 1
                        print(f'True! {answers[j].strip()} is the answer!')
                        j += 1

                    else:
                        print(f'Wrong! True answer is {answers[j].strip()}.')
                        j += 1
    return f'Your score is {score}. Congratulations!'

playing = input('Would you like to play? (Y/N)')
if playing.lower() == 'y':
    questions()
else:
    pass