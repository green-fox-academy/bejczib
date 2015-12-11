class MyString:
    def __init__(self, text):
        self.text = text

    def duplicate_encoder(self):
        result = ''
        for char in self.text.lower():
            if self.text.lower().count(char) == 1:
                result +='('
            else:
                result += ')'
        return result
