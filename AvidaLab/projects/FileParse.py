import sys


class Parser:

    def __init__(self, file_name):
        self.file_name = file_name
        file = open(file_name, 'r')
        self.type = file.readline()[2:]
        self.date_created = file.readline()[2:]

        # Take out stupid comments
        line = file.readline()
        while line[2] != ' ':
            line = file.readline()

        # Store the column names in a its list
        data_list = {}
        self.keys = []
        i = 0
        while line.startswith("#"):
            data_list[line[6:-1]] = []
            self.keys.append(line[6:-1])
            line = file.readline()
            i = i + 1
        # Store Data in list of lists (duple)
        data = file.readline()
        while len(data) > 1:  # until it reaches the end of the file
            i = 0
            for col in self.keys:
                data_list[col].append(float(data.split()[i]))
                i = i + 1
            data = file.readline()
        self.data = data_list


    def list_fields(self):
        """
        :return: list of the fields
        """
        return self.keys

    def get_column(self, column):
        """
        Gets a column of data
        :param column: string of the column
        :return: list
        """
        return self.data[column]

    def get_all_data(self):
        """
        Gets all the data from the map
        :return: map
        """
        return self.data

    def get_row(self, row_int):
        """
        Gets the row of the map by the integer
        :param row_int: index of the row
        :return: list of the row
        """
        row = []
        for col in self.keys:
            row.append(self.data[col][row_int])
        return row

    def get_row_by_update(self, update_num):
        """
        Uses the update number to find a row
        :param update_num: the index by update of the row to return
        :return: list of the row
        """
        return self.get_row(self.data['Update'].index(float(update_num)))


    """   Returns the data at the location [row][column]   """
    def get_data(self, column, row):
        """
        Gets a specific peice of data at the column in the row specified
        :param column: String of the column
        :param row: integer of the row
        :return: float at the column and row
        """
        return self.data[column][row]

    def get_data_by_update(self, column, update_num):
        """
        Uses the Update column to find a specific peice of data
        :param column: Name of the column to query
        :param update_num: Number in update
        :return: float at the column row
        """
        return self.data[column][self.data['Update'].index(float(update_num))]

    def __str__(self):
        """
        String representation of itself
        :return: String
        """
        return self.file_name