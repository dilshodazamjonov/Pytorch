
Animal = []
Colour = []

AnimalTopPointer = 0
ColourTopPointer = 0

def PushAnimal(DataToPush: str) -> bool:
    global AnimalTopPointer
    if AnimalTopPointer == 20:
        return False
    
    else:
        Animal.append(DataToPush)
        AnimalTopPointer += 1
        return True


def PopAnimal() -> str:
    global AnimalTopPointer
    return_data: str = ''
    if AnimalTopPointer == 0:
        return False
    
    else: 
        return_data = Animal[AnimalTopPointer - 1]
        AnimalTopPointer -= 1
        return return_data
    

def PushColour(DataToPush: str) -> bool:
    global ColourTopPointer
    if ColourTopPointer == 20:
        return False
    
    else:
        Colour.append(DataToPush)
        ColourTopPointer += 1
        return True
    
def PopColour() -> str:
    global ColourTopPointer
    return_data: str = ''
    if ColourTopPointer == 0:
        return False
    
    else: 
        return_data = Colour[ColourTopPointer - 1]
        ColourTopPointer -= 1
        return return_data

def read_file(filepath) -> list:
    data = []
    try:
        with open(file=filepath, mode='r', encoding='utf-8') as file:
            for line in file:
                data.append(line.strip())
    
    except FileNotFoundError:
        print(f'file on the path {filepath} does not exist')

    return data

def ReadData(ColourFilePath: str, AnimalFilePath: str):
    animals = read_file(AnimalFilePath)
    colours = read_file(ColourFilePath)
    
    for animal in animals:
        PushAnimal(animal)
    
    for colour in colours:
        PushColour(colour)


def OutputItem():
    animal_popped = PopAnimal()
    colour_popped = PopColour()
    
    if not animal_popped:
        return 'No animal'
    if not colour_popped:
        return 'No colour'
    else:
        return(f'{colour_popped} {animal_popped}')

    


if __name__ == "__main__":
    ReadData("Colours.txt", "Animals.txt")

    # Output 4 items
    for _ in range(4):
        print(OutputItem())