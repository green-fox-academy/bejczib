
def wc():
    filename = open("alma.txt")
    text = filename.read()
    line_count = len(text.split('\n'))
    char_count = len(text)
    filename.close()
    return [line_count, char_count]


#
# def rows(text):
#     db = 0
#     for row in text:
#         db += 1
#     return db
#
# text2 = filename.read()
#
# def char(text2):
#     db_char = 0
#     for row in text:
#         for char in row:
#             db_char += 1
#     return db_char
#
#
# def wc():
#     result= []
#     result.append(rows(text))
#     result.append(char(text2))
#     return result

print(wc())
