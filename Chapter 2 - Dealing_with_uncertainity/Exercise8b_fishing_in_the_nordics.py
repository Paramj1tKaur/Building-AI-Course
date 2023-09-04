""" Write a function that uses the given numbers and tries to guess the nationality of the winner when we know that the winner is a fisher and their gender (either female or male).
"""
import math
import random
import numpy as np
import io
from io import StringIO
countries = ['Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden']
populations = [5615000, 5439000, 324000, 5080000, 9609000]
male_fishers = [1822, 2575, 3400, 11291, 1731]
female_fishers = [69, 77, 400, 320, 26] 

def guess(winner_gender):
    guess = None
    biggest = 0.0
    if winner_gender == 'female':
        fishers = female_fishers
    else:
        fishers = male_fishers

    # write your solution here
    total_Population = 0
    for i in populations:
        total_Population += i
    fishers_Total = 0
    for i in fishers:
        fishers_Total += i
    
    for i in range(len(countries)):
        fraction = fishers[i] / fishers_Total * 100
        if fraction > biggest:
            biggest = fraction
            guess = countries[i]
    return (guess, biggest)  

def main():
    country, fraction = guess("male")
    print("if the winner is male, my guess is he's from %s; probability %.2f%%" % (country, fraction))
    country, fraction = guess("female")
    print("if the winner is female, my guess is she's from %s; probability %.2f%%" % (country, fraction))

main()
