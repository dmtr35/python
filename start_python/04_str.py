# методы строк

# s = 'stroka texta'


# print('str' in s)       # поиск по строке (True/False)



# up = s.upper()                       # все в верхний регистр         
# low = s.lower()                      # все в нижний регистр
# cap = s.capitalize()                 # первая в нижний регистр
# print(up)
# print(low)
# print(cap)
# .rstrip('.')                         # удалить все точки справа от строки
# .lstrip('\'')                        # удалить все символы слева от строки


# path = 'C:/Users/PyHS/Desktop/s.py'
# path1 = path.replace('/', '\\')        # заменить подстроку
# name = path1.split('\\')               # разбиваем по разделителю '\'
# print(name[-1])                        # получаем последный элемент списка


# =========================================================

# r = open('/home/dm/bin/test_110.txt')
# text = r.read()
# text = text.replace('\"', '')
# text = text.replace('(', '')
# text = text.replace(')', '')
# text = text.replace('\n', '\t')


# print(text)
# r.close()

# ============================================================
enter = input('Your name: ')
python = 'Python'


print('Hello %s, I am %s' % (enter, python))
print(f'Hello {enter}, I am {python}')











