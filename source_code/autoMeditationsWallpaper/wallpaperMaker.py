import os

from PIL import Image, ImageFont, ImageDraw

from autoMeditationsWallpaper.textFormatter import TextFormatter


def number_to_word(i):
    if i == 1:
        return "First"
    elif i == 2:
        return "Second"
    elif i == 3:
        return "Third"
    elif i == 4:
        return "Forth"
    elif i == 5:
        return "Fifth"
    elif i == 6:
        return "Sixth"
    elif i == 7:
        return "Seventh"
    elif i == 8:
        return "Eight"
    elif i == 9:
        return "Ninth"
    elif i == 10:
        return "Eleventh"
    elif i == 11:
        return "Eleventh"
    elif i == 12:
        return "Twelfth"
    else:

        print("wrong input in word_to_number")
        return "ERROR: Book does not exist!"


def textToImage(text, book):
    img = Image.open(os.path.join(os.path.dirname(__file__), "MarcusAureliusWallpaper.png"))
    draw = ImageDraw.Draw(img)
    draw.text((90, 720), "The " + (number_to_word(book)) + " Book", (233, 67, 115),
              ImageFont.truetype("timesbd.ttf", 50))

    x = 550
    y = 60

    obj = TextFormatter(text, (1920 - x), (1920 - (x - x / 2)), 990, 550, 35, 18)

    obj.format_input_string()

    font = ImageFont.truetype("timesi.ttf", obj.fontSizeMax)

    for line in obj.formatted_lines:

        draw.text((x, y), line, (233, 67, 115), font=font)
        if y < 610:
            x += obj.fontSizeMax / 2


        else:
            x -= obj.fontSizeMax / 2

        y += obj.fontSizeMax

    img.save("sample-out.png")
