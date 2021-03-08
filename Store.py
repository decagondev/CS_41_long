from Department import Department

class Store:
    # attributes
    # name
    # departments
    def __init__(self, name, departments):
        self.name = name
        self.departments = departments
    def __str__(self):
        output = f"{self.name}\n"
 
        for i, dept in enumerate(self.departments):
            output += " " + str(i + 1) + ". " + dept.name + "\n"
        
        output += f" {i + 2}. Exit"





        return output



    def __repr__(self):
        return f'Store("{self.name}", {self.departments})'


# instance of the Store class
my_store = Store("Bobs Emporium", [Department("Clothes"), Department("Tools"), Department("Electronics"), Department("Bobs Specials")])

# print(repr(my_store))
# make a variable to hold the users choice?
choice = 0
while choice != len(my_store.departments) + 1:

    # print out the menu
    print(my_store)

    # request input from the user
    choice = int(input("Select the number of department you wish to enter. "))
    if choice == len(my_store.departments) + 1:
        print(f"Thanks for shopping at {my_store.name}")
        break
    elif choice > 0 and choice <= len(my_store.departments):
        # print the users choice
        print(f"{my_store.departments[choice - 1]}")
    else:
        print(f"Please choose a valid number between [1] and [{len(my_store.departments) + 1}]")
    