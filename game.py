active = True
health = 3
questions = [["what is 2 + 2", [4, [3, 5]]], ["What is 3 + 4", [7, [6, 8]]]]

def game_start():
    print("You have entered the dungeon. Upon entering each room you must choose the door with the correct answer to each  questions in the hopes of reaching the treasure before you reach your doom!")
    start = input("Are you prepared? (yes/no)").lower()
    if start == "yes":
        print("Then lettuce begin! (yeah, it's one of those kind of games...)")
    else:
        game_start()



game_start()
