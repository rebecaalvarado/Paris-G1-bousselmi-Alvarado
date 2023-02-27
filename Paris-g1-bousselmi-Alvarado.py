

print( "hello from - rebeca")
print ("hello")
print("bye")
print ("hola I'm Anthony")

print("rajoute")

print("tryout 1")

import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#HEATMAP, Exercise 1.-------------------------------------------------------------
# Create a dataset
df = pd.DataFrame(np.random.random((5,5)), columns=["a","b","c","d","e"])
# numpy.random.random() is one of the function for doing random sampling in numpy. 
#It returns an array of specified shape and fills it with random floats in the half-open interval [0.0, 1.0).


# Default heatmap            ------- plot first heatmap
p1 = sns.heatmap(df)
