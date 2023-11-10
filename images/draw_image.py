from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL, "pt_BR.utf8")


def birthdays_image(data):

    if data.day < 10:
        day = f"0{data.day}"
    else:
        day = data.day

    path_background_image = "background.png"
    img = Image.open(path_background_image)
    draw = ImageDraw.Draw(img)

    font_title = ImageFont.truetype("../fonts/OpenSans_Condensed-Bold.ttf", 32)
    title = f"Aniversariantes de {day} de {data.strftime('%B').title()}"
    draw.text((330, 110), title, (0, 51, 142), font=font_title)

    greatings = "Desejamos saúde, paz e felicidades, que seja um novo ciclo repleto de sucesso\n\t\te crescimento constante..."
    greatings2 = "Não se esqueçam de parabenizar os aniversariantes para ajudar a tornar este dia ainda\n\t\tmais especial!!"
    font_greatings = ImageFont.truetype("../fonts/OpenSans_Condensed-SemiBold.ttf", 24)
    draw.text((110, 545), greatings, (137, 187, 80), font=font_greatings)
    draw.text((160, 613), greatings2, (137, 187, 80), font=font_greatings)

    img.save("img_aniversariantes.png")


if __name__ == "__main__":

    birthdays_image(datetime.today())
