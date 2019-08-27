
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer 
from nltk.corpus import wordnet

import re
import string
import Contractions_Words as contractions
import importlib
importlib.reload(contractions)

contractions_dict = contractions.contractions_dict

#print(contractions_dict.keys())
#print(contractions_dict["s***"])

pattern = '%s' % '|'.join(contractions_dict.keys())
#pattern = r"%s" % pattern
#print(pattern)
contractions_re = re.compile(pattern)
def expand_contractions(s, contractions_dict=contractions_dict):
    #edit for special case like s*** etc
    s = re.sub("\*", "#", s)
    def replace(match):
        #print(type(match), match)
        return contractions_dict[match.group(0)]
    return contractions_re.sub(replace, s)


lemmatizer = WordNetLemmatizer() 

# return both wholeText, paragraph Text
def simplifiedReviewCleanUp(sample):
    #print(sample)
    #sample = sample.decode("utf-8")
    sample = expand_contractions(sample)
    sample = sample.lower()
    
    #for word in sample:
    #    print(lemmatizer.lemmatize(word, wordnet.VERB))
    
    review = sent_tokenize(sample)
    #print(review)
    for count, eachSent in enumerate(review):
        #remove numbers
        #eachSent = re.sub("r'\d+/\d+|\d+|\$\d+.\d+", " ", eachSent)
        #remove string
        eachSent = re.sub('[%s]' % re.escape(string.punctuation), ' ', eachSent)
        review[count] = eachSent
    wholeText = [" ".join(review) ]
    paragraphText = review
    return paragraphText, wholeText

#paragraphText, wholeText = singleReviewCleanUp(sample)
#wholeText, paragraphText
#paragraphText

simplifiedTextParagraph = lambda text: simplifiedReviewCleanUp(text)[0]

