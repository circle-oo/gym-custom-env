import gym
import numpy as np

class _Env:
    def __init__(self, name, render):
        self._env_name = name
        self.env = gym.make(self._env_name)
        self.render = render
        self.action_number = None
        self.state_number = None

    def reset(self):
        self.env.reset()
    
    def action(self, act):
        return act

    def step(self, act):
        if self.render == True:
            self.env.render()
        state, reward, done, _ = self.env.step(self.action(act))
        return state, reward, done, _