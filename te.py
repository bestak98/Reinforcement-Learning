from re import I


class LRWorld():
    def __init__(self):
        self.x=6

    global i
    i=0
    def step(self, a):
        global i
        
        # 0번 액션: 왼쪽, 1번 액션: 오른쪽
        if a==0:
            self.move_left()
            reward = -1 #왼쪽으로 움직일 때 보상:-1
        elif a==1:
            self.move_right()
            reward = +1 #오른쪽으로 움직일 때 보상:+1
        i += 1
        done = self.is_done()
        
        return (self.x), reward, done, i

LRWorld.step(i)

print(i)