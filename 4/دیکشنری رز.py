class RoseDictionary:
    def __init__(self):
        self.rose = list(list())
        self.lastkey = None

    def __getitem__(self, key):
        for i in self.rose:
            if i[0] == key:
                return i[1]
        return "KeyError"

    def __setitem__(self, key, value):
        flag = False
        for i in range(self.rose.__len__()):
            if self.rose[i][0] == key:
                self.rose[i][1] = value
                flag = True
                break
        if flag == False:
            self.rose.append([key, value])

        self.lastkey = key

    def pop_item(self, raise_error=None, default=None, error_msg=None):
        if self.rose.__len__() != 0:
            value = None
            for i in range(self.rose.__len__() - 1, -1, -1):
                if self.rose[i][0] == self.lastkey:
                    value = self.rose[i][1]
                    self.rose.remove(i)
                    return value
            if raise_error:
                if error_msg is not None:
                    return print(error_msg)
                else:
                    return print('')
        elif self.rose.__len__() == 0:
            if raise_error:
                if error_msg is not None:
                    return print(f"KeyError: {error_msg}")
                else:
                    return print("KeyError: The RoseDictionary is empty")
            else:
                if default is None:
                    if error_msg is not None:
                        return print(error_msg)
                    else:
                        return print(
                            "Dictionary was empty and no default value/message was specified.")
                else:
                    return default

        else:
            if not raise_error:
                if default is not None:
                    return default
            return 'KeyError: Dictionary was empty and no default value/message was specified.'

    def get_item(self, key, raise_error=None, default=None, error_msg=None):
        if self.rose.__len__() != 0:
            for i in self.rose:
                if i[0] == key:
                    return i[1]
            if raise_error:
                if error_msg is not None:
                    return print(error_msg)
                else:
                    return print('')
        elif self.rose.__len__() == 0:
            if raise_error:
                if error_msg is not None:
                    return print(f"KeyError: {error_msg}")
                else:
                    return print("KeyError: The RoseDictionary is empty")
            else:
                if default is None:
                    if error_msg is not None:
                        return print(error_msg)
                    else:
                        return print(
                            "Value was not found and no default value/message was specified.")
                else:
                    return default
