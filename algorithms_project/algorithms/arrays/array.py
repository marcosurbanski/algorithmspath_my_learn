
class array:
    def __init__(self, array_data):
        self.array_data = array_data

    def simple_array(self):
        for x in self.array_data:
            print(f"valor {x}")

if __name__ == "__main__":
    numbers = [10, 20, 30]
    new_array = array(numbers)
    new_array.simple_array()
