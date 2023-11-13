from database.consults import month_birthday
from datetime import datetime
from images.draw_image import birthdays_image

TODAY = datetime.today()


def month_niver():

    title_text = ""

    if TODAY.day == 13:

        birthdays_of_the_month = month_birthday()

        if len(birthdays_of_the_month) > 0:

            if len(birthdays_of_the_month) >= 2:
                title_text = "Aniversariantes"
            else:
                title_text = "Aniversariante"

            title_text = title_text + " do mês de " + TODAY.strftime("%B").title()

            # greatings = "Desejamos saúde, paz e felicidades, que seja um novo ciclo repleto de sucesso\n\t\te crescimento constante..."
            # greatings2 = "Não se esqueçam de parabenizar os aniversariantes para ajudar a tornar este dia ainda\n\t\tmais especial!!"

            birthdays_image(title=title_text, dict_birthdays=birthdays_of_the_month)


month_niver()
