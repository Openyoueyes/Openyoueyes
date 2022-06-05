current_users = ['johN', 'Eric', 'Petr', 'ILya']
new_users = ['John', 'Vano', 'eric', 'Jamshood']
 
for user in new_users:
    if user.lower() in [i.lower() for i in current_users]:
        print(user + " :already exists")
    else:
        print(f"{user}: login free")