# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 21:00:47 2018

@author: antonio
"""

import numpy as np

class Simulation:
    def __init__(self):
        self.num_in_sys = 0

        self.clock = 0.0
        self.t_arrival = self.generate_interarrival()
        self.t_departure = float('inf')

        self.num_arrivals = 0
        self.num_departs = 0
        self.total_wait = 0.0

    def advance_time(self):
        t_event = min(self.t_arrival,self. t_departure)
        self.total_wait += self.num_in_sys * (t_event-self.clock)
        self.clock = t_event

        if(self.t_arrival <= self.t_departure):
            self.handle_arrival_event()
        else:
            self.handle_departure_event()

    def handle_arrival_event(self):
        self.num_in_sys += 1
        self.num_arrivals += 1

        if(self.num_in_sys <= 1):
            self.t_departure = self.clock + self.generate_service()
        self.t_arrival = self.clock + self.generate_interarrival()

    def handle_departure_event(self):
        self.num_in_sys -= 1
        self.num_departs += 1

        if(self.num_in_sys > 0):
            self.t_departure = self.clock + self.generate_service()
        else:
            self.t_departure = float('inf')

    def generate_interarrival(self):
        return np.random.exponential(1./3)

    def generate_service(self):
        return np.random.exponential(1./4)

np.random.seed(0)

s = Simulation()

for i in range(100):
    s.advance_time()

print(s.num_arrivals)
print(s.num_departs)
print(s.total_wait)
print(s.total_wait / s.num_departs)