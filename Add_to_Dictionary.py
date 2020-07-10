#!/usr/bin/env python
# coding: utf-8

# In[4]:





# In[ ]:


database = {}
def add_to_dict(song_id, fanout_m):
    """
    Adds all fingerprints associated with a songs in a database based upon song_id
    
    Parameters
    ----------
    song_id: int
    
    fanout_m: List[Tuple[Tuple[fm,fn,dt], tm]]
        Contains all the fingerprints associated with a single song
    
    """
    

    for (fm, fn, dt), tm in fanout_m:
        
        if (fm, fn, dt) in database.keys():
            database[(fm, fn, dt)].append((song_id, tm))
            
        else:
            database[(fm, fn, dt)] = []
            database[(fm, fn, dt)].append((song_id, tm))

