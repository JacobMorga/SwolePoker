from config import *

class poker_env(gym.Env):

    def __init__(self, render_mode=None):
        super().__init__()

        # Define action and observation spaces (REQUIRED)
        self.action_space = spaces.
        self.observation_space = spaces.

        self.render_mode = render_mode

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)  # Important: seeds self.np_random

        obs = self._get_obs()   # Your method to build obs
        info = self._get_info()         # Auxiliary diagnostic info (dict)

        return obs, info
    
    def step(self, action):

        # update env

        terminated = bool(self._agent_pos == self._target)  # Natural end (goal reached, died)
        truncated = False   # Hit time limit 
        reward = 
        obs = self._get_obs()
        info = self._get_info()

        return obs, reward, terminated, truncated, info
    
    def _get_obs(self):
        return obs
    
    def _get_info(self):
        return info
    
    def render(self):
        if self.render_mode == "human":
            # Draw to screen (pygame, etc.)
            pass
        elif self.render_mode == "rgb_array":
            return np.zeros((84, 84, 3), dtype=np.uint8)  # Return pixel array