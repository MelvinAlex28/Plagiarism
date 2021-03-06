import re, math
import os
import sys
from collections import Counter
path = 'C:\xampp\htdocs\Plagiarism\new\files'

WORD = re.compile(r'\w+')

def get_cosine(vec1, vec2):
     intersection = set(vec1.keys()) & set(vec2.keys())
     numerator = sum([vec1[x] * vec2[x] for x in intersection])

     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)

     if not denominator:
        return 0.0
     else:
        return float(numerator) / denominator

def text_to_vector(text):
     words = WORD.findall(text)
     return Counter(words)


def get_input(file1,file2):

    fh = open(os.path.join(path,file1), "r")
    text1=fh.read()
    fh = open(os.path.join(path,file2), "r")
    text2=fh.read()
    return text1,text2






# text1 = 'This is a foo bar sentence .'
# text2 = 'This sentence is similar to a foo bar sentence .'

f1=sys.argv[1]
f2=sys.argv[2]

text1,text2=get_input(f1,f2)

vector1 = text_to_vector(text1)
vector2 = text_to_vector(text2)



cosine = get_cosine(vector1, vector2)

print 'Cosine:', cosine*100