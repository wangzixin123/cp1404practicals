name = input('please enter your name')
print(
    """(H)ello
(G)oodbye
(Q)uit""")
choice = input('>>>')
while choice != 'Q':
    if choice == 'H':
        print('hello', name)
    elif choice == 'G':
        print('goodbye', name)
    else:
        print('invalid choice')
    print(
       """(H)ello
(G)oodbye
(Q)uit""")
    choice = input('>>>')
print('Finished.')
