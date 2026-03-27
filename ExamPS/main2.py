class TreasureChest:
    def __init__(self, question: str, answer: int, points: int):
        self.__question = question
        self.__answer = answer
        self.__points =  points

    def getQuestion(self):
        return self.__question
    
    def checkAnswer(self, inputAns):
        return self.__answer == inputAns

    def getPoints(self, attempts):
        return self.__points - (attempts - 1)

        
def readData(filepath: str) -> str:
    array = []
    try:
        with open(file=filepath, mode='r', encoding='utf-8') as file:
            for line in file:
                array.append(int(line.strip()))
        print(array)
    except FileNotFoundError:
        print(f'file at {filepath} not found')
    


readData('Data.txt')
