# Introduction to Natural Language Processing  

Natural language processing (NLP) refers to the methods and technologies used to allow computers to process, understand, and perform tasks using human language. 
Common NLP tasks include sentiment analysis, part-of-speech tagging, named entity recognition, machine translation, document classification, clustering, and topic extraction.
This course will introduce fundamental concepts in NLP including word and document representation, text processing, document classification, document similarity, and clustering, and dimensionality reduction. 
The course will be taught using jupyter notebooks in python. NLP tools covered will be sci-kit learn and ntlk. 

**Who:** This course is targeted primarily at graduate students and researchers who have some experience with machine learning and python, but are new to NLP.  

**Requirements:** Participants must bring a laptop with a few specific software packages installed (see [Pre-Workshop Instructions](#Instructions)). 

**Prerequisites:** A previous course in programming is strongly recommended. Experience with basic machine learning is recommended. 

**Contact**: Please mail [ggaut@uci.edu](mailto:ggaut@.edu) for more information.

* * *


## <a name="Schedule"></a>Tentative Schedule

| Time               |               |
| ------------- |:-------------:|
| 8:30-9:00   | Sign-in (coffee & bagels)     |
| 9:00-10:30   | **Text Processing and Document Classification**          |
| 10:30 - 10:45 | Break         |
| 10:45-12:30   | **Document Similarity and Clustering**          |
| 12:30-1:00    | Lunch            |

* * *

## <a name="Syllabus"></a>Syllabus

1. Introduction/Preparation
  * Common NLP Tasks 
  * Word and Document Representation
  * Text Processing 
2. Document Classification
  * Text Processing 
  * TFIDF
  * Evaluation 
3. Clustering 
  * Document Similartiy  
4. Dimensionality Reduction  
  * Topic Modeling 
  * Visualization 
 
* * *

## <a name="Instructions"></a>Pre-Workshop Instructions

You can install the required programs using either `pip` or `anaconda`

### Anaconda 

This is the recommended was of installation for users newer to python, or those that have not used pip.    

[Anaconda](https://www.continuum.io/downloads) should have all required modules. After installing Anaconda, run 

```conda update conda```    
to update all modules. It may also help to specifically update scikit-learn by running    
```conda update scikit-learn```
 
### Pip 
To run this script you will need the packages listed in `requirements.txt`. To install run 

```pip install -r requirments.txt``` 
in the command line. 

You will also need `python` installed. The notebook will run with versions 3.5 and 2.9.

## Data
The data was filtered from this [dataset](https://www.reddit.com/r/datasets/comments/3bxlg7/i_have_every_publicly_available_reddit_comment/). 

To unzip the data, run ```gunzip RC_2015-05.json.gz```

