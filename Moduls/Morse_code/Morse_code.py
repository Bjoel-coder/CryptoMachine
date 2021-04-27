import re


class Morse:

    alph = ("а", "б", "в", "г", "д", "е", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", ",", ":", ";", "'", '"', "-", "/", "_", "?", "!", "+", "=", "@")
    code = ("*-", "-***", "*--", "--*", "-**", "*", "***-", "--**", "**", "*---", "-*-", "*-**", "--", "-*", "---", "*--*", "*-*", "***", "-", "**-", "**-*", "****", "-*-*", "---*", "----", "--*-", "--*--", "-**-", "-*--", "**-**", "**--", "*-*-", "-----", "*----", "**---", "***--", "****-", "*****", "-****", "--***", "---**", "----*", "******", "*-*-*-", "---***", "-*-*-*", "*----*", "*-**-*", "-****-", "-**-*", "**--*-", "**--**", "--**--", "*-*-*", "-***-", "*--*-*")

    def encode(self, text_input):
        text_input = text_input.strip().lower().replace("ё", "е")
        if text_input == "":
            return "Введите текст!", "", "#$/ERROR/$#"
        text_input = re.sub(r"\s{2,}", " ", text_input)
        text_input = list(text_input)
        for i in range(len(text_input)):
            if (text_input[i] not in self.alph) and (text_input[i] != " "):
                return "Используйте только RUS алфавит, цифры, пробел и знаки: . , : ; ' \" - / _ ? ! + = @", "", "#$/ERROR/$#"
            if text_input[i] == " ":
                text_input[i] = "   "
            else:
                text_input[i] = self.code[self.alph.index(text_input[i])]
            print(text_input[i])
        text_output = str(" ".join(text_input))
        return text_output, "", ""

    def decode(self, text_input):
        text_input = re.sub(r"\s{2,}", "   ", text_input).strip().replace(".", "*").replace("_", "-").replace("   ", " spc ")
        print(text_input)
        if text_input == "":
            return "Введите текст!", "", "#$/ERROR/$#"
        text_input = text_input.split(" ")
        print(text_input)
        for i in range(len(text_input)):
            if (text_input[i] not in self.code) and (text_input[i] != "spc"):
                print("{}".format(text_input[i]))
                return "Используйте только - _ * . и пробел!", "", "#$/ERROR/$#"
            if text_input[i] in self.code:
                text_input[i] = self.alph[self.code.index(text_input[i])]
            elif text_input[i] == "spc":
                text_input[i] = " "
            else:
                message = "Неизвестный код " + text_input[i]
                return message, "", "#$/ERROR/$#"
        text_output = str("".join(text_input))
        print(text_output)
        return text_output, "", ""
