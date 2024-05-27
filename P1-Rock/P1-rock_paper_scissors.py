import random
while True :
    user = input('choose (S,R,P):حح \n').lower()
    pc = random.choice(['s','r','p' ])

    print('user played: ' + user)
    print('pc played: ' + pc)

    if pc == user :
        print('tie!')
    elif ((user == 's' and pc == 'p') or (user == 'p' and pc == 'r') or (user == 'r'and pc == 's') ):
        print('You Win')
    else:
        print('Pc Win')