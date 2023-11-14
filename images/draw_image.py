from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import locale

locale.setlocale(locale.LC_ALL, "pt_BR.utf8")


def birthdays_image(**kwargs) -> None:

    title = kwargs.get("title")
    greetings = kwargs.get("greetings")
    greetings2 = kwargs.get("greetings2")

    count = 0
    pos_y = 200
    pos_x = 180
    dict_birthdays = kwargs.get("dict_birthdays")

    path_background_image = Path("images/background.png")
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

    draw.text(xy=(330, 110), text=title, fill=(0, 51, 142), font=font_title)

    if greetings and greetings2 != "":

        draw.text(xy=(110, 545), text=greetings, fill=(137, 187, 80), font=font_greatings)
        draw.text(xy=(160, 613), text=greetings2, fill=(137, 187, 80), font=font_greatings)

    img.save("images/img_aniversariantes.png")
