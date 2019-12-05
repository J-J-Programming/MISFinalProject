import person


class Physician(person.Person):

    def __init__(self, id_, name, addr, city, state, zip_, phone, email):
        super().__init__(id_, name, addr, city, state, zip_, phone, email)

        self.__appt_list = []

    def get_appt_list(self):
        return self.__appt_list
