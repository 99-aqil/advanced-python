class Animal():

    def sleep(self):
        print("I sleep while leaning")

    def eat(self):
        print("I eat food")

    def height(self):
        print("I have a height")

class Horse(Animal):
    def sleep(self):
        print("I sleep while standing up")

class Dog(Animal):
    def sleep(self):
        print("I sleep while lying down")

class Snake(Animal):
    def sleep(self):
        print("I just sleep")


h = Horse()
d = Dog()
s = Snake()

h.sleep()
d.sleep()
s.sleep()
