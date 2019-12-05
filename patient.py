import person


class Patient(person.Person):
    def __init__(self, id_, name, addr, city, state, zip_, phone, email, DOB, ins_type, doctor):
        super().__init__(id_, name, addr, city, state, zip_, phone, email)

        self.__DOB = DOB
        self.__ins_type = ins_type
        self.__doctor = doctor
        self.__appt_list = []

    def get_ins_type(self):
        return self.__ins_type

    def get_doctor(self):
        return self.__doctor

    def get_appt_list(self):
        return self.__appt_list

    def __str__(self):
        string = super().__str__()
        string += "/"

        attrib_list = [self.__DOB, self.__ins_type, self.__doctor]
        attrib_string = "/"

        attrib_string = attrib_string.join(attrib_list)

        string += attrib_string

        return string


