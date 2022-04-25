#!/usr/bin/env python
# coding: utf-8

# # Anogram 
# ## Libenathi Mlindi

# In[ ]:





# In[7]:


# A python program to print all anagrams together
# Structure for each word of duplicate array


class word(object):
    def __init__(self,string,index):
        self.string = string
        self.index = index
        
# create a DupArrray object that contains an array
# of words

def createDupArray(string,size):
    dupArray = []
    
    # one by one copy words from the given wordArray
    # to dupArray
    for i in xrange(size):
        dupArray.append(word(string[i],i))
    return dupArray



def printAnagramsTogether(wordArr,Size):
    # a copy of all words present in WordArr
    dupArray = createDupArray(WordArr,size) 
    # iterating through all words in dupArray and sort individual words
    for i in xrange(size):
        dupArray[i].string = '' .join(sorted(dupArray[i].string))
        
    # Sorts the array of words in dupArray
    dubArray = sorted(dupArray, key =lambda k: k.string)
    
    # Instructing to get corresponding original word
    for word in dupArray:
        print( wordArr[word.index])
        


        
    


# ### Driver Program

# In[ ]:


WordArr = ['cat','dog','tac','God','act']
size = len(wordArr)
printAnagramsTogether(wordArr,size


# In[ ]:





# In[ ]:




