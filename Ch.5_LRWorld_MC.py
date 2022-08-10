import random
import numpy as np
from copy import deepcopy as cp
class LRWorld():
    
    def __init__(self):
        self.x=6
        self.move_way = []

    #상태전이
    def step(self, a):
        global i 
        # 0번 액션: 왼쪽, 1번 액션: 오른쪽
        
        if a==0:       
            if self.move_way == ['L', 'R', 'L', 'R', 'L']:
                self.move_left()
                reward = 1000 #이 상태일 때만 1000점
            else:
                self.move_left()
                reward = -1   #왼쪽으로 움직일 때 보상:-1

        elif a==1:
            self.move_right()
            reward = +1 #오른쪽으로 움직일 때 보상:+1
        
        i = i + 1  
        
        done = self.is_done()
        
        return self.x, reward, self.move_way, done

    def move_left(self):
        self.x -= 1
        self.move_way.append("L")  
        
        if self.x < 0:
            self.x = 0
      
    def move_right(self):
        self.x += 1
        self.move_way.append("R")
        
        if self.x > 12:
            self.x = 12
      
      #6번 움직이면 종료
    def is_done(self):    
        if i == 6:                      
            return True                            
        else:            
            return False

    def get_state(self):
        return (self.x,self.move_way)
      
    def reset(self):
        self.x = 6
        self.move_way = []
        return (self.x,self.move_way)

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
    env = LRWorld()
    agent = Agent()

    #테이블 만들기
    data2 = {}
    act = ["L", "R"]
    data2[str([])] = 0
    for w in act:
        cal_data2 = []
        cal_data2_1 = cp(cal_data2) # [] , []
        cal_data2_1.append(w)       #[] , [0]
        data2[str(cal_data2_1)] = 0
        
        for w in act:                 
            cal_data2_2 = cp(cal_data2_1)
            cal_data2_2.append(w)      
            data2[str(cal_data2_2)] = 0
            
            for w in act:                 
                cal_data2_3 = cp(cal_data2_2)
                cal_data2_3.append(w)      
                data2[str(cal_data2_3)] = 0

                for w in act:
                    cal_data2_4 = cp(cal_data2_3)
                    cal_data2_4.append(w)      
                    data2[str(cal_data2_4)] = 0

                    for w in act:
                        cal_data2_5 = cp(cal_data2_4)
                        cal_data2_5.append(w)
                        data2[str(cal_data2_5)] = 0

                        for w in act:
                            cal_data2_6 = cp(cal_data2_5)
                            cal_data2_6.append(w)
                            data2[str(cal_data2_6)] = 0
    gamma = 1.0
    
    alpha = 0.001

    for k in range(10000):
        done = False
        history = [([],0)] #([],0)
        global i
        i=0 #6번 행동
        while not done:
            #print("1", history)
            action = agent.select_action()
            #print("2",action,history)
            history=cp(history) # TD와 똑같은 문제 발생, 상태전이가 일어나기 전에 history에 오류가 생기는 것을 막는다.
            x, reward, way, done = env.step(action)
            #print("3", way,history)
            history.append((way,reward))
            print("history", history)
            #print( )
            
        env.reset()

        cum_reward = 0
        for transition in history[::-1]:
            way, reward = transition
            data2[str(way)] = data2[str(way)] + alpha*(cum_reward-data2[str(way)])
            cum_reward = reward + gamma*cum_reward  
            #print(cum_reward)
            
    for i,keys in enumerate(data2):
        print(i,keys,data2[keys])

if __name__ == '__main__':
    main()
