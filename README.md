<!-- This is the markdown template for the final project of the Building AI course, 
created by Reaktor Innovations and University of Helsinki. 
Copy the template, paste it to your GitHub README and edit! -->

#  Building AI Course
This repository contains my python code files from [A free online course - Elements of A](https://buildingai.elementsofai.com/). This course has five chapters.
1.	Getting started with AI
3.	Dealing with uncertainty
4.	Machine learning
5.	Neural Networks
6.	Conclusion


## 1. Getting started with AI

[Exercise: 1a listing_pineapple_routes](https://github.com/Paramj1tKaur/Building-AI-Course/blob/main/Chapter%201%20-getting_started/Exercise1a_listing_pineapple_routes.py) <br>
[Exercise: 1b listing_pineapple_routes](https://github.com/Paramj1tKaur/Building-AI-Course/blob/main/Chapter%201%20-getting_started/Exercise1b_listing_pineapple_routes.py)

[Exercise: 2a Pineapple_routes_emissions](https://github.com/Paramj1tKaur/Building-AI-Course/blob/main/Chapter%201%20-getting_started/Exercise2a_pineapple_routes_emissions.py)  <br>
[Exercise:2b Pineapple_routes_emissions](https://github.com/Paramj1tKaur/Building-AI-Course/blob/main/Chapter%201%20-getting_started/Exercise2b_pineapple_routes_emissions.py)


### Hill Climbing
Example 3 Intermediary: Reach the highest summit <br>
Example 3 Advance:  Reach the highest summit
https://github.com/Paramj1tKaur/Building-AI-Course/blob/main/Chapter%201%20-getting_started/Exercise1a_listing_pineapple_routes.py

Example 4 Intermediary: Probabilities <br>
Example 4 Advance: Probabilities

Example 5 Intermediary: Warn-up Temprature <br>
Example 5 Advance:  Warn-up Temprature

Example 6 Intermediary: Simulated Annealing <br>
[Example 6 Advance:  Simulated Annealing](./docs/README.md)

[Link to Exercise](./Exercise)






Example 6
```
Example 6 Intermediary: Simulated Annealing
import math
import random
import numpy as np
import io
from io import StringIO
import math
import random             	# just for generating random mountains                                 	 

# generate random mountains                                                                               	 
w = [random.random()/3, random.random()/3, random.random()/3]
h = [1.+math.sin(1+x/6.)*w[0]+math.sin(-.3+x/9.)*w[1]+math.sin(-.2+x/30.)*w[2] for x in range(100)]
h[0] = 0.0; h[99] = 0.0

def climb(x, h):
    # keep climbing until we've found a summit
    summit = False

    # edit here
    while not summit:
        summit = True         # stop unless there's a way up
        if h[x + 1] > h[x]:
            x = x + 1         # right is higher, go there
            summit = False    # and keep going
        elif  h[x - 1] > h[x]:
            x = x - 1         # left is higher, go there
            summit = False    # and keep going
    return x


def main(h):

    # start at a random place                                                                                  	 
    x0 = random.randint(1, 98)
    x = climb(x0, h)

    print("Venla started at %d and got to %d" % (x0, x))
    return x0, x

main(h)
```

```
Example 6 Advanced: Simulated Annealing CHECK
import math
import random
import numpy as np
import io
from io import StringIO
import math
import random             	# just for generating random mountains                                 	 

# generate random mountains                                                                               	 

w = [.05, random.random()/3, random.random()/3]
h = [1.+math.sin(1+x/.6)*w[0]+math.sin(-.3+x/9.)*w[1]+math.sin(-.2+x/30.)*w[2] for x in range(100)]

def climb(x, h):
    # keep climbing until we've found a summit
    summit = False
    while not summit:
        summit = True  # stop unless there's a way up
        for i in range(5):
            if x + i < 100 and x + i >= 0:
                if h[x + i] > h[x]:
                    x = x + i  # right is higher, go there
                    summit = False  # and keep going
                    break
    return x


def main(h):
    # start at a random place                                                                                  	 
    x0 = random.randint(1, 98)
    x = climb(x0, h)

    return x0, x

main(h)
```



## Data sources and AI methods
Where does your data come from? Do you collect it yourself or do you use data collected by someone else?
If you need to use links, here's an example:
[Twitter API](https://developer.twitter.com/en/docs)

| Syntax      | Description |
| ----------- | ----------- |
| Header      | Title       |
| Paragraph   | Text        |

## Challenges

What does your project _not_ solve? Which limitations and ethical considerations should be taken into account when deploying a solution like this?

## What next?

How could your project grow and become something even more? What kind of skills, what kind of assistance would you  need to move on? 


## Acknowledgments

* list here the sources of inspiration 
* do not use code, images, data etc. from others without permission
* when you have permission to use other people's materials, always mention the original creator and the open source / Creative Commons licence they've used
  <br>For example: [Sleeping Cat on Her Back by Umberto Salvagnin](https://commons.wikimedia.org/wiki/File:Sleeping_cat_on_her_back.jpg#filelinks) / [CC BY 2.0](https://creativecommons.org/licenses/by/2.0)
* etc

## How is it used?

Describe the process of using the solution. In what kind situations is the solution needed (environment, time, etc.)? Who are the users, what kinds of needs should be taken into account?

Images will make your README look nice!
Once you upload an image to your repository, you can link link to it like this (replace the URL with file path, if you've uploaded an image to Github.)
![Cat](https://upload.wikimedia.org/wikipedia/commons/5/5e/Sleeping_cat_on_her_back.jpg)

If you need to resize images, you have to use an HTML tag, like this:
<img src="https://upload.wikimedia.org/wikipedia/commons/5/5e/Sleeping_cat_on_her_back.jpg" width="300">
