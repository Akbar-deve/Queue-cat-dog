#writting a program queue which contains the list of cats and dogs

#Creating a class called animal which cantains cat and dog queue
class animal:
    def __init__(self):
        #Declearing a cat and dog queues
        self.cats=[]
        self.dogs=[]
    
    # Enqueuing the animal to queue depends on the type of animal (cat or dog) 
    def animal_enqueue(self,animal,type):
        if type=='cat':
            self.cats.append(animal)
        else:
            self.dogs.append(animal)

    #dequeue the cat only 
    def catsdequeue(self):
        if len(self.cats)==0:
            print("no cats to dequeue ")
        else:
            print(self.cats.pop(0))
    
    ##dequeue the dog only 
    def dogsdequeue(self):
        if len(self.dogs)==0:
            print('no dogs to dequeue')
        else:
            print(self.dogs.pop(0))
    
    #dequeuing the animal if cat is present it remove the cat else dog will be removed 
    def animal_dequeue(self):
        if len(self.cats)==0:
            print(self.dogs.pop(0))
        else:
            print(self.cats.pop(0))

    #Displaying the both queues of the class
    def display(self):
        print("Displaying both the DOG and CAT Queues--->")
        print(self.cats)
        print(self.dogs)

#creating the object of class animal

a=animal()

while True:
    print('Select the option to perform \n')
    print("1.animalenqueue\n2.cat-dequeue\n3.dog-dequeue\n4.animal-dequeue\n5.display\n")
    opt=int(input("enter the option to perform--> "))
    match opt:
        case 1:
            animal=input('enter animal name to enqueue -->')
            type=input("enter animal type to enqueue--> ")
            a.animal_enqueue(animal,type)
        case 2:
            a.catsdequeue()
        case 3:
            a.dogsdequeue()
        case 4:
            a.animal_dequeue()
        case 5:
            a.display()
        case _:
            print("enter correct option ")