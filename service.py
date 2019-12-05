class Service:

    def __init__(self, id_, name, price):
        self.__id_ = id_
        self.__name = name
        self.__price = price

    def get_id(self):
        return self.__id_

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def __str__(self):
        attrib_list = [self.__id_, self.__name, self.__price]

        attrib_string = "/"
        attrib_string = attrib_string.join(attrib_list)

        return attrib_string
