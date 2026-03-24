from config import *

env = 
agent = 
agent.load(PATH)
agent.epsilon = 0.0   # No exploration

for episode in range(10):
    obs, info = env.reset()
    while True:
        action = agent.select_action(obs)
        obs, reward, terminated, truncated, info = env.step(action)
        if terminated or truncated:
            break