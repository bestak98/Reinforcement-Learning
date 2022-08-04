import random
import numpy as np



class LRWorld():
    
    def __init__(self):
        self.x=6

    
    def step(self, a):
        global i 
        # 0번 액션: 왼쪽, 1번 액션: 오른쪽
        if a==0:
            self.move_left()
            reward = 0 #왼쪽으로 움직일 때 보상:-1
        elif a==1:
            self.move_right()
            reward = +1 #오른쪽으로 움직일 때 보상:+1
        i = i + 1
        
        done = self.is_done()
        
        return (self.x), reward, done

    def move_left(self):
        self.x -= 1  
        if self.x < 0:
            self.x = 0
      
    def move_right(self):
        self.x += 1
        if self.x > 12:
            self.x = 12
      
      #6번 움직이면 종료
    def is_done(self):    
        if i == 6:                      
            return True                            
        else:            
            return False

    def get_state(self):
        return (self.x)
      
    def reset(self):
        self.x = 6
        
        return (self.x)

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


def main():
    #TD
    env = LRWorld()
    agent = Agent()
    data = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    gamma = 0
    
    alpha = 0.1
    left = 0
    right = 0
    for k in range(1000):
        done = False
        global i
        i=0
        while not done:
            x = env.get_state()
            action = agent.select_action()
            if x == 5:
                if action == 0:
                    left += 1
                if action == 1:
                    right += 1
                
            (x_prime), reward, done = env.step(action)
            x_prime = env.get_state()
            #print(data[x],data[x_prime])
            data[x] = data[x] + alpha*(reward+gamma*data[x_prime]-data[x])
    
        env.reset()
    print(left, right)  
    print(data)

if __name__ == '__main__':
    main()