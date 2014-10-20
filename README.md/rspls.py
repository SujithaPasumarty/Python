import random
# Converts String name into numbers 0 to 4
def name_to_number(name):
    if name=='rock':
        number=0
    elif name=='spock':
        number=1
    elif name=='paper':
        number=2
    elif name=='lizard':
        number=3
    elif name=='scissors':
        number=4
    else:
        number=-1
    return number

# Converts numbers 0 to 4 into corresponding string names
def number_to_name(number):
    if number==0:
        name='rock'
    elif number==1:
        name='spock'
    elif number==2:
        name='paper'
    elif number==3:
        name='lizard'
    elif number==4:
        name='scissors'
    else:
        print 'Invalid Input entered'
    return name
    
def rpsls(players_choice):
    print 'Player chooses '+players_choice
    player_number=name_to_number(players_choice)
    comp_number=random.randrange(0,4)
    comp_choice=number_to_name(comp_number)
    print 'Computer chooses '+comp_choice
    value=(comp_number - player_number)%5
    if value==1 or value==2:
        print 'Computer Wins!'
    elif value==3 or value==4:
        print 'Player Wins!'
    else:
        print 'Player and Computer ties!'

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
       
    
    

        
