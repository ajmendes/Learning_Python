# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 21:00:48 2018

@author: antonio
"""

#https://www.youtube.com/watch?v=7LuN_6m7h2o

import numpy as np



class Simulation:
    def __init__(self, order_cutoff, order_target):
        self.inventory = order_target
        self.num_ordered = 0

        self.clock = 0.0
        self.t_customer = self.generate_interarrival()
        self.t_delivery = float('inf')

        self.revenue = 0
        self.cost_order = 0
        self.cost_holding = 0

        self.order_cuttof = order_cutoff
        self.order_target = order_target

    def advance_time(self):
        t_event = min(self.t_customer, self.t_delivery)
        self.cost_holding += self.inventory * 2 * (t_event- self.clock)
        self.clock = t_event

        if self.t_delivery <= self.t_customer :
            self.handle_delivery_event()
        else:
            self.handle_customer_event()

    def handle_customer_event(self):
        demand = self.generate_demand()
        if self.inventory > demand :
            self.revenue += 100 * demand
            self.inventory -= demand
        else:
            self.revenue = 100 * self.inventory
            self.inventory = 0

        if self.inventory < self.order_cuttof and self.num_ordered == 0:
            self.num_ordered = self.order_target - self.inventory
            print('order ', self.num_ordered)

            self.cost_order = 50 * self.num_ordered
            self.t_delivery = self.clock + 2

        self.t_customer = self.clock + self.generate_interarrival()

    def handle_delivery_event(self):
        self.inventory += self.num_ordered
        self.num_ordered = 0
        self.t_delivery = float('inf')

    def generate_interarrival(self):
        return np.random.exponential(1./5)

    def generate_demand(self):
        return np.random.randint(1, 5)



np.random.seed(0)
s = Simulation(10, 30)


print(s.clock,s.inventory, s.revenue, s.t_customer, s.t_delivery)

while s.clock <= 5.0:
    s.advance_time()
    print('inv: ',s.inventory)
    print()