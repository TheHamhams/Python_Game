import random

active = True
health = 3
questions = [["what is 2 + 2", ["4", ["3", "5"]]], ["What is 3 + 4", ["7", ["6", "8"]]]]
active_questions = questions

def game_start():
    print("You have entered the dungeon. Upon entering each room you must choose the door with the correct answer to each  questions in the hopes of reaching the treasure before you reach your doom!")
    start = input("Are you prepared? (yes/no)").lower()
    if start == "yes":
        print("Then lettuce begin! (yeah, it's one of those kind of games...)")
        next_question = active_questions[1]
        prompt("what is 2 + 2", "4", ["3", "5"])
    else:
        game_start()

def prompt(question, right, wrong_lst):
    answer_lst = [right, wrong_lst[0], wrong_lst[1]]
    random.shuffle(answer_lst)
    print(question)
    answer = input("door 1 = {}, door 2 = {}, door 3 = {} (enter door number for answer)".format(answer_lst[0], answer_lst[1], answer_lst[2]))
    if answer_lst[(int(answer) - 1)] == right:
        print("Great Job!")
    else:
        print("Ouch")
        health -= 1
        print(health) 

game_start()
