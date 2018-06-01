import gym
import numpy as np
import matplotlib.pyplot as plt
from gym import wrappers

num_episodes = 1000

def run_episode(env,Q,learning_rate,discount,episode,render=True):
    observation = env.reset()
    done = False
    t_reward = 0
    max_steps = env.spec.tags.get('wrapper_config.TimeLimit.max_episode_steps')
    for i in xrange(max_steps):
        if done:
            break
        if render:
            env.render()

        curr_state = observation

        action = np.argmax(Q[curr_state,:]  + np.random.randn(1, env.action_space.n)*(1./(episode+1)))

        observation, reward, done, info = env.step(action)

        t_reward += reward

        #Q(state, action) = R(state, action) + Gamma * Max[Q(next state, all actions)]

    return Q, t_reward

def train():
    env = gym.make('FrozenLake-v0')
    env = wrappers.Monitor(env, '/tmp/FrozenLake-experiment-6',force=True)
    learning_rate = 0.81
    discount = 0.96

    reward_per_ep = list()
    Q = np.zeros((env.observation_space.n, env.action_space.n))
    for i in xrange(num_episodes):
        Q,reward = run_episode(env,Q,learning_rate,discount,i)
        reward_per_ep.append(reward)
        #print "----------Next Episode---------"
        #print i
    plt.plot(reward_per_ep)
    
    return Q

q = train()
print q