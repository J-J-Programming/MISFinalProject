class Appointment:
    def __init__(self, id_, doctor, patient, filled, date, time):
        self.__id_ = id_
        self.__doctor = doctor
        self.__patient = patient
        self.__filled = filled
        self.__date = date
        self.__time = time
        self.__service_list = []

    def get_id(self):
        return self.__id_

    def get_doctor(self):
        return self.__doctor

    def get_patient(self):
        return self.__patient

    def get_filled(self):
        return self.__filled

    def get_date(self):
        return self.__date

    def get_time(self):
        return self.__time

    def get_service_list(self):
        return self.__service_list

    def __str__(self):
        attrib_list = [self.__id_, self.__doctor, self.__patient, self.__filled, self.__date, self.__time]

        attrib_string = "/"
        attrib_string = attrib_string.join(attrib_list)

        return attrib_string
