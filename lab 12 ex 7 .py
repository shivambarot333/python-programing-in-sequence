class Date:
    def _init_(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def _eq_(self, other):
        return (self.day == other.day and self.month == other.month and self.year == other.year)
