import random



class LR_WORLD():

    def __init__(self):
        self.x = 0
        self.his = []
        self.count = 0
        self.reward = 0

    def step(self, a):
        # 0번 액션: 왼쪽, 1번 액션: 오른쪽
        if a == 0:
            self.move_left()
            self.his.append('L')
            if self.his == ['L', 'R', 'L', 'R', 'L', 'L']:
                self.reward += 1000

            else:
                self.reward -= 1

        elif a == 1:
            self.move_right()
            self.reward += 1
            self.his.append('R')

        self.count += 1
        done = self.is_done()
        return self.x, self.reward, done, self.his, self.count

    def move_right(self):
        self.x += 1

        if self.x > 6:
            self.x = 6

    def move_left(self):
        self.x -= 1

        if self.x < -6:
            self.x = 6

    def is_done(self):
        if self.count == 6:
            return True
        else:
            return False

    def get_state(self):
        return self.x

    def reset(self):
        self.count = 0
        self.x = 0
        self.his = []
        self.reward = 0
        return


class Agent():

    def __init__(self):
        pass

    def select_action(self):
        # print('new', data[0][x-1], data[0][x], data[0][x+1],'\t',x,max(data[0][x-1], data[0][x+1]))
        if bool(data[1]) == False:
            coin = random.random()
            print(coin)
            if coin < 0.5:
                action = 0

                print(data[0][x - 1], data[0][x + 1], 'a=0')

            else:
                action = 1
                print(data[0][x-1], data[0][x+1], 'a=1')
            print(action)
        else:
            if data[0][x-1] <= data[0][x+1]:
                print(data[0][x-1], data[0][x+1], 'a=1')
                action = 1
            else:
                action = 0
                print(data[0][x - 1], data[0][x + 1], 'a=0')
        return action


def main():
    # TD
    global data, x
    env = LR_WORLD()
    agent = Agent()
    data = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],env.his]

    gamma = 1.0
    alpha = 0.01

    for k in range(50000):
        done = False
        while not done:
            x = env.get_state()
            action = agent.select_action()
            x_prime, reward, done, env.his, env.count = env.step(action)
            print(env.his)
            # x_prime = env.get_state()
            data[0][x] = data[0][x] + alpha * (reward + gamma * data[0][x_prime] - data[0][x])
            # print('update', data[0][x - 1], '--',data[0][x],'--', data[0][x + 1],'\t',x)
            # print(data)
        env.his.append(env.reward)


        data.remove(data[1])
        data.append(env.his)

        env.reset()

    change = data[0][:7]
    del data[0][:7]
    data[0] = data[0].__add__(change)

    for i in data:
        print(i)

if __name__ == '__main__':
    main()