import functions

functions.create_database()
choice = -1
# # while choice is not 0:
while choice < 0 or choice > 4:
    choice = functions.ask()
if choice == 1:
    functions.add_users()
elif choice == 2:
    functions.list_all()
elif choice == 3:
    functions.delete_record()
elif choice == 4:
    functions.update_firstname()
