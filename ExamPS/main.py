class DataHandler:
    def __init__(self, filename):
        self.DataArray = []
        self.filename = filename

    
    def read_data(self):
        try:
            with open(file=self.filename, mode='r', encoding='utf-8') as file:
                for line in file:
                    self.DataArray.append(int(line.strip()))
                
            if len(self.DataArray) != 25:
                print(f"Warning: Expected 25 integers, but found {len(self.DataArray)}")

        except FileNotFoundError:
            print(f"Error: File {self.filename} not found.")

        except ValueError:
            print("Error: File contains non-integer values.")

        
    def PrintArray(self):
        for item in self.DataArray:
            print(item, end=' ')
        print()

    
    def LinearSearch(self, search_value):
        count = 0
        for item in self.DataArray:
            if item == search_value:
                count += 1
        return count 

    def search_number(self):
        while True:
            try:
                num = int(input("Enter a whole number between 0 and 100 inclusive: "))
                if 0 <= num <= 100:
                    break
                else:
                    print("Number out of range. Try again.")
            except ValueError:
                print("Invalid input. Enter a whole number.")

        occurrences = self.LinearSearch(num)
        print(f"The number {num} is found {occurrences} time{'s' if occurrences != 1 else ''}.")


if __name__ == "__main__":
    handler = DataHandler("Data.txt")
    handler.read_data()       
    print("DataArray contents:")  
    handler.PrintArray()      
    handler.search_number()   

                