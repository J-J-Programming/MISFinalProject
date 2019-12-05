class Person:
    def __init__(self, id_, name, addr, city, state, zip_, phone, email):
        self.__id = id_
        self.__name = name
        self.__addr = addr
        self.__city = city
        self.__state = state
        self.__zip = zip_
        self.__phone = phone
        self.__email = email

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_addr(self):
        return self.__addr

    def get_city(self):
        return self.__city

    def get_state(self):
        return self.__state

    def get_zip(self):
        return self.__zip

    def get_phone(self):
        return self.__phone

    def get_email(self):
        return self.__email

    def __str__(self):
        attrib_list = [self.__id, self.__name, self.__addr, self.__city, self.__state, self.__zip, self.__phone, self.__email]

        attrib_string = "/"
        attrib_string = attrib_string.join(attrib_list)

        return attrib_string
