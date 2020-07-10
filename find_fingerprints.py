#!/usr/bin/env python
# coding: utf-8

# In[15]:


import numpy as np

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

from scipy.ndimage.filters import maximum_filter
from scipy.ndimage.morphology import generate_binary_structure, binary_erosion
from scipy.ndimage.morphology import iterate_structure

get_ipython().run_line_magic('matplotlib', 'notebook')


# In[16]:


from numba import njit

# `@njit` "decorates" the `_peaks` function. This tells Numba to
# compile this function using the "low level virtual machine" (LLVM)
# compiler. The resulting object is a Python function that, when called,
# executes optimized machine code instead of the Python code
@njit
def _peaks(data_2d, rows, cols, amp_min):
    """
    A Numba-optimized 2-D peak-finding algorithm.
    
    Parameters
    ----------
    data_2d : numpy.ndarray, shape-(H, W)
        The 2D array of data in which local peaks will be detected.

    rows : numpy.ndarray, shape-(N,)
        The 0-centered row indices of the local neighborhood mask
    
    cols : numpy.ndarray, shape-(N,)
        The 0-centered column indices of the local neighborhood mask
        
    amp_min : float
        All amplitudes at and below this value are excluded from being local 
        peaks.
    
    Returns
    -------
    List[Tuple[int, int]]
        (row, col) index pair for each local peak location. 
    """
    peaks = []
    
    # iterate over the 2-D data in col-major order
    for c, r in np.ndindex(*data_2d.shape[::-1]):
        if data_2d[r, c] <= amp_min:
            continue

        for dr, dc in zip(rows, cols):
            # don't compare element (r, c) with itself
            if dr == 0 and dc == 0:
                continue

            # mirror over array boundary
            if not (0 <= r + dr < data_2d.shape[0]):
                dr *= -1

            # mirror over array boundary
            if not (0 <= c + dc < data_2d.shape[1]):
                dc *= -1

            if data_2d[r, c] < data_2d[r + dr, c + dc]:
                break
        else:
            peaks.append((r, c))
    return peaks


def local_peak_locations(data_2d, neighborhood, amp_min):
    """
    Defines a local neighborhood and finds the local peaks
    in the spectrogram, which must be larger than the specified `amp_min`.
    
    Parameters
    ----------
    data_2d : numpy.ndarray, shape-(H, W)
        The 2D array of data in which local peaks will be detected
    
    neighborhood : numpy.ndarray, shape-(h, w)
        A boolean mask indicating the "neighborhood" in which each
        datum will be assessed to determine whether or not it is
        a local peak. h and w must be odd-valued numbers
        
    amp_min : float
        All amplitudes at and below this value are excluded from being local 
        peaks.
    
    Returns
    -------
    List[Tuple[int, int]]
        (row, col) index pair for each local peak location.
    
    Notes
    -----
    The local peaks are returned in column-major order.
    """
    rows, cols = np.where(neighborhood)
    assert neighborhood.shape[0] % 2 == 1
    assert neighborhood.shape[1] % 2 == 1

    # center neighborhood indices around center of neighborhood
    rows -= neighborhood.shape[0] // 2
    cols -= neighborhood.shape[1] // 2
    
    return _peaks(data_2d, rows, cols, amp_min=amp_min)


# In[17]:


def fingerprint(data, fp, amp_min, fanout): 
    """
    Returns all fingerprints associated with a song
    
    Parameters
    ----------
    data : numpy.ndarray, shape-(H, W)
        The 2D array of data in which local peaks will be detected
    
    fp : numpy.ndarray, shape-(h, w)
        A boolean mask indicating the "neighborhood" in which each
        datum will be assessed to determine whether or not it is
        a local peak. h and w must be odd-valued numbers
        
    amp_min : float
        All amplitudes at and below this value are excluded from being local 
        peaks.
    
    fanout: int
        The fanout value
    
    Returns
    -------
    List[Tuple[Tuple[fm,fn,dt], tm]] 
        Contains all fingerprint values 
        
    
    """

    peaks = local_peak_locations(data,fp,amp_min) #List[Tuple[int, int]]

    fingerprints = []  #List[Tuple[Tuple[fm,fn,dt], tm]]
    
    
    print(len(peaks))

    for i in range(len(peaks)):
        fm = peaks[i][1]
        
        r = min(i + fanout, len(peaks))
        
        loop_over = [k for k in range(i+1,r)]
        
        for j in loop_over:

            fn = peaks[j][1]

            dt = peaks[j][0] - peaks[i][0]

            tm = peaks[i][0]
            
            
            insert = [tuple([fm,fn,dt]), tm]
            
            fingerprints.append(tuple(insert))
    
    
    return fingerprints 




        

        


# In[4]:





# In[18]:





# In[ ]:




