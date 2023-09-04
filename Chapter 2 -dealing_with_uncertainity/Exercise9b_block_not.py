""" Bayes - Block or not. Decide whether you should block the new follower using Bayes. where P(bot) is the probability of bot, p8_bot iis the probability of bot with eight digit  user name, and p8_human is the probability of human with eight digit  user name.
Program calculate and print out the probability of the new follower being a bot, P(bot | 8-digits).
"""
import math
import random
import numpy as np
import io
from io import StringIO
def bot8(pbot, p8_bot, p8_human):
    p_8 = p8_bot * pbot + p8_human * (1-pbot)
    pbot_8 = p8_bot * pbot/p_8
    print(pbot_8)
 
# you can change these values to test your program with different values
pbot = 0.1
p8_bot = 0.8
p8_human = 0.05

bot8(pbot, p8_bot, p8_human)