def test_function(x):
    if x > 40 and x <= 50:
        print('Число від сорока до п\'ятдесяти (включно)')
    elif x > 51 and x <= 60:
        print('Число від п\'ятдесяти одного до шестидесяти (включно)')
    elif x > 61:
        print('Число більше шестидесяти одного')


test_function(50)
