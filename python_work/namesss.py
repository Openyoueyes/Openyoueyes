import json

def get_stored_username():
    #"" "Если имя пользователя сохранено, получите его" ""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
   # "" "Предложите пользователю ввести имя пользователя" ""
    username = input("What is your name?")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
   # "" "Приветствие пользователя и указание его имени, вопрос о том, сам ли он, или повторное ввод имени пользователя" ""
    username = get_stored_username()
    if username:
        answer = input("Is this your username?(y/n)\n" + username + "\n")
        if answer == "y":
            print("Welcome back, " + username + "!")
        else:
            username = get_new_username()
            print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")

get_new_username()
get_stored_username()
greet_user()