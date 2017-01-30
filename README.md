# Document Classification Example 

You can install the required programs using either `pip` or `anaconda`

## Anaconda 

This is the recommended was of installation for users newer to python, or those that have not used pip.    

[Anaconda](https://www.continuum.io/downloads) should have all required modules. After installing Anaconda, run 

```conda update conda```    
to update all modules. It may also help to specifically update scikit-learn by running    
```conda update scikit-learn```
 
## Pip 
To run this script you will need the packages listed in `requirements.txt`. To install run 

```pip install -r requirments.txt``` 
in the command line. 

You will also need `python` installed. The notebook will run with versions 3.5 and 2.9.

## Data
The data was filtered from this [dataset](https://www.reddit.com/r/datasets/comments/3bxlg7/i_have_every_publicly_available_reddit_comment/). 

To unzip the data, run ```gunzip RC_2015-05.json.gz```

#If you would like data from Jan-April in addition to data from May, you can enter the following command from the cloned repository to grab data from the DSSG data mount:

#```rsync -av USERNAME@BOX.dssg.io:/mnt/data/training/nlp_training/2015 .```

