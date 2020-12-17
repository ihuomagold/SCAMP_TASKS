import functions

functions.create_database()
choice = -1

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
elif choice == 5:
    functions.update_lastname()
elif choice == 6:
    functions.update_age()
elif choice == 7:
    functions.update_email()
elif choice == 8:
    functions.update_username()
elif choice == 9:
    functions.update_course()
else:
    print("Invalid Option!")
