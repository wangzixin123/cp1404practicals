colour_to_code = {'absolute zero':	'#0048ba', 'acid green': '#b0bf1a', 'alice blue': '#f0f8ff',
                  'alizarin crimson': '#e32636', 'amaranth':	'#e52b50', 'amber': '#ffbf00',
                  'amethyst':	'#9966cc', 'antique white':	'#faebd7', 'antique white1':	'#ffefdb',
                  'antique white2':	'#eedfcc', 'antique white3':	'#cdc0b0'}
colour_name = input("Enter a colour name: ").lower()
while colour_name != "":
    print(colour_to_code.get(colour_name, 'colour not found'))
    colour_name = input("Enter a colour name: ").lower()
