__author__ = 'vladimir'

from random import choice, shuffle


class Message(object):
    def __init__(self, message, secret_row, secret_column):

        if self._all_chars_are_unique(secret_column):
            self.secret_column = secret_column
        if self._all_chars_are_unique(secret_row):
            self.secret_row = secret_row
        if self._text_fit_into_matrix(message):
            self.message = message

        self.matrix = None
        self.row_key = None
        self.column_key = None

    def encrypt(self):
        self.matrix = self._make_matrix()
        self.matrix, self.column_key = self._shuffle_columns()
        self.print_matrix()
        print "Your column key: {}\n".format(self.column_key)
        self.matrix, self.row_key = self._shuffle_rows()
        print "Your row key: {}\n".format(self.row_key)

        return self.matrix, self.row_key, self.column_key

    def _all_chars_are_unique(self, string):
        for char in string:
            if string.count(char) > 1:
                raise Exception("String: <{}> has not unique chars".format(string))
        return True

    def _text_fit_into_matrix(self, message):
        if len(message) > len(self.secret_row) * len(self.secret_column):
            raise Exception("String doesn't fit into this matrix")
        else:
            return True

    def _make_matrix(self, whitespace_symbols='aAeEcCsS'):
        text_len = len(self.message)
        row_len = len(self.secret_row)
        output = []
        for i_indx, i_val in enumerate(self.secret_column):
            output.append([])
            for j_indx, j_val in enumerate(self.secret_row):
                if row_len * i_indx + j_indx < text_len:
                    output[i_indx].append(self.message[row_len * i_indx + j_indx])
                else:
                    output[i_indx].append(choice(whitespace_symbols))
        return output

    def _shuffle_rows(self):
        new_order = range(len(self.secret_column))
        while new_order == range(len(self.secret_column)):
            shuffle(new_order)
        output = []
        for i in new_order:
            output.append(self.matrix[i])
        return output, new_order

    def _shuffle_columns(self):
        new_order = range(len(self.secret_row))
        while new_order == range(len(self.secret_row)):
            shuffle(new_order)
        output = []
        for i, val in enumerate(self.matrix):
            output.append([])
            for j in new_order:
                output[i].append(self.matrix[i][j])
        return output, new_order

    def decrypt(self, secret_row, secret_column):
        output = [None] * len(secret_row)
        for i_indx, i_val in enumerate(secret_row):
            output[int(i_val)] = self.matrix[int(i_indx)]
            tmp = [None] * len(secret_column)
            for j_indx, j_val in enumerate(secret_column):
                tmp[int(j_val)] = self.matrix[int(i_indx)][int(j_indx)]
            output[int(i_val)] = tmp
        return output

    def print_matrix(self):
        for i in self.matrix:
            print i

msg = Message('hello world', [6, 7, 2, 5], [1, 2, 3, 4])
test = msg.encrypt()
emsg = msg.decrypt(test[1], test[2])
print emsg