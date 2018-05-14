class Calendar:
    MAX_DAYS = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, day, month, year):
        self.day = day
        self.year = year
        self.month = month
        self.valid = self.check_valid()

    def isLeapYear(self):
        if self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        else:
            return False

    def check_valid(self):
        if self.year <= 0:
            return False
        if self.month <= 0 or self.month > 12:
            return False
        if self.day <= 0 or self.day > self.MAX_DAYS[self.month - 1]:
            return False
        if self.month == 2 and self.day == 29 and not self.isLeapYear():
            return False
        return True





