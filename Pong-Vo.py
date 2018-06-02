import gym
import cv2



env = gym.make("Pong-v1")

observation = env.reset()

for _ in range(1000):
  env.render()
  action = env.action_space.sample() # your agent here (this takes random actions)
  frame , reward, done, info = env.step(action)
  print(frame)

