def rpsgame():
    comp = random.choice(['r','p','s'])
    user = input('Enter rock(r), paper(p) or scissors(s) ')
    print(f"Computer's choice is {comp}")
    #p>r, r>s, s>p
    if(user == comp):
        print('It\'s a tie!!')
    elif((comp == 'p' and user == 'r') or (comp == 'r' and user == 's') or (comp == 's' and user == 'p')):
        print('You lost...computer wins!!')
    else:
        print('You won!!')
rpsgame()
