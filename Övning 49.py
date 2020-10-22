# Förståelse kring objektorientering genom djur och deras läten, egenskaper
import random


class Dog:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(f"{self.name}: Woff!")

    def make_trick(self):
        tricks = ['roll', 'sit', 'jump']
        print(f"{self.name}: making trick {random.choice(tricks)}")


class Cat:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(f"{self.name}: Mjau!")

    def make_trick(self):
        print(f"{self.name}: Cat's don't make tricks on demand!")


# TODO: implement parrot's methods
class Parrot:

    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(f"{self.name}: {self.name} wants a cracker!")

    def make_trick(self):
        print(f"{self.name}: Sings a song")


def play_with_animals():
    hund = Dog("Rufus")
    hund.make_sound()
    hund.make_trick()
    hund9 = hund
    cat = Cat("Cecilia")
    cat.make_sound()
    cat.make_trick()
    bird = Parrot("Polly")
    bird.make_sound()
    bird.make_trick()


if __name__ == '__main__':
    play_with_animals()
