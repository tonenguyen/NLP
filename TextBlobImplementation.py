from textblob import TextBlob

# need to do a data check first
def getPolaritySubjectivity(data):
    #print(data)
    paragraphText = data
    sumPolarity = []
    sumSubjectivity = []
    for each in paragraphText:
        sumPolarity.append(TextBlob(each).sentiment.polarity)
        sumSubjectivity.append(TextBlob(each).sentiment.subjectivity)
    #print("sumPol", sumPolarity)
    return sumPolarity, sumSubjectivity

# give 1 if sum of all sentences(doc) >  0
getPolarityFromText = lambda text: 0.0 if sum(getPolaritySubjectivity(text)[0]) < 0 else 1.0

