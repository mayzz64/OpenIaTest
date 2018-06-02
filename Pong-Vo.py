import gym
#import cv2
import numpy 


env = gym.make("Pong-v0")

observation = env.reset()

for _ in range(1000):
  env.render()
  action = env.action_space.sample() # your agent here (this takes random actions)
  frame , reward, done, info = env.step(action)
  arr = np.array(frame)
  print(frame.shape)

