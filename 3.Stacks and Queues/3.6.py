# -*- coding: utf-8 -*-

"""
Question 3.6:
    Animal Shelter: An animal shelter, which holds dogs and cats, operates on a strictly "first in,first out" basis.
                    People must adopt either oldest of the animals at the shelter or they can select whether they would
                    prefer a dog or a cat. they can not select which specific animal they would like create the data
                    structures to maintain which system and implement operations such as enqueue, dequeueAny, dequeueDog
                    and dequeueCat.You may use the build-in LinkedList data structure.
"""


class Node:
    def __init__(self, animal, next):
        self.animal = animal
        self.next = next


class Animal:
    def __init__(self):
        self.val = 0

    def set_val(self, val):
        self.val = val


class Dog(Animal):
    pass


class Cat(Animal):
    pass


class Shelter:
    def __init__(self):
        """
        Take O(n) space
        """
        self.cats = Node(Cat(), None)
        self.dogs = Node(Dog(), None)
        self.flag = 0

    def enqueue(self, animal):
        """
        Take O(n) time
        :param animal: Input Animal
        :return: None
        """
        self.flag += 1
        if isinstance(animal, Dog):
            d = Dog()
            d.set_val(self.flag)
            temp = self.dogs
            while temp.next:
                temp = temp.next
            temp.next = Node(d, None)
        elif isinstance(animal, Cat):
            c = Cat()
            c.set_val(self.flag)
            temp = self.cats
            while temp.next:
                temp = temp.next
            temp.next = Node(c, None)
        else:
            raise Exception('Enqueue Error !')

    def dequeueAny(self):
        """
        Take O(1) time
        :return: None
        """
        if self.cats.animal.val == 0:
            self.cats = self.cats.next
        if self.dogs.animal.val == 0:
            self.dogs = self.dogs.next
        if self.dogs.animal.val < self.cats.animal.val:
            print('Dog Dequeue')
            self.dogs = self.dogs.next
        else:
            print('Cat Dequeue')
            self.cats = self.cats.next

    def dequeueDog(self):
        """
        Take O(1) time
        :return: None
        """
        print('Dog Dequeue')
        self.dogs = self.dogs.next

    def dequeueCat(self):
        """
        Take O(1) time
        :return: None
        """
        print('Cat Dequeue')
        self.cats = self.cats.next


if __name__ == '__main__':
    s = Shelter()
    s.enqueue(Dog())
    s.enqueue(Cat())
    s.enqueue(Dog())
    s.enqueue(Cat())
    s.enqueue(Cat())
    s.enqueue(Cat())
    s.enqueue(Dog())
    s.dequeueAny()
    s.dequeueAny()
    s.dequeueCat()
    s.dequeueDog()
