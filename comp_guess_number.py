print('****************************************************')
print('*       Computer guess a number from 0 to 20       *')
print('*    if computer variant is correct print "yes"    *')
print('*if computer variant is less than your print "more"*')
print('*if computer variant is more than your print "less"*')
print('****************************************************')
min_value = 0
max_value = 20
counter = 6
variant = 10
while counter > 0:
    print('Chanses:', counter)
    print('Your number is', variant, '?')
    hint = input()
    if hint == 'yes':
        print('Nice!')
        input('Press Enter to exit')
        break
    elif hint == 'more':
        counter -= 1
        min_value = variant
        variant = (min_value + max_value + 1) // 2
    elif hint == 'less':
        counter -= 1
        max_value = variant
        variant = (min_value - 1 + max_value) // 2
    else:
        print('Unknown command')
else:
    print('Game over')
    input('Press Enter to exit')
