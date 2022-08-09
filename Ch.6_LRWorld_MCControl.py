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
        
        return self.move_way, reward, done

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

class QAgent():
    def __init__(self):
        self.q_table = np.zeros((1, 127, 2)) # q벨류를 저장하는 변수. 모두 0으로 초기화. 
        self.eps = 0.9 
        self.alpha = 0.01
        
    def select_action(self, s):
        # eps-greedy로 액션을 선택
        for s,keys in enumerate(data2):
            move_way = s+1
        coin = random.random()
        if coin < self.eps:
            action = random.randint(0,1)
        else:
            action_val = self.q_table[1,move_way,:]
            action = np.argmax(action_val)
        return action

    def update_table(self, history):
        # 한 에피소드에 해당하는 history를 입력으로 받아 q 테이블의 값을 업데이트 한다
        cum_reward = 0
        for transition in history[::-1]:
            s, a, r, s_prime = transition
            move_way = s
            # 몬테 카를로 방식을 이용하여 업데이트.
            self.q_table[1,move_way,a] = self.q_table[1,move_way,a] + self.alpha * (cum_reward - self.q_table[1,move_way,a])
            cum_reward = cum_reward + r 

    def anneal_eps(self):
        self.eps -= 0.03
        self.eps = max(self.eps, 0.1)

    def show_table(self):
        # 학습이 각 위치에서 어느 액션의 q 값이 가장 높았는지 보여주는 함수
        q_lst = self.q_table.tolist()
        data = np.zeros((1,127))
        for row_idx in range(len(q_lst)):
            row = q_lst[row_idx]
            for col_idx in range(len(row)):
                col = row[col_idx]
                action = np.argmax(col)
                data[row_idx, col_idx] = action
        print(data)

def main():
    env = LRWorld()
    agent = QAgent()
    global data2
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
    for n_epi in range(1000): # 총 1,000 에피소드 동안 학습
        done = False
        history = []
        global i
        i=0
        s = env.reset()
        while not done: # 한 에피소드가 끝날 때 까지
            a = agent.select_action(s)
            s_prime, r, done = env.step(a)
            history.append((s, a, r, s_prime))
            s = s_prime
        agent.update_table(history) # 히스토리를 이용하여 에이전트를 업데이트
        agent.anneal_eps()

    agent.show_table() # 학습이 끝난 결과를 출력

if __name__ == '__main__':
    main()