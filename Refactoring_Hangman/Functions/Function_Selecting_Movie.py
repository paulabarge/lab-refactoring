#!/usr/bin/env python
# coding: utf-8

# ### This file will define the csv file we'll work with to select the movies and the function to select the movie to play hangman

# In[8]:


#Instead of having a predefined list, let's work with csv file with movies. 

movies = pd.read_csv("../dataset_hangman/movies.csv")
movies.head()


# In[10]:


#Now that we have imported the dictionary, since we only care about the film title, lets put it in a list.

movies_list = movies.Film.tolist()
movies_list


# In[ ]:


#Let's define a function like in the previous version returns a word


# In[12]:


def cpu_choice(): 
#List of the words used by the computer to use during the game
    movies_list
#The computer picks a word, converst the word onto a list with the different letters and displays the lenght
    import random
    word_choice = random.choice(movies_list)
    return word_choice


# In[14]:


word_choice = cpu_choice()

