#!/usr/bin/env python
# coding: utf-8

# ### This file will define the csv file we'll work with to select the movies and the function to select the movie to play hangman

# In[ ]:


#Let's define a function like in the previous version returns a word


# In[3]:


def cpu_choice(): 
    
    import pandas as pd
    movies = pd.read_csv("../dataset_hangman/movies.csv")
    movies.head()
    movies_list = movies.Film.tolist()
    
#List of the words used by the computer to use during the game
    movies_list
    
#The computer picks a word, converst the word onto a list with the different letters and displays the lenght

    import random
    word_choice = random.choice(movies_list)
    return word_choice


# In[4]:


word_choice = cpu_choice()

