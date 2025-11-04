class robot:
    name = "Robz_67"
    age = "18 years ago"
    workplace = "Nasa"
    department = "Astronomy"
    planet = "Mars"
    def introduction(self):
        print("Hi, I am an intelligent robot!")
    def details(self):
        print("My name is", self.name)
        print("I was made", self.age)
        print("I work for", self.workplace)
        print("My specific department is", self.department)
        print("The planet I work on is", self.planet)
ob = robot()
ob.introduction()
ob.details()