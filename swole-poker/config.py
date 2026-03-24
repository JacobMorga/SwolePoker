import gymnasium as gym
from gymnasium import spaces
import numpy as np

# Hyper-parameters
LEARNING_RATE = 1e-3
GAMMA = 0.99          # Discount factor
EPSILON_START = 1.0   # Exploration rate
EPSILON_END = 0.01
EPSILON_DECAY = 0.995
BATCH_SIZE = 64
BUFFER_SIZE = 10_000
NUM_EPISODES = 1000