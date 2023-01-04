def main_function(x):
    if x > 0 and x <= 10:
        print('Число від нуля до десяти (включно)')
    elif x > 11 and x <= 20:
        print('Число від одинадцяти до двадцяти (включно)')
    elif x > 21 and x <= 30:
        print('Число від двадцяти одного до тридцяти (включно)')
    elif x > 31:
        print('Число більше тридцяти')


main_function(40)
