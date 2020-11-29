import functions

choice = -1
# while choice is not 0:
while choice < 0 or choice > 4:
    choice = functions.ask()
if choice == 1:
    functions.add_users()
elif choice == 2:
    functions.delete_record()
