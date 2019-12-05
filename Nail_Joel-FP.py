import person  # imported out of principle

import patient
import physician
import service
import appointment


def process_patient_file():
    patient_dict = {}
    patient_file = open("patients.txt", 'r')

    for patient_inp in patient_file:
        patient_split = patient_inp.rstrip().split('#')
        patient_obj = patient.Patient(patient_split[0], patient_split[1], patient_split[2], patient_split[3],
                                      patient_split[4], patient_split[5], patient_split[6], patient_split[7],
                                      patient_split[8], patient_split[9], patient_split[10])
        patient_dict[patient_split[0]] = patient_obj
    return patient_dict


def process_physician_file():
    physician_dict = {}
    physician_file = open("physicians.txt", 'r')

    for physician_inp in physician_file:
        physician_split = physician_inp.rstrip().split('#')
        physician_obj = physician.Physician(physician_split[0], physician_split[1], physician_split[2],
                                            physician_split[3], physician_split[4], physician_split[5],
                                            physician_split[6], physician_split[7])
        physician_dict[physician_split[0]] = physician_obj
    return physician_dict


def process_service_file():
    service_dict = {}
    service_file = open("services.txt", 'r')

    for service_inp in service_file:
        service_split = service_inp.rstrip().split('#')
        service_obj = service.Service(service_split[0], service_split[1], service_split[2])
        service_dict[service_split[0]] = service_obj
    return service_dict


def process_appointment_file():
    appointment_dict = {}
    appointment_file = open("appointments.txt", 'r')

    for appointment_inp in appointment_file:
        appointment_split = appointment_inp.rstrip().split('#')
        appointment_obj = appointment.Appointment(appointment_split[0], appointment_split[1], appointment_split[2],
                                                  appointment_split[3], appointment_split[4], appointment_split[5])
        appointment_dict[appointment_split[0]] = appointment_obj
    return appointment_dict


def process_services_rendered_file():
    services_rendered_dict = {}
    services_rendered_file = open("services_rendered.txt", 'r')

    for services_rendered_inp in services_rendered_file:
        services_rendered_split = services_rendered_inp.rstrip().split('#')
        appointment_id = services_rendered_split[0]
        services_rendered_list = services_rendered_split[1:]
        services_rendered_dict[appointment_id] = services_rendered_list
    return services_rendered_dict


def main():
    patient_dict = process_patient_file()
    physician_dict = process_physician_file()
    service_dict = process_service_file()
    appointment_dict = process_appointment_file()
    services_rendered_dict = process_services_rendered_file()

    for data in patient_dict:
        print(patient_dict[data])

    for data in services_rendered_dict:
        print(services_rendered_dict[data])


main()
