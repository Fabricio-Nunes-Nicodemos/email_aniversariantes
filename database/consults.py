from database.conect import consults_manager
from datetime import datetime
from datetime import timedelta


def all_employees():

    sql = """SELECT R034FUN.NOMFUN, R034FUN.DATNAS, R034FUN.POSTRA, R018CCU.NOMCCU 
                        FROM VETORH.R034FUN 
                        INNER JOIN VETORH.R018CCU ON R018CCU.CODCCU = R034FUN.CODCCU
                        WHERE R034FUN.SITAFA IN ('1', '2', '3', '4', '6')"""

    return consults_manager(sql)


def day_birthday() -> dict:

    all_people = all_employees()
    birthdays_employees = {}

    for (index, data_in_row) in all_people.iterrows():

        if data_in_row.datnas.strftime("%d/%m") == datetime.today().strftime("%d/%m"):

            full_name = data_in_row.nomfun.title().strip()
            date_nasci = data_in_row.datnas.strftime("%d/%m/%Y")
            name_ccu = data_in_row.nomccu.title().strip()
            birthdays_employees[full_name] = {"nome": full_name, "nascimento": date_nasci, "departamento": name_ccu}

    return birthdays_employees


def weekend_birthday() -> dict:

    all_people = all_employees()
    birthdays_employees = {}
    today = datetime.today()

    if today.weekday() == 4:

        saturday = today + timedelta(days=1)
        sunday = today + timedelta(days=2)

        for (index, data_in_row) in all_people.iterrows():

            if data_in_row.datnas.strftime("%d/%m") == saturday.strftime("%d/%m") or data_in_row.datnas.strftime("%d/%m") == sunday.strftime("%d/%m"):

                full_name = data_in_row.nomfun.title().strip()
                date_nasci = data_in_row.datnas.strftime("%d/%m/%Y")
                name_ccu = data_in_row.nomccu.title().strip()
                birthdays_employees[full_name] = {"nome": full_name, "nascimento": date_nasci, "departamento": name_ccu}

        return birthdays_employees


def month_birthday() -> dict:

    all_people = all_employees()
    birthdays_employees = {}

    for (index, data_in_row) in all_people.iterrows():

        if data_in_row.datnas.strftime("%m") == datetime.today().strftime("%m"):

            full_name = data_in_row.nomfun.title().strip()
            date_nasci = data_in_row.datnas.strftime("%d/%m/%Y")
            name_ccu = data_in_row.nomccu.title().strip()
            birthdays_employees[full_name] = {"nome": full_name, "nascimento": date_nasci, "departamento": name_ccu}

    return birthdays_employees
