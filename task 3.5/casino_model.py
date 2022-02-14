import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def table_seq(ini_prob, K):

    var = np.random.binomial(1, ini_prob, 1)
    table_seq = []
    table_seq.append(var[0])

    for i in range(1,K):

        var = np.random.binomial(1, 1/4, 1)
        # Change table
        if (var[0] == 1) and (table_seq[i-1]==0) :  
            table_seq.append(1)
        elif (var[0] == 1) and (table_seq[i-1]==1):
            table_seq.append(0)
        # Stay in the same table
        else:
            table_seq.append(table_seq[i-1])
    
    return table_seq



def sample(K,primed,unprimed,player,table_seq):
    
    player_result = []
    table_result = []
    S = []
    for i in range(K):

        # Sample from the player
        pos = np.random.multinomial(1, player)
        number = np.argmax(pos)
        player_result.append(number+1)

        # Sample from the table
        if table_seq[i] == 0:
            pos = np.random.multinomial(1, unprimed)
        else: 
            pos = np.random.multinomial(1, primed)
        number = np.argmax(pos)
        table_result.append(number+1)

    for i in range(K):
        S.append(table_result[i] + player_result[i])
    # print('player_result',player_result)
    # print('table_result',table_result)
    # print('S',S)


    return S




N = 100
# Choose the number of tables and generate a sequence of tables
K = 10
ini_prob = 0.5
table_seq = table_seq(ini_prob, K)
print('tables seq', table_seq)

# Choose different cat distr for the unprimed, primed table and the player
primed = []
unprimed = []
player = []

for i in range(6):
    primed.append(1/6)
    unprimed.append(1/6)
    player.append(1/6)

# primed = [1,0,0,0,0,0]
# unprimed = [1,0,0,0,0,0]
# player = [0,0,0,0,0,1]

# Obtain the S = (S1,...,SN) sequence. For each Si, sampling K tables by getting dice sum ofthe player and the table,
# which can be primed or unprimed
# Do this for N players:
S = []
for i in range(N):
    S.append(sample(K,primed,unprimed,player,table_seq))

# To plot data for different categorical distributions and player
ocurrence = [0,0,0,0,0,0,0,0,0,0,0]
for i in range(N):
    for j in range(K):
        ocurrence[S[i][j]-2] += 1

print('ocurrence', ocurrence)

# plt.bar(range(len(ocurrence)), ocurrence, width=0.5)
plt.bar([2,3,4,5,6,7,8,9,10,11,12], ocurrence, width=0.5)

plt.xticks([2,3,4,5,6,7,8,9,10,11,12])
plt.ylabel('Count')
plt.xlabel('Numbers')
plt.title(str(N)+' players and '+str(K)+' tables')
plt.show()