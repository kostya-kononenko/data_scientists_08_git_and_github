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

def test_function(x):
    if x > 40 and x <= 50:
        print('Число від сорока до п\'ятдесяти (включно)')
    elif x > 51 and x <= 60:
        print('Число від п\'ятдесяти одного до шестидесяти (включно)')
    elif x > 61:
        print('Число більше шестидесяти одного')


test_function(50)
