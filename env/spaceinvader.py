import gym
import numpy as np

from env.baseenv import _Env

class SpaceInvaders(_Env):
    def __init__(self, render):
        super().__init__('SpaceInvaders-v0', render)
        self.action_number = 6
        self.state_number = (210, 160, 3)
    
    def action(self, act):
        return np.argmax(6)
        