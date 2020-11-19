from pathlib import Path


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


def int_to_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num


with open(str(Path("meditations").resolve()) + "\\55317.txt", 'rt') as myfile:
    book = 1
    excerpt = 1
    BooksAndExcerptsMatrix = []
    isOnCorrectBook = None

    for enum, line in enumerate(myfile, 1):
        if len(line) > 1:
            if "BOOK " + int_to_roman(book + 1) + "." in line:
                isOnCorrectBook = False
                excerpt = 1
                book += 1


            if "BOOK " + int_to_roman(book) + "." in line:
                isOnCorrectBook = True


            if isOnCorrectBook:

                first_word = line.split()[0]
                if first_word == str(excerpt) + ".":
                    BooksAndExcerptsMatrix.append([book, excerpt, enum])
                    excerpt += 1
                if "END" in line and len(BooksAndExcerptsMatrix) >= 1:

                    BooksAndExcerptsMatrix[-1].append(enum)
                    isOnCorrectBook = False
                    excerpt = 1
                    book += 1



