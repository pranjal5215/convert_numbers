class Numbers:
    def __init__(self):
        # hindi
        self.__group = (
        ('१', '1'),
        ('२', '2'),
        ('३', '3'),
        ('४', '4'),
        ('५', '5'),
        ('६', '6'),
        ('७', '7'),
        ('८', '8'),
        ('९', '9'),
        ('०', '0'),
        )
        # persian
        self.__group_2 = (
        ('۱', '1'),
        ('۲', '2'),
        ('۳', '3'),
        ('۴', '4'),
        ('۵', '5'),
        ('۶', '6'),
        ('۷', '7'),
        ('۸', '8'),
        ('۹', '9'),
        ('۰', '0'),
        )
        # persian -  hindi
        self.__group_3 = (
        ('۱', '१'),
        ('۲', '२'),
        ('۳', '३'),
        ('۴', '४'),
        ('۵', '५'),
        ('۶', '६'),
        ('۷', '७'),
        ('۸', '८'),
        ('۹', '९'),
        ('۰', '०'),
        )


    def persian_to_english(self, x):
        num = []
        if isinstance(x, int):
            x = str(x)
        for ii,i in enumerate(x):
            for y in self.__group_2:
                if i in y:
                    num.append(y[1])
        return ''.join(map(str, num))

    def english_to_persian(self, x):
        num = []
        if isinstance(x, int):
            x = str(x)
        for ii,i in enumerate(x):
            for y in self.__group_2:
                if i in y:
                    num.append(y[0])
        return ''.join(map(str, num))


    # parsian to hindi
    def persian_to_hindi(self, x):
        num = []
        if isinstance(x, int):
            x = str(x)
        for ii,i in enumerate(x):
            for y in self.__group_3:
                if i in y:
                    num.append(y[1])
        return ''.join(map(str, num))

    def hindi_to_persian(self,x):
        num = []
        if isinstance(x, int):
            x = str(x)
        for ii,i in enumerate(x):
            for y in self.__group_3:
                if i in y:
                    num.append(y[0])
        return ''.join(map(str, num))


    # hindi to arabic
    def hindi_to_arabic(self, x):
        num = []
        if isinstance(x, int):
            x = str(x)
        for ii,i in enumerate(x):
            for y in self.__group:
                if i in y:
                    num.append(y[1])
        return ''.join(map(str, num))


    def arabic_to_hindi(self, x):
        num = []
        if isinstance(x, int):
            x = str(x)
        for ii,i in enumerate(x):
            for y in self.__group:
                if i in y:
                    num.append(y[0])
        return ''.join(map(str, num))


    def hindi_to_english(self, x):
        num = []
        if isinstance(x, int):
            x = str(x)
        for ii,i in enumerate(x):
            for y in self.__group:
                if i in y:
                    num.append(y[1])
        return ''.join(map(str, num))


    def english_to_hindi(self, x):
        num = []
        if isinstance(x, int):
            x = str(x)
        for ii,i in enumerate(x):
            for y in self.__group:
                if i in y:
                    num.append(y[0])
        return ''.join(map(str, num))


    def arabic_to_english(self, x):
        num = []
        if isinstance(x, int):
            x = str(x)
        for ii,i in enumerate(x):
            for y in self.__group:
                if i in y:
                    num.append(y[1])
        return ''.join(map(str, num))


    def english_to_arabic(self, x):
        num = []
        if isinstance(x, int):
            x = str(x)
        for ii,i in enumerate(x):
            for y in self.__group:
                if i in y:
                    num.append(y[0])
        return ''.join(map(str, num))
