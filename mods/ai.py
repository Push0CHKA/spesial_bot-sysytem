import random
import time

import numpy as np
from mods import db
import matplotlib.pyplot as plt # to plot error during training


# create NeuralNetwork class
class NeuralNetwork:

    # intialize variables in class
    def __init__(self, inputs, outputs):
        self.inputs = inputs
        self.outputs = outputs
        # initialize weights as .50 for simplicity
        sp_l = []
        for i in range(len(inputs[0])):
            sp_l.append([.50])
        self.weights = np.array(sp_l)
        self.error_history = []
        self.epoch_list = []

    # activation function ==> S(x) = 1/1+e^(-x)
    def sigmoid(self, x, deriv=False):
        if deriv == True:
            return x * (1 - x)
        return 1 / (1 + np.exp(-x))

    # data will flow through the neural network.
    def feed_forward(self):
        self.hidden = self.sigmoid(np.dot(self.inputs, self.weights))

    # going backwards through the network to update weights
    def backpropagation(self):
        self.error = self.outputs - self.hidden
        delta = self.error * self.sigmoid(self.hidden, deriv=True)
        self.weights += np.dot(self.inputs.T, delta)

    # train the neural net for 25,000 iterations
    def train(self, epochs=25000):
        for epoch in range(epochs):
            # flow forward and produce an output
            self.feed_forward()
            # go back though the network to make corrections based on the output
            self.backpropagation()
            # keep track of the error history over each epoch
            self.error_history.append(np.average(np.abs(self.error)))
            self.epoch_list.append(epoch)

    # function to predict output on new and unseen input data
    def predict(self, new_input):
        prediction = self.sigmoid(np.dot(new_input, self.weights))
        return prediction


def get_dataset():
    data_set = []
    ans_set = []
    bots = db.download('db/detect/main_data/main_data.db', 'main_data')
    new_bots = []
    cnt = 1
    for bt in bots:
        new_bots.append(bt)
        cnt += 1
        if cnt % 2000 == 0:
            break
    for bot in new_bots:
        ans_set.append([0])
        li = []
        if bot[4][:2] == 'id':
            li.append(0)
        else:
            li.append(1)
        if bot[4] == bot[6]:
            li.append(0)
        else:
            li.append(1)
        if bot[46] != '':
            if int(bot[46]) > 100:
                li.append(1)
            else:
                li.append(0)
        else:
            li.append(0)

        if bot[49] != '':
            if int(bot[49]) > 100:
                li.append(1)
            else:
                li.append(0)
        else:
            li.append(0)

        if bot[49] != '' and bot[51] != '':
            try:
                proc = int(bot[51]) / int(bot[49])
                if proc > 0.2:
                    li.append(1)
                else:
                    li.append(0)
            except:
                li.append(0)
        else:
            li.append(0)
        data_set.append(li)
    peopl = db.download('db/detect/friends_data/friends_data.db', 'friends_data')
    for bot in peopl:
        ans_set.append([1])
        li = []
        if bot[5][:2] == 'id':
            li.append(0)
        else:
            li.append(1)
        if bot[5] == bot[7]:
            li.append(0)
        else:
            li.append(1)
        if bot[47] != '':
            if int(bot[47]) > 100:
                li.append(1)
            else:
                li.append(0)
        else:
            li.append(0)

        if bot[50] != '':
            if int(bot[50]) > 100:
                li.append(1)
            else:
                li.append(0)
        else:
            li.append(0)

        if bot[50] != '' and bot[52] != '':
            try:
                proc = int(bot[52]) / int(bot[50])
                if proc > 0.2:
                    li.append(1)
                else:
                    li.append(0)
            except:
                li.append(0)
        else:
            li.append(0)
        data_set.append(li)

    inputs = np.array(data_set)
    # output data
    outputs = np.array(ans_set)

    # create neural network
    NN = NeuralNetwork(inputs, outputs)
    # train neural network
    NN.train()

    example = [1,1,0,0,0]
    example_2 = []
    example_3 = []
    for i in range(5):
        example_2.append(random.randint(0, 1))
        example_3.append(1)
    # create two new examples to predict
    example = np.array([example])
    example_2 = np.array([example_2])

    # print the predictions for both examples
    print(NN.predict(example), ' - Correct: ', example)
    print(NN.predict(example_2), ' - Correct: ?', example_2)
    print(NN.predict(example_3), ' - Correct: ', example_3)
    print(NN.weights)

    # plot the error over the entire training duration
    plt.figure(figsize=(15, 5))
    plt.plot(NN.epoch_list, NN.error_history)
    plt.xlabel('Epoch')
    plt.ylabel('Error')
    plt.show()

    # Набор входных данных
    """x = np.array(data_set)

    # Выходные данные
    y = np.array([ans_set]).T

    # Сделаем случайные числа более определёнными
    np.random.seed(1)

    # Инициализируем веса случайным образом со средним 0
    syn0 = 2 * np.random.random((len(data_set[0]), 1)) - 1

    l1 = []

    print('start learning')
    for iter in range(10000):
        if iter % 1000 == 0:
            print(iter)
        # Прямое распространение
        l0 = x
        l1 = sigmoid(np.dot(l0, syn0))

        # Насколько мы ошиблись?
        l1_error = y - l1

        # Перемножим это с наклоном сигмоиды
        # на основе значений в l1
        l1_delta = l1_error * sigmoid(l1, True)

        # Обновим веса
        syn0 += np.dot(l0.T, l1_delta)

    print("Выходные данные после тренеровки:")
    print(l1[0], l1[len(l1) - 1])"""
