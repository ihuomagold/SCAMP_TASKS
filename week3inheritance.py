class Person:
    def __init__(self, name, age, weight, height):
        self.__name = name
        self.__age = age
        self.__weight = weight
        self.__height = height

# The following methods are mutators for the class's data attributes
    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_weight(self, weight):
        self.__weight = weight

    def set_height(self, height):
        self.__height = height

#  The following methods are accessors for the class attributes
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_weight(self):
        return self.__weight

    def get_height(self):
        return self.__height


class Steph(Person):
    def __init__(self, name, age, weight, height, complexion):
        Person.__init__(self, name, age, weight, height)
        self.__complexion = complexion

# Mutator for the complexion attribute
    def set_complexion(self, complexion):
        self.__complexion = complexion

# Accessor for the complexion attribute
    def get_complexion(self):
        return self.__complexion


class Nasa(Person):
    def __init__(self, name, age, weight, height, race):
        Person.__init__(self, name, age, weight, height)
        self.__race = race

# Mutator for the race attribute
    def set__race(self, race):
        self.__race = race

# Accessor for the complexion attribute
    def get_race(self):
        return self.__race


def main():
    nasa_details = Nasa("Chinasa", 21, "65kg", "1.63m", "Black")
    print("Chinasa's Details:")
    print("---------------------")
    print("Name:", nasa_details.get_name())
    print("Age:", nasa_details.get_age())
    print("Weight:", nasa_details.get_weight())
    print("Height:", nasa_details.get_height())
    print("Race:", nasa_details.get_race())
    print()


main()


def main():
    steph_details = Steph("Stephanie", 25, "135lbs", "1.56m", "Light skinned")
    print("Stephanie's Details:")
    print("---------------------")
    print("Name:", steph_details.get_name())
    print("Age:", steph_details.get_age())
    print("Weight:", steph_details.get_weight())
    print("Height:", steph_details.get_height())
    print("Complexion:", steph_details.get_complexion())


main()
