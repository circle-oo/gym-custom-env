import gym
import numpy as np

from env.baseenv import _Env

class CartPole(_Env):
    def __init__(self, render):
        super().__init__('CartPole-v1', render)
        self.action_number = 1
        self.state_number = 4
    
    def action(self, act):
        return 1 if act > 0 else 0
        