import random
import math
import pandas as pd
import numpy as np
class Hard:
    right_awnser = 0
    wrong_awnser = 0
    total_awnser = 0

    def __init__(self):    
        self.df = pd.DataFrame(columns=['right awnser', 'total awnser', 'level',"wrong awnser"])
        self.right_awnser = 0
        self.wrong_awnser = 0
        self.total_awnser = 0

    def long_multi(self):
        self.questions = {
            '4535 * 7685': 34851475,
            '6565 * 6656': 43696640,
            '45 * 500': 2250,
            '4554 * 765':3483810,
            '7548 * 2':15096
        }
        try:
            for quiz_amount in range(5):
                random_question = random.choice(list(self.questions))
                print(random_question)
                awnser = int(input('enter awnser: '))
                if awnser == self.questions[random_question]:
                    print("correct awnser")
                    self.right_awnser = self.right_awnser +1
                    self.total_awnser = self.total_awnser +1

                else:
                    print("wrong awnser")
                    self.wrong_awnser = self.wrong_awnser - 1
                    print("the correct awnser is: ",self.wrong_awnser)
                    self.total_awnser = self.total_awnser +1
                    print("the correct awnser is: ",self.questions[random_question])

            print('correct awnser:', self.self.right_awnser,'wrong awnser:',self.wrong_awnser,'total awnser',self.total_awnser)
            output = [[self.right_awnser] , [self.wrong_awnser], [self.total_awnser] , ["hard"]]
            self.df = self.df.append(output, ignore_index=True)

            print(self.df)

        except ValueError:
            print("please enter proper type")

        except KeyboardInterrupt:
            print("keyboard interrupted app")

        except Exception as e:
            print(e)

class Medium(Hard):
    
    def short_multi(self):
        self.questions = {
            '9 * 5': 45,
            '7 * 3': 21,
            '2 * 100': 200,
            '7 * 10':70,
            '5 * 7':35
        }
        try:
            for quiz_amount in range(5):
                random_question = random.choice(list(self.questions))
                print(random_question)
                awnser = int(input('enter awnser: '))
                if awnser == self.questions[random_question]:
                    print("correct awnser")
                    self.right_awnser = self.right_awnser +1
                    self.total_awnser = self.total_awnser +1

                


        except ValueError:
            print("please enter proper type")

        except KeyboardInterrupt:
            print("keyboard interrupted app")

        except Exception as e:
            print(e)

class Easy(Hard):
    def __init__(self):
        super().__init__()


    def ePlus(self):
        self.questions = {
            '5 + 5': 10,
            '7 - 3': 4,
            '2 + 100': 102,
            '7 - 10':3,
            '5 + 7':12
        }
        try:
            for quiz_amount in range(5):
                random_question = random.choice(list(self.questions))
                print(random_question)
                awnser = int(input('enter awnser: '))
                if awnser == self.questions[random_question]:

                    print("correct awnser")
                    self.right_awnser = self.right_awnser +1
                    self.total_awnser = self.total_awnser +1

                else:
                    print("wrong awnser")
                    self.wrong_awnser = self.wrong_awnser - 1
                    print("the correct awnser is: ",self.wrong_awnser)
                    self.total_awnser = self.total_awnser +1
                    print("the correct awnser is: ",self.questions[random_question])

            print('correct awnser:', self.self.right_awnser,'wrong awnser:',self.wrong_awnser,'total awnser',self.total_awnser)
            output = [[self.right_awnser] , [self.wrong_awnser], [self.total_awnser] , ["easy"]]
            self.df = pd.concat([pd.DataFrame(output), self.df], ignore_index=True)

        except ValueError:
            print("please enter proper value in awnser")

        except KeyboardInterrupt:
            print("keyboard interrupted app")

        except Exception as e:
            print(e)

levels = input("Please enter level Hard , Medium , Easy: ")
levels.lower()

if levels == "hard":
    obj = Hard()
    obj.long_multi()
elif levels == "medium":
    obj = Medium()
    obj.short_multi()

elif levels == "easy":
    obj = Easy()
    obj.ePlus()


      
        


   

        



