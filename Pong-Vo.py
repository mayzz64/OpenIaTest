import gym
import numpy as np 

def to_grayscale(img):
    return np.mean(img,axis=2).astype(np.uint8)
  
env = gym.make("Pong-v1")

observation = env.reset()

for _ in range(1000):
  env.render()
  action = env.action_space.sample() # your agent here (this takes random actions)
  frame , reward, done, info = env.step(action)
  img = np.array(to_grayscale(frame))
  print(frame.shape)

