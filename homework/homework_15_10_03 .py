# Костромин Андрей Львович

hh_stroke = 'I am Learning Python. hello, WORLD!'

start = hh_stroke[:hh_stroke.find('h')]
middle = hh_stroke[hh_stroke.rfind('h'):hh_stroke.find('h'):-1]
end = hh_stroke[hh_stroke.rfind('h'):]

print(start + middle + end)
