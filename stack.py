class Stack:
    data_array = []

    # Adding the data to end of the array.
    def insert(self, data):
        self.data_array.append(data)

    # Removing the last element first.
    def remove(self):
        return self.data_array.pop()
