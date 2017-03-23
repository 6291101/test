import random
def number_guesser(low,high):
    secret=random.randint(low,high)
    print ('Guess my number between', low,'and', high)   
    guess = int(raw_input('Guess: '))
    guess =secret
    while guess !=secret:
        if guess>secret:
            print('no,', guess,'is too high')
            if guess<secret:
                print('no,', guess,'is too low')
        else:
            print('yes!', guess,'is my number')                
            
      # 11. because the numbers could get very big like 1- 1 billion, that would be a painful brian melting task.
      #      