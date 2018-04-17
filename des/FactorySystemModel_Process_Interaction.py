# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 20:02:37 2018

FACTORY SYSTEM MODEL

Specifications:
    - n = 50 machinesworking 8hours/day, 5 days/week
    - Each fails randomly after d~uniform(132,182) hours
    - Imediately replace with spare when available
    - Repairer fixes machine in r~uniform(4,1) hours, returns to spares
    - Hire R repairers at 3,75€/hour
    - Purchase S spares at 30£/day
    - Costs 20€/hour/machine if out-of-service (no spares)


@author: antonio mendes
"""

import simpy
import numpy as np

def factory_run(env, repairers, spares):    
    global costs

    costs = 0.0
    
    for i in range (50):
        env.process(operate_machine(env, repairers, spares))

    while True:
        costs += 3.75 * 8 * repairers.capacity + 30 * spares.capacity
        yield env.timeout(8.0)


def operate_machine(env, repairers, spares):
    global costs
    
    while True:
        yield env.timeout(generate_time_to_failure())
        t_broken = env.now
        print '{:.2f} machine broke' .format(t_broken)
        env.process(repair_machine(env, repairers, spares))
        #Launch repair process
        yield spares.get(1)
        t_replaced = env.now
        print '{:.2f} machine replaced' .format(t_replaced)
        costs += 20 * (t_replaced - t_broken)

def repair_machine(env, repairers, spares):
    with repairers.request() as request:
        yield request
        yield env.timeout(generate_repair_time())
        yield spares.put(1)
    print '{:.2f} repair complete' .format(env.now)

        
obs_time = []
obs_cost = []
obs_spares = []

def process_monitor(env, spares):
    while True:
        obs_time.append(env.now)
        obs_cost.append(costs)
        obs_spares.append(spares.level)
        yield env.timeout(1.0)
        

def generate_time_to_failure():
    return np.random.uniform(132,182)


def generate_repair_time():
    return np.random.uniform(4,10)



np.random.seed(0)

env = simpy.Environment()

repairers = simpy.Resource(env, capacity = 3)
spares = simpy.Container(env, init = 20, capacity = 20)



env.process(factory_run(env, repairers, spares))
env.process(process_monitor(env, spares))

env.run(until = 8 * 5.0 * 52) 



import matplotlib.pyplot as plt

plt.figure()
plt.step(obs_time, obs_spares, where = 'post')
plt.xlabel('time')
plt.ylabel('spares')

plt.figure()
plt.step(obs_time, obs_cost, where = 'post')
plt.xlabel('time')
plt.ylabel('cost')