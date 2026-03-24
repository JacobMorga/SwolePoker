from config import *

env = 
agent = 

for episode in range(NUM_EPISODES):
    obs, info = env.reset()
    total_reward = 0

    while True:
        action = agent.select_action(obs)
        next_obs, reward, terminated, truncated, info = env.step(action)
        agent.learn()
        obs = next_obs
        total_reward += reward

        if terminated or truncated:
            break

    if episode % 100 == 0:
        agent.save(f"models/model_ep{episode}.pt")