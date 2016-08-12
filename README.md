# Document Classification Example 

## Dependencies 
To run this script you will need the packages listed in `requirements.txt`. To install run 

```pip install -r requirments.txt``` 

in the command line. 

You will also need `jupyter notebook` and `python` installed. 

## Data
The data was filtered from this [dataset](https://www.reddit.com/r/datasets/comments/3bxlg7/i_have_every_publicly_available_reddit_comment/). 

To unzip the data, run `gunzip RC_2015-05.json`

If you would like data from Jan-April in addition to data from May, you can enter the following command in the git repo to grab data from the DSSG data mount:

```rsync -av USERNAME@BOX.dssg.io:/mnt/data/training/nlp_training/2015 .```

