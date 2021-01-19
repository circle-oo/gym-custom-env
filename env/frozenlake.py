import gym
import numpy as np

from env.baseenv import _Env

class FrozenLake(_Env):
    def __init__(self, render):
        super().__init__('FrozenLake-v0', render)
        self.action_number = 4
        self.state_number = 1
    
    def action(self, act):
        return np.argmax(act)
        