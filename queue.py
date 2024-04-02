class Queue:
    data_array = []

    # Insert new data to end of the array.
    def insert(self, data):
        self.data_array.append(data)

    # Removing the first element of the array.
    def remove(self):
        if self.data_array:
            return self.data_array.pop(0)
