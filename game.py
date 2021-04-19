import random

starting_health = 2
health = starting_health
count = 1
questions = [
["Blue + Yellow =...", "Green", ["Orange", "Purple"]], 
["What is 3 + 4", "7", ["6", "8"]], 
["What is the capitol of Washington?", "Olympia", ["Seattle", "Tacoma"]], 
["What coding language does Unity primarily use?", "C#", ["JS", "Python"]], 
["What brand of table saw stops when it detects flesh?", "SawStop", ["Dewalt", "Craftsman"]],
['The game series "Monster Hunter" is made by what company?', "Capcom", ["Blizzard", "Konami"]],
["Funko headquarters are located in which city?", "Everett, WA", ["San Fransisco, CA", "New York"]],
["What is the 7th planer from the sun?", "Neptune", ["Uranus", "Saturn"]],
['What color does "B" represent in Magic the Gathering?', "Black", ["Blue", "Burgandy"]],
['The movie "Gentleman Broncos" focuses around a book written by the protagonist called...', "Yeast Lords", ["Cybor Harpies", "Blood Custard"]]
]
active_questions = questions

def game_start():
    global active_questions
    global starting_health
    global health
    health = starting_health
    print("""
    You have entered the dungeon. Upon entering each room you must choose the door with the correct answer to each  questions in the hopes of reaching the treasure before you reach your doom!
    """)
    start = input("Are you prepared? (yes/no)").lower()
    if start == "yes":
        print("Then lettuce begin!")
        next_prompt()
    else:
        game_start()

def prompt(question, right, wrong_lst):
    global count
    answer_lst = [right, wrong_lst[0], wrong_lst[1]]
    random.shuffle(answer_lst)
    print("\n" + question + "\n")
    answer = input("door 1 = {}, door 2 = {}, door 3 = {} (enter door number for answer)".format(answer_lst[0], answer_lst[1], answer_lst[2]))
    if answer_lst[(int(answer) - 1)] == right:
        print("""
        Great Job!
        """)
        count += 1
        if count < 10:
            next_prompt()
        if count == 10:
            victory()
    else:
        global health
        health -= 1
        print("""
        Ouch!
        Health remaining: {}
        """.format(health))        
        if health > 0:
            count += 1
            if count == 10:
                victory()
            else:
                next_prompt()
            
        else:
            game_over()

def next_prompt():
    if len(active_questions) > 1:
        next = random.randrange(0, (len(active_questions) - 1))
    else:
        next = 0
    next_question = active_questions[next]
    active_questions.pop(next)
    prompt(next_question[0], next_question[1], next_question[2])

def game_over():
    restart = input("Game Over! would you like to try again? (yes/no)").lower()
    if restart == "yes":
        game_start()
    elif restart == "no":
        print("Thanks for playing, bye bye!")
    else:
        game_over()

def victory():
    print("\n" + "Congradulations! You made it to the treasure!" + "\n")
    restart = input("Would you like to play again? (yes/no)" + "\n")
    if restart == "yes":
        game_start()
    else:
        print("Thanks for playing, don't spend the treasure all at one shope!")
        exit()

game_start()
