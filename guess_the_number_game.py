# Guess the number game
n = input('Please describe the minimum number.');
m = input('Please decrtibe the max number.');


# create random number
import random
randomNum = random.randint(int(n), int(m));

# challenge until you hit it.
for i in range(int(n)):
    userNum = input('Guess a random number between minimum and  max.');
    print(randomNum);

    if randomNum == int(userNum):
        print('correct!!');
        break;
    else:
        print('mistake!!');