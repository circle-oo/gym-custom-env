import gym
import numpy as np

from env.baseenv import _Env

class Breakout(_Env):
    def __init__(self, render):
        super().__init__('Breakout-v0', render)
        self.action_number = 4
        self.state_number = (1, 210, 160)
    
    def reset(self):
        state = super().reset()
        state = np.array(state)
        state = state.mean(axis=2)
        state = state.reshape((1, 210, 160))
        return state
    
    def action(self, act):
        return act
    
    def step(self, act):
        state, reward, done, _ = super().step(act)
        state = np.array(state)
        state = state.mean(axis=2)
        state = state.reshape((1, 210, 160))
        return state, reward, done, _