import gym
import random

# VARIABLES
env = gym.make('frozenLake-v0')
score = 0
env.reset()


print(env.observation_space) # which space the player is currently in
print(env.action_space) # actions the player can take

# 0 = left
# 1 = down
# 2 = right
# 3 = up
# obs, rew, done, info = env.step(env.action_space.sample()) # take an action
score = 0
for g in range(1000):
    env.reset()
    for i in range(10):
        obs, rew, done, info = env.step(random.randit(1,2))
        env.render()
        if done:
            break
            # scipy


global score
for i in range (numGames):
    obs, rew, done, info = env.step(randm.randint(1,2))


   en.rest()

print(score)