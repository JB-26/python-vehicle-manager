#OOP practice
#import time module
import datetime
#import os module
import os
# base Vehicle class
class Vehicle():
    def __init__(self, registration, brand, model, vehicleType):
        '''
        Initialise object
        '''
        self.brand = brand
        self.model = model
        self.registration = registration
        self.vehicleType = vehicleType
        self.dateCreated = datetime.datetime.now()
        self.inGarage = True

# inherits Vehicle class
class Car(Vehicle):
    def __init__(self, brand, model, wheels, doors, engineType, year, registration):
        '''
        Initialise object
        '''
        try:
            Vehicle.__init__(self, registration, brand, model, 'Car')
            self.wheels = int(wheels)
            self.doors = int(doors)
            self.engineType = engineType
            self.year = year
        except(ValueError):
            print("Whoops! Something went wrong! Error details: ValueError")
    
    def __str__(self):
        '''
        Display details of a car
        '''
        try:
            return f'Vehicle details:\nVehicle Type: {self.vehicleType}\nBrand: {self.brand}\nModel: {self.model}\nNumber of wheels: {self.wheels}\nNumber of doors: {self.doors}\nEngine Type: {self.engineType}\nYear: {self.year}\nRegistration: {self.registration}\nIn garage: {self.inGarage}\nDate added: {self.dateCreated}'
        except:
            print("Your car doesn't look right! Please edit the details and try again!")
    
    def info(self):
        '''
        Returns info on the car
        '''
        try:
            return f'Vehicle details:\nVehicle Type: {self.vehicleType}\nBrand: {self.brand}\nModel: {self.model}\nNumber of wheels: {self.wheels}\nNumber of doors: {self.doors}\nEngine Type: {self.engineType}\nYear: {self.year}\nRegistration: {self.registration}\nIn garage: {self.inGarage}\nDate added: {self.dateCreated}'
        except:
            print("Your car doesn't look right! Please edit the details and try again!")

# inherits Vehicle class
class Motorbike(Vehicle):
    def __init__(self, registration, brand, model, wheels, engineType, year):
        '''
        Initialise object
        '''
        try:
            Vehicle.__init__(self, registration, brand, model, 'Motorbike')
            self.wheels = wheels
            self.engineType = engineType
            self.year = year
        except(ValueError):
            print("Whoops! Something went wrong! Error details: ValueError")
        
    def __str__(self):
        '''
        Display details of a motorbike
        '''
        try:
            return f'Vehicle details:\nVehicle Type: {self.vehicleType}\nBrand: {self.brand}\nModel: {self.model}\nNumber of wheels: {self.wheels}\nEngine Type: {self.engineType}\nYear: {self.year}\nRegistration: {self.registration}\nIn garage: {self.inGarage}\nDate added: {self.dateCreated}'
        except:
            print("Your motorbike doesn't look right! Please edit the details and try again!")
    
    def info(self):
        '''
        Returns info on the motorbike
        '''
        try:
            return f'Vehicle details:\nVehicle Type: {self.vehicleType}\nBrand: {self.brand}\nModel: {self.model}\nNumber of wheels: {self.wheels}\nEngine Type: {self.engineType}\nYear: {self.year}\nRegistration: {self.registration}\nIn garage: {self.inGarage}\nDate added: {self.dateCreated}'
        except:
            print("Your motorbike doesn't look right! Please edit the details and try again!")


# Garage class
class Garage():
    def __init__(self):
        '''
        Initialise object
        '''
        self.garage = []

    def __str__(self):
        '''
        Print details for all the vehicles in the garage
        '''
        for vehicle in self.garage:
            print(vehicle)
            print('\n')
        return'\n'

    def __len__(self):
        '''
        For returning the number of vehicles in the garage
        '''
        return len(self.garage)
    
    def __iter__(self):
        '''
        Makes the garage list iterable
        '''
        return iter(self.garage)
    
    def numberOfvehicles(self):
        '''
        Print the number of vehicles in the garage
        '''
        print(f'You have {len(self.garage)} vehicles in the garage.')

    def addVehicleToGarage(self, vehicle):
        '''
        Adds a vehicle to the garage (list)
        '''
        self.garage.append(vehicle)
    
    def findAVehicle(self, reg):
        '''
        Takes a string (registration) and attempts to find an item in the list that matches it
        '''
        vehicleFound = False
        for vehicle in self.garage:
            if reg == vehicle.registration:
                print(vehicle)
                vehicleFound = True
                break
            else:
                pass
        if vehicleFound == False:
            print(f'No vehicle could be found with registration {reg}')
    
    def writeToFile(self):
        '''
        Method to print all vehicles information to a text file
        '''
        file = open('vehicle_log.txt', 'w')
        file.write(f'File created on {datetime.datetime.now()}\n')
        for vehicle in self.garage:
            text = vehicle.info()
            file.write(text+'\n\n')
        file.close()

    def writeOneVehicleToFile(self):
        '''
        Method to print one vehicle information to a text file
        '''
        while True:
            vehicleFound = False
            print('Enter the registration of the vehicle you want to write to a file')
            vehicleReg = input('Registration - ')
            for vehicle in self.garage:
                if vehicleReg == vehicle.registration:
                    fileName = f'{vehicle.registration}_info.txt'
                    print(f'File will be called {fileName}')
                    file = open(f'{fileName}', 'w')
                    file.write(f'File created on {datetime.datetime.now()}\n')
                    text = vehicle.info()
                    file.write(text+'\n')
                    file.close()
                    vehicleFound = True
                    return fileName
                else:
                    pass
            if vehicleFound == False:
                print('No vehicle could be found, please try again!')
    
    def deleteAllVehicles(self):
        '''
        Deletes all the items in the list
        '''
        print('Now removing all vehicles from the garage....')
        del self.garage[:]
        print('Complete!')
    
    def deleteSingleVehicle(self):
        '''
        Deletes a single item from the list that the user specifies
        '''
        print('Please enter the registration of the vehicle you want to delete from the garage.')
        reg = input('Registration - ')
        count = 0
        vehicleDeleted = False
        for vehicle in self.garage:
            if reg == vehicle.registration:
                del self.garage[count]
                print(f'{reg} - has been deleted')
                vehicleDeleted = True
                break
            else:
                count += 1
        if vehicleDeleted == False:
            print(f'No vehicle with registration {reg} could be found!')
        else:
            pass
    
    def isInGarage(self):
        '''
        Changes the bool value for inGarage attribute for a vehicle
        '''
        vehicleFound = False
        print('Enter the registration of the vehicle to retrieve status of the vehicle')
        reg = input('Enter registration - ')
        for vehicle in self.garage:
            if reg == vehicle.registration:
                vehicleFound = True
                print(f"The current status of the vehicle is {vehicle.inGarage}")
                status = vehicle.inGarage
                if status == True:
                    while True:
                        print('Do you want to change the status to False? (Vehicle is NOT in the garage)\nEnter (Y)es or (N)o')
                        boolean = input('Input - ').upper()
                        if boolean == 'Y':
                            vehicle.inGarage = False
                            print(f'{reg} updated to False')
                            break
                        elif boolean == 'N':
                            print(f'{reg} not updated')
                            break
                        else:
                            print("I don't understand that - please try again!")
                else:
                    while True:
                        print('Do you want to change the status to True? (Vehicle is IN the garage)\nEnter (Y)es or (N)o')
                        boolean = input('Input - ').upper()
                        if boolean == 'Y':
                            vehicle.inGarage = True
                            print(f'{reg} updated to True')
                            break
                        elif boolean == 'N':
                            print(f'{reg} not updated')
                            break
                        else:
                            print("I don't understand that - please try agin!")
            else:
                pass
        if vehicleFound == False:
            print(f'Vehicle {reg} could not be found!')
        

def registerVehicle():
    '''
    Getting input from a user to determine what vehicle they want to register
    '''
    while True:
        print("Do you want to register a car or a motorbike?\nType 'C' for Car or 'M' for Motorbike")
        select = input('Please enter: ').upper()
        if select == 'C':
            registerCar()
            break
        elif select == 'M':
            registerMotorbike()
            break
        else:
            print("I don't understand that, try again!")

def vehicleNum():
    '''
    When variable is going to be an int - function ensures that input is an int
    '''
    while True:
        try:
            numOfWheels = int(input('Value - '))
            return numOfWheels
        except(ValueError):
            print("Please enter a valid number!")

def checkReg():
    '''
    Function to check if the entered registration for vehicle exists
    '''
    while True:
        vehicleReg = input('Registration - ')
        regCheck = 0
        if len(garage) == 0:
            return vehicleReg
        else:
            for vehicle in garage:
                if vehicleReg == vehicle.registration:
                    regCheck += 1
                else:
                    pass
            if regCheck == 1:
                print(f'{vehicleReg} already exists - please try again!')
            else:
                return vehicleReg

def defineEngineType():
    '''
    Function for the user to choose what the engine type of the vehicle is
    '''
    while True:
        print('Enter the corresponding number for the engine type for the vehicle.\n1) Petrol\n2) Diesel\n3) Electric\n4) Hydrogen')
        try:
            engineChoice = int(input('Value - '))
            if engineChoice == 1:
                print('You have chosen Petrol')
                return 'Petrol'
            elif engineChoice == 2:
                print('You have chosen Diesel')
                return 'Diesel'
            elif engineChoice == 3:
                print('You have chosen Electric')
                return 'Electric'
            elif engineChoice == 4:
                print('You have chosen Hydrogen')
                return 'Hydrogen'
            else:
                print(f"{engineChoice} is not a valid option. Please try again!")
        except(ValueError):
            print("Please enter a valid number!")

def registerCar():
    '''
    Process of adding a new car (object) to the garage (object/list)
    '''
    print('Enter the brand of the car:')
    carBrand = input('Brand name - ')
    print('Enter the car model:')
    carModel = input('Car model - ')
    print('Enter the number of wheels:')
    carWheels = vehicleNum()
    print('Enter the number of doors:')
    carDoors = vehicleNum()
    print('Enter the engine type:')
    carEngine = defineEngineType()
    print('Enter the year the car was manufactured in:')
    carYear = vehicleNum()
    print('Enter the car registration:')
    carRegistration = checkReg()

    print('Creating car!')
    newcar = Car(carBrand, carModel, carWheels, carDoors, carEngine, carYear, carRegistration)
    print('Car created!')
    print(f'Adding {carRegistration} to garage....')
    garage.addVehicleToGarage(newcar)
    print('Added!')

def registerMotorbike():
    '''
    Process of adding a new Motorbike (object) to the garage (object/list)
    '''
    print('Enter the brand of the motorbike:')
    bikeBrand = input('Brand name - ')
    print('Enter the motorbike model:')
    bikeModel = input('Motorbike model - ')
    print('Enter the number of wheels:')
    bikeWheels = vehicleNum()
    print('Enter the engine type (i.e. Electric, Petrol, Diesel):')
    bikeEngine = defineEngineType()
    print('Enter the year the motorbike was manufactured in:')
    bikeYear = input('Year - ')
    print('Enter the motorbike registration:')
    bikeRegistration = checkReg()

    print('Creating motorbike!')
    newbike = Motorbike(bikeRegistration, bikeBrand, bikeModel, bikeWheels, bikeEngine, bikeYear)
    print('Motorbike created!')
    print(f'Adding {bikeRegistration} to garage....')
    garage.addVehicleToGarage(newbike)
    print('Added!')

def printChoice():
    '''
    Function to decide if the user wants to print information of all vehicles to a text file or a single vehicle to a text file
    '''
    printStatus = True
    while printStatus == True:
        try:
            print('Please choose the corresponding number if you want to print ALL vehicles in the garage or just ONE vehicle.\n1) All vehicles\n2) One vehicle')
            choice = int(input('Enter value - '))
            if choice == 1:
                garage.writeToFile()
                print(f'File written to {os.getcwd()} - called vehicle_log.txt')
                printStatus = False
            elif choice == 2:
                fileName = garage.writeOneVehicleToFile()
                print(f'File written to {os.getcwd()} - called {fileName}')
                printStatus = False
            else:
                print(f"{choice} is not a valid option. Please try again!")
        except(ValueError):
            print('Please enter a valid number!')

def deleteVehicles():
    '''
    Function to decide if the user wants to delete all vehicles in the list or a single vehicle
    '''
    while True:
        print('Do you want to delete all the vehicles in the garage or a specific vehicle?')
        print(f'There are currently {len(garage)} vehicles in the garage')
        print("Press 'A' for ALL vehicles or 'S' for specific vehicle")
        selection = input('Input - ').upper()
        if selection == 'A':
            garage.deleteAllVehicles()
            break
        elif selection == 'S':
            garage.deleteSingleVehicle()
            break
        else:
            print(f"I don't understand {selection} - please try again!")

#main body of program
garage = Garage()

print('Welcome to Vehicle Fleet manager!')
while True:
    print("Main menu:\n(R)egister a vehicle to the garage\n(V)iew all vehicle\n(F)ind a vehicle\n(P)rint vehicle information to text file\n(C)hange status of a vehcile\n(D)elete vehicles\n(Q)uit")
    print('Enter the appropriate letter in the brackets to choose\n')
    choice = input('Command - ').upper()
    if choice == 'R':
        registerVehicle()
    elif choice == 'V':
        print(garage)
        garage.numberOfvehicles()
    elif choice == 'F':
        reg = input('Please enter the registration of the vehicle you want to find: ').upper()
        garage.findAVehicle(reg)
    elif choice == 'P':
        printChoice()
    elif choice == 'C':
        garage.isInGarage()
    elif choice == 'D':
        deleteVehicles()
    elif choice == 'Q':
        print('Goodbye!')
        break
    else:
        print("I don't understand that! Try again!")
