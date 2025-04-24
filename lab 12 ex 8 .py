class String:
    def _init_(self, text):
        self.text = text

    def _iadd_(self, other):
        self.text += other.text
        return self

    def toLower(self):
        return self.text.lower()

    def toUpper(self):
        return self.text.upper()
