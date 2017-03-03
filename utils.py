import ujson
import numpy as np
import matplotlib.pyplot as plt
import sys 

import os
import psutil

from sklearn.metrics import precision_recall_curve, roc_auc_score, roc_curve, auc
from collections import OrderedDict


def print_memory():
    """
    Function to print the total memory used in Gb
    """
    process = psutil.Process(os.getpid())
    print(process.memory_info().rss/1000000000)

def load_reddit(fname, ls_subreddits=[], MIN_CHAR=30):
    """
    Loads Reddit Comments from a json file based on 
    whether they are in the selected subreddits and 
    have more than the MIN_CHARACTERS
    
    Parameters
    ----------
    fname: str
        filename
    ls_subreddits: ls[str]
        list of subreddits to select from 
    MIN_CHAR: int
        minimum number of characters necessary to select
        a comment
        
    Returns
    -------
    corpus: ls[str]
        list of selected reddit comments
    subreddit_id: array[int]
        np.array of indices that match with the ls_subreddit
        index 
    """
    corpus = []
    subreddit_id = []
    with open(fname, 'r') as infile:
        for line in infile:
            dict_reddit_post =  ujson.loads(line)
            subreddit = dict_reddit_post['subreddit']
            n_characters = len( dict_reddit_post['body'] )
            
            if ls_subreddits: # check that the list is not empty
                in_ls_subreddits = subreddit in ls_subreddits
            else:
                in_ls_subreddits = True
            
            grter_than_min = n_characters > MIN_CHAR
            
            if ( grter_than_min and in_ls_subreddits ):
                corpus.append(dict_reddit_post['body'])
                subreddit_id.append(subreddit)
                
    return np.array(corpus), np.array(subreddit_id)


def plot_roc(y_true, y_score):
    """
    Plots the precision and recall as a function 
    of the percent of data for which we calculate 
    precision and recall 
    
        
    params:
        ytrue: 
        yprob_: 
        model_name: 
    
    """
    # Compute micro-average ROC curve and ROC area
    fpr, tpr, _ = roc_curve(y_true, y_score)
    roc_auc = roc_auc_score( y_true, y_score)
    
    
    plt.figure()
    lw = 2
    plt.plot(fpr, tpr, color='darkorange',
         lw=lw, label='ROC curve (area = %0.2f)' % roc_auc)
    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curve')
    plt.legend(loc="lower right")
    plt.show()


def print_variable_sizes(variables):
    """
    Function that prints all local variables and their sizes 
    """
    sorted_variables = OrderedDict( sorted(variables, key=lambda x: sys.getsizeof(x[1]), reverse=True) )
    
    for var, obj in sorted_variables.items():
        print(var, sys.getsizeof(obj)/1000000000)
