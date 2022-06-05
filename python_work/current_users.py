current_users = ['Ilya','DiAna','Svetlana',
				 'Denis','Alexander','Michel','admin']
current_users = [i.lower() for i in current_users]
new_users = ['Ilya', 'DIANA', 'Petr', 'Andrey', 'Dima']
new_users = [i.lower() for i in new_users]
for new_users in new_users:
	if new_users in current_users:
		print('Name ' + new_users.title() + ' is busy, please enter new name')
	else:
		print('Name ' + new_users.title() + ' is free')

