import gym
import numpy as np

from env.baseenv import _Env
from env.wrappers import make_atari, wrap_deepmind, wrap_pytorch

class Pong(_Env):
    def __init__(self, render):
        super().__init__('Pong-v0', render)
        self.action_number = 6
        self.state_number = (1, 84, 84)
    
    def reset(self):
        state = super().reset()
        state = np.array(state)
        state = state.mean(axis=2)
        state = np.resize(state, (84, 84))
        state = state.reshape((1, 84, 84))
        return state
    
    def action(self, act):
        return act
    
    def step(self, act):
        state, reward, done, _ = super().step(act)
        state = np.array(state)
        state = state.mean(axis=2)
        state = np.resize(state, (84, 84))
        state = state.reshape((1, 84, 84))
        return state, reward, done, _