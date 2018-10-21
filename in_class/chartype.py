vowels = ['a','e','i','o','u']
enter = input('Please enter a vowel (1 character): ')

if enter in vowels:
    print('Congratulation!')
elif enter.isdigit():
    print('Please enter a character not a digit.')
elif enter.isalpha():
    print('Please enter a character that is a vowel.')
else:
    print('Sorry the input was not a vowel, a letter, or a digit.')