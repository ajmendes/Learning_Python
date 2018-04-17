# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 20:59:43 2018

@author: antonio
"""

#  https://www.youtube.com/watch?v=Kmu9DNQamLw


import simpy
import numpy as np


def warehouse_run(env, order_cutoff, order_target):
    global inventory, balance, num_ordered

    inventory = order_target
    balance = 0.0
    num_ordered = 0

    while True:
        interarrival = generate_interarrival()
        yield env.timeout(interarrival)
        balance -= inventory * 2 * interarrival
        demand = generate_demand()
        if demand < inventory :
            balance += 100 * demand
            inventory -= demand
            print('{:.3} Sold {}'.format(env.now, demand))
        else:
            balance += 100 * inventory
            inventory = 0
            print('{:.3} Sold out {} (out of stock)'.format(env.now, inventory))
        if inventory < order_cutoff and num_ordered == 0:
           env.process(handle_order(env, order_target))


def handle_order(env, order_target):
    global inventory, balance, num_ordered

    num_ordered = order_target - inventory
    print('{:.3} Ordered {}'.format(env.now, num_ordered))
    balance -= 50 * num_ordered
    yield env.timeout(2.0)
    inventory += num_ordered
    print('{:.3} Received order. Inv: {}'.format(env.now, inventory))
    num_ordered = 0


obs_time = []
inventory_level = []

def observe(env):
    global inventory

    while True:
        obs_time.append(env.now)
        inventory_level.append(inventory)
        yield env.timeout(0.1)


def generate_interarrival():
    return np.random.exponential(1./5)


def generate_demand():
    return np.random.randint(1,5)






np.random.seed(0)

env = simpy.Environment()
env.process(warehouse_run(env, 10, 30))
env.process(observe(env))

env.run(until = 5.0)

#import matplotlib as mpl
#mpl.use('tkagg')    #YAAA!!  this finally makes the Damn thing work

import matplotlib.pyplot as plt


plt.figure()
plt.step(obs_time, inventory_level, where = 'post')
plt.xlabel =('x')
plt.ylabel =('y')