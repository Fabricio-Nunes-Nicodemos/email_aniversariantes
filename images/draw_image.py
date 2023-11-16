from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import locale

locale.setlocale(locale.LC_ALL, "pt_BR.utf8")


def birthdays_image(**kwargs) -> None:

    title = kwargs.get("title")
    greetings = kwargs.get("greetings")
    greetings2 = kwargs.get("greetings2")
    pos_x = kwargs.get("pos_x")
    pos_y = kwargs.get("pos_y")
    title_pos_x = kwargs.get("title_pos_x")
    title_pos_y = kwargs.get("title_pos_y")

    count = 0

    if pos_x is None:
        pos_x = 120
    if pos_y is None:
        pos_y = 290

    if title_pos_x is None:
        title_pos_x = 120
    if title_pos_y is None:
        title_pos_y = 230

    dict_birthdays = kwargs.get("dict_birthdays")

    path_background_image = Path("images/background.png")
    # Linha para teste
    # path_background_image = Path("background.png")
    font_title = ImageFont.truetype("C:/fonts/OpenSans_Condensed-Bold.ttf", size=32)
    font_text = ImageFont.truetype("C:/fonts/OpenSans_Condensed-SemiBold.ttf", size=22)
    font_greatings = ImageFont.truetype("C:/fonts/OpenSans_Condensed-SemiBold.ttf", size=24)

    img = Image.open(path_background_image)
    draw = ImageDraw.Draw(img)

    for person in dict_birthdays:

        teste = dict_birthdays[person]["nascimento"].strftime("%d") + " - " + dict_birthdays[person]["nome"] + " - " + dict_birthdays[person]["departamento"]

        draw.text(xy=(pos_x, pos_y), text=teste, fill=(0, 0, 0), font=font_text)

        pos_y += 35

        if count == 13:
            pos_x = 540
            pos_y = 200

        count += 1

    draw.text(xy=(title_pos_x, title_pos_y), text=title, fill=(0, 51, 142), font=font_title)

    if greetings and greetings2 != "":

        draw.text(xy=(110, 545), text=greetings, fill=(137, 187, 80), font=font_greatings)
        draw.text(xy=(160, 613), text=greetings2, fill=(137, 187, 80), font=font_greatings)

    img.save("images/img_aniversariantes.png")
    # Linha para teste
    # img.save("img_aniversariantes.png")


if __name__ == "__main__":
    from database.consults import day_birthday
    from datetime import datetime

    TODAY = datetime.today()

    if TODAY.day < 10:
        day = f"0{TODAY.day}"
    else:
        day = TODAY.day

    birthdays_day = day_birthday()

    title_text = "Aniversariante"
    message = f" de {day} de {TODAY.strftime('%B').title()}"
    title_text += message

    birthdays_image(title=title_text, dict_birthdays=birthdays_day)
