# python
import numpy as np

# 1.卡池中存在4、5、6星三种卡片；
# 2.每次抽卡时，获得6星卡片的概率为1.2%，5星卡片的概率为7.0%，获得4星卡片的概率为91.8%
# 3.若进行十连抽，则必定获得一张5星或6星卡片（可以理解为判断10次抽卡中的前9次是否有5星或6星卡片，若没有，则第十张卡片必为5星或6星卡片（先计算当前六星概率，若不出6星则必为5星））
# 4.若连续60抽未获得6星卡片，则从第61抽开始，每次抽卡获得6星卡片的概率增加6%（即第61抽获得6星卡片的概率为7.2%，第62抽获得6星卡片的概率为13.2%），直到获得6星卡片为止；获得6星卡片后，从下一抽重新开始计算本规则（比如一次十连抽中的第五抽获得了6星卡片，则这次十连抽结束后，该用户还需要再累计抽卡无6星卡片55次后，开始叠加6星卡片概率）；
# 5.6星卡片获取概率提升时，不影响5星卡片的获取概率，仅影响4星卡片的获取概率（即随着6星卡片获取概率的提升，4星卡片的获取概率会下降）；
# 6.若卡池中存在up的6星卡片，则第一次抽到6星卡片时，该6星卡片有50%的概率是up卡，若第一次抽到的6星卡片不是up卡，则第二次抽到6星卡片时必为up卡片；卡池内仅可能存在1张或者0张up的6星卡片；
# 7.若卡池中存在up的5星卡片，则每次抽到5星卡片时，都有50%的概率是up卡片；若存在多张5星up卡片，则多个up卡片共享50%的概率；


def up6(list):
    prize = np.random.choice([6,61],p=[0.5,0.5])
    if 61 in list:
        prize = 6
    return prize

def up5():
    return np.random.choice([5,51], p=[0.5,0.5])

def update_probabilities(probabilities,list):
    l = 0
    i = 0
    while i>0 and i<list.size:
        if(list[list-1-i] in [6,61]):
            i = -1 
        else:
            l = l+1
            i = i+1

    l = l - 60
    p = l * 0.06 if l * 0.06 > 1 else 1
    if(p==1):
        probabilities[0] = 0
        probabilities[1] = 0
        probabilities[2] = 1
    else:
        probabilities[0] = probabilities[0] - p
        probabilities[2] = probabilities[2] + p


def draw_lottery(list):
    
    # 奖池列表
    prizes = [4, 5, 6]

    # 对应的概率列表
    probabilities = [0.918, 0.07, 0.012]


     # 10抽判断
    flag10 = True
    if(len(list)<10): 
        flag10 = False
    else:
        for i in range(8):
            x = list[len(list)-i-1]
            if(x in [6, 61, 5, 51]):
                flag10 = False

    # 60抽判断
    flag60 = True
    if(len(list)<60):
        flag60 = False
    else:
        for i in range(59):
            x = list[len(list)-i-1]
            if(x == 6 or x == 61):
                flag60 = False
   
    prize = np.random.choice(prizes, p=probabilities)


    if(flag10==True & flag60==True):
        update_probabilities(probabilities,list)
        prize = np.random.choice(prizes, p=probabilities)
        if(prize!=6):prize=up5()
        elif(print==6):
            prize = up6(list)

    elif(flag60==True):
        update_probabilities(probabilities,list)
        prize = np.random.choice(prizes, p=probabilities)
        if(prize==6): prize = up6(list)
        if(prize==5): prize = up5()

    elif(flag10==True):
        prize = np.random.choice(prizes, p=probabilities)
        if(prize!=6):prize=up5()
        elif(print==6):
            prize = up6(list)

    return prize
    



# 抽奖结果缓存列表
list = []

while True:

    input('press enter lottery')

    # 进行一次抽奖
    prize = draw_lottery(list)

    # 缓存抽奖结果
    # if(len(list)>=77):list.pop(0)
    list.append(prize)

    print(prize)