import random

class Kidsmaths:

    def __init__(self, person_name, score=None, diffculty='easy'):

        self.person_name = person_name
        self.score = score
        self.diffculty = diffculty

    def keep_score(self):

        self.score =+ 1
        return self.score

    def generate_question(self):

        operators = ['+', '-', '/', '*']

        if self.diffculty == 'easy':
            ran_num = random.randint(1, 10)
            ran_num2 = random.randint(1, 10)
        else:
            ran_num = random.randint(1, 100)
            ran_num2 = random.randint(1, 100)


        answer = ran_num + ran_num2

        results = (ran_num, ran_num2, answer)

        return results


    def __str__(self):

        return self.person_name



player = Kidsmaths('sam', 0, 'hard')
print(player)


if __name__ == '__main__':

     try:
         name = str(input("What is your name: "))
     except ValueError:
         print("Sorry I didn't understand that")
     else:
         player = Kidsmaths(name)
         ans = 0
         while True:
             num1, num2, ans = player.generate_question()
             player_ans = int(input(f"{num1} + {num2} = "))
             if player_ans == ans:
                 print('Correct')
                 player.keep_score()
             elif player_ans == 'q':
                 print(f'Your score is {score}')
             else:
                 print('Incorrect')





