from tabnanny import verbose
from NNclasses import *
import numpy as np 
from scipy.special import softmax
import matplotlib.pyplot as plt 

act = ActivationLayer(2, 'relu')

fake_affine_weights = np.random.rand(2, 2)
#print(fake_affine_weights)

X_train = np.array([[1, 1],[1, 0],[0, 1],[0, 0]])
y_train = np.array([0, 1, 1, 0])
#print(y_train.size)
'''
milp = MLP([2, 3, 2], ['relu'])
print(len(milp.layers_list))
for l in milp.layers_list:
    print(type(l))'''

#milp.fit(X_train, y_train, 4, 1, 40000)

#print(milp.predict(X_train))


sizes = [2, 4, 8, 16, 36]
scores = []
'''for size in sizes:
    right = 0
    for i in range(100): 
        m = MLP([2, size, 2], ['relu'])
        m.fit(X_train, y_train, batch_size=4, learning_rate=.09, epochs = 50)
        if (m.predict(X_train) == y_train).all():
            right +=1
    scores.append(right)
    print(f'with hidden layer size {size}: {right}/100')

plt.plot(sizes, scores)
plt.show()'''



        

milp = EmbeddingMLP([36], ['relu'], 2, 6, 2, 2)
print('======', milp.predict(X_train))
milp.fit(X_train, y_train, 4, 0.01, 10000)
print('==========', milp.predict(X_train))

'''e = EmbeddingLayer(4, 5, ones = True)
ins = np.array([[1, 2],[2, 3]])

f = e.forward_propagation(ins)

probs = milp.forward_propagation(f)

g = milp.back_propagation(probs, np.array([1, 0]))

g = np.ones(g.shape)

print('-----------\n', e.one_hot_matrix(ins))
e.back_propagation(ins, g)
e.update(1)
print(e.weights)
'''




