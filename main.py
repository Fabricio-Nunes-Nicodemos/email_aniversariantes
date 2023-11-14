from database.consults import month_birthday, weekend_birthday, day_birthday
from datetime import datetime
from images.draw_image import birthdays_image

TODAY = datetime.today()
GREETINGS = "Desejamos saúde, paz e felicidades, que seja um novo ciclo repleto de sucesso\n\t\te crescimento constante..."
GREETINGS2 = "Não se esqueçam de parabenizar os aniversariantes para ajudar a tornar este dia ainda\n\t\tmais especial!!"


def data_to_image(dict_birthdays: dict, messages: str, **kwargs):

    if len(dict_birthdays) > 0:

        if len(dict_birthdays) >= 2:
            title_text = "Aniversariantes"
        else:
            title_text = "Aniversariante"

        title_text += messages

        birthdays_image(title=title_text, dict_birthdays=dict_birthdays, greetings=kwargs.get("greetings"), greetings2=kwargs.get("greetings2"))


# Day birthday
if len(day_birthday()) > 0:

    if TODAY.day < 10:
        day = f"0{TODAY.day}"
    else:
        day = TODAY.day

    message = f" de {day} de {TODAY.strftime('%B').title()}"

    data_to_image(day_birthday(), message, greetings=GREETINGS, greetings2=GREETINGS2)

# Month birthdays
if TODAY.day == 1:

    message = " do mês de " + TODAY.strftime("%B").title()

    data_to_image(month_birthday(), message)

# Weekend birthdays
if TODAY.weekday() == 4:

    message = " do fim de semana"

    data_to_image(weekend_birthday(), message, greetings=GREETINGS, greetings2=GREETINGS2)
