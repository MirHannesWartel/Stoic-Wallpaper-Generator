class TextFormatter:
    inputString = ''
    length = 0
    maxLength = 0
    maxHeight = 0
    x_start_coordinate = 0
    fontSizeMax = 0
    fontSizeMin = 0
    formatted_lines = []
    total_line_height = 0

    def __init__(self, text, length, maxLenght, max_height, x, fMax, fMin):
        self.inputString = text
        self.length = length
        self.maxLength = maxLenght
        self.maxHeight = max_height
        self.x_start_coordinate = x
        self.fontSizeMax = fMax
        self.fontSizeMin = fMin

    def format_input_string(self):
        length = self.length
        self.total_line_height = 0
        self.formatted_lines = []
        leftover_line = ''
        for line in self.inputString:
            if self.total_line_height > 610 and (length + self.fontSizeMax / 2) < self.maxLength:

                length += self.fontSizeMax / 2
            else:
                length -= self.fontSizeMax / 2

            new_line = ''

            words = line.split()

            for word in words:

                if (len(new_line) * (self.fontSizeMax / 2)) + (len(word) * (self.fontSizeMax / 2)) >= length:
                    self.formatted_lines.append(new_line)
                    self.total_line_height += self.fontSizeMax
                    new_line = ''
                    leftover_line += word + " "

                elif (len(leftover_line) * (self.fontSizeMax / 2)) + (len(word) * (self.fontSizeMax / 2)) < length:
                    leftover_line += " " + word

                elif (len(leftover_line) * (self.fontSizeMax / 2)) + (len(word) * (self.fontSizeMax / 2)) > length:
                    new_line += leftover_line
                    self.formatted_lines.append(new_line)
                    self.total_line_height += self.fontSizeMax
                    new_line = ''
                    leftover_line = word

        if len(leftover_line) > 0:
            self.formatted_lines.append(leftover_line)
            self.total_line_height += self.fontSizeMax
            leftover_line = ""

        if self.total_line_height > self.maxHeight:
            try:

                if self.fontSizeMax == self.fontSizeMin and length < self.maxLength:

                    print("Text to long! Reformatting with longer lines")

                    length += self.fontSizeMax * 1

                    self.format_input_string()

                elif self.fontSizeMax > self.fontSizeMin:
                    print("Text to long! Reformatting with smaller font")
                    self.fontSizeMax -= 2
                    if self.fontSizeMax < self.fontSizeMin:
                        self.fontSizeMax = self.fontSizeMin
                    self.format_input_string()
            except RecursionError:
                print("Formatting failed: RecursionError")


    def get_formatted_lines(self):
        return self.formatted_lines
