import random
import numpy as np

class GridWorld():
    def __init__(self):
        self.x=0
        self.y=0
    
    def step(self, a):
        # 0번 액션: 왼쪽, 1번 액션: 오른쪽
        if a==0:
            self.move_left()
            reward = -1 #왼쪽으로 움직일 때 보상:-1
        elif a==1:
            self.move_right()
            reward = +1 #오른쪽으로 움직일 때 보상:+1

        done = self.is_done()
        return (self.x, self.y), reward, done

    def move_left(self):
        self.y -= 1  
        if self.y < -6:
            self.y = -6
      
    def move_right(self):
        self.y += 1
        if self.y > 6:
            self.y = 6

    def is_done(self):
        for i in range(6):
            if i == 5:
                return True
            else:
                return False

    def get_state(self):
        return (self.x, self.y)
      
    def reset(self):
        self.x = 0
        self.y = 0
        return (self.x, self.y)

class Agent():
    def __init__(self):
        pass        

    def select_action(self):
        coin = random.random()
        if coin < 0.5:
            action = 0
        else:
            action = 1
        return action

#----main 함수부터 달라진다-----
def main():
    #TD
    env = GridWorld()
    agent = Agent()
    data = [[0,0,0,0,0,0,0,0,0,0,0,0,0]]
    gamma = 1.0
    
    alpha = 0.01

    for k in range(50000):
        done = False
        while not done:
            x, y = env.get_state()
            action = agent.select_action()
            (x_prime, y_prime), reward, done = env.step(action)
            x_prime, y_prime = env.get_state()
            data[x][y] = data[x][y] + alpha*(reward+gamma*data[x_prime][y_prime]-data[x][y])
        env.reset()
            
    for row in data:
        print(row)

if __name__ == '__main__':
    main()