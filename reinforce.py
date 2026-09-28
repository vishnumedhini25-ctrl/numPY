import random

actions = ["Left", "Right"]

for i in range(10):

    action = random.choice(actions)

    if action == "Right":
        reward = 1
    else:
        reward = -1

    print("Action:", action)
    print("Reward:", reward)