# Random-Word-Processor
A Python-based tool that randomly generates 1000 conjunctions of letters and verifies whether they are English Words

# Project Notes and Step by Step Thinking:

### Organisation of Code:

1. I plan to organise my document in terms of my imports, functions and then the call of the function. The majority of the code should be contained within the main function that performs  the operations of the list of numbers themselves. ( Future projects can focus on the choice of using multiple or 1 main function to streamline this entire process). 

### Random Word Generator:

1. Initial Idea:

```python
words = [''.join(random.choices(string.ascii_letters, k = random.randint(1,6))) for x in range(1000)]
```

I have decided to adapt the NLP processing project a bit by making it a little more interesting and challenging than what I had set out for myself to practice. I decided to generate a random conjunctions of characters from 1 to 6 letters as this is what most words in the english language would sit between. Then I generated 1000 of these in a **list comprehension** to split them and allow them to be analysed. 

1. Secondary Development of Idea: 

After observing in the console the general problem with just generating random words from .ascii_letters - that the majority of the results are not words rather than words. Due to this I have had to include some conditions in the generating of the words. Instead of using the ASCI Letters call from before, I defined a string which seggregated letters into 3 different groups: vowels, regular consonatns and rare consonants. 

cont = 'aeiouAEIOUbcdfghjklmnprstBCDFGHJKLMNPRSTqvwxyzQVWXYZ' 

This was to be able to attach probability weights within the random function to sift through the prescribed normal characters and derive a higher likelihood of yielding actually words. The result was pretty successful, as including the probability weights for each section ( vowels: 0.6, regular consonants: 0.35, rare consonants: 0.05) ensured that most words contained the most common letters. 

The List comprehension to generate the list can be seen here: 
[''.join(random.choices(cont, weights = dd, k = random.randint(1,6))) for x in range(1000)] 

Where dd is a list containing the probability for the string cont variable storing the ordered letters from ASCII letters. 

So to formally list out the sequence of events: 

1. Words will be generated as per usual - increasing the probabilities of vowels to increase in the occurrence of actual words. Weighted probabilities will even be added to discriminate against x, y, z and other uncommon letter from ascii_letters. 
2. Words will then be extracted and compared to the total set of words imported from the natural language toolkit.
3. Words will also pass through an alogrithim in the above process which analyses certain words that are not natural in the english dictionary from the natural language toolkit. If the word only has 1 spelling mistake, it can be added to the final sorted list with a correction to that mistake. Similarly, for words over 3 characters in length, the algorithim can identify 2 spelling mistakes and submit the correct version of such words. 
5. Based on the results, a probability summary will be printed in the console displaying the results with adequate formatting. 

### Natural Language Toolkit import:

```python
#Imports
import nltk 
from nltk.corpus import words 

#Downloading
nltk.download('words')
 

#Loading the English dictionary 
english_words = set(words.words())
```

This was the solution elected to verify words, as a **set** containing the 235,000 english words in the natural language toolkit, to easily and quickly check generated words against the ones in the set. 

### Errors with Loading the Toolkit:

```python
(.venv) noahpeter@Noahs-MBP-2 Text Processor for NLP % "/Users/noahpeter/Desktop/VSCodeDirectory/Text Processor for NL
P/.venv/bin/python" "/Users/noahpeter/Desktop/VSCodeDirectory/Text Processor for NLP/# Text Processor for NLP.py"
[nltk_data] Error loading words: <urlopen error [SSL:
[nltk_data]     CERTIFICATE_VERIFY_FAILED] certificate verify failed:
[nltk_data]     unable to get local issuer certificate (_ssl.c:992)>
Traceback (most recent call last):
  File "/Users/noahpeter/Desktop/VSCodeDirectory/Text Processor for NLP/.venv/lib/python3.11/site-packages/nltk/corpus/util.py", line 84, in __load
    root = nltk.data.find(f"{self.subdir}/{zip_name}")
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/noahpeter/Desktop/VSCodeDirectory/Text Processor for NLP/.venv/lib/python3.11/site-packages/nltk/data.py", line 579, in find
    raise LookupError(resource_not_found)
LookupError: 
**********************************************************************
  Resource words not found.
  Please use the NLTK Downloader to obtain the resource:

  >>> import nltk
  >>> nltk.download('words')
  
  For more information see: https://www.nltk.org/data.html

  Attempted to load corpora/words.zip/words/

  Searched in:
    - '/Users/noahpeter/nltk_data'
    - '/Users/noahpeter/Desktop/VSCodeDirectory/Text Processor for NLP/.venv/nltk_data'
    - '/Users/noahpeter/Desktop/VSCodeDirectory/Text Processor for NLP/.venv/share/nltk_data'
    - '/Users/noahpeter/Desktop/VSCodeDirectory/Text Processor for NLP/.venv/lib/nltk_data'
    - '/usr/share/nltk_data'
    - '/usr/local/share/nltk_data'
    - '/usr/lib/nltk_data'
    - '/usr/local/lib/nltk_data'
**********************************************************************

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/noahpeter/Desktop/VSCodeDirectory/Text Processor for NLP/# Text Processor for NLP.py", line 11, in <module>
    english_words = set(words.words())
                        ^^^^^^^^^^^
  File "/Users/noahpeter/Desktop/VSCodeDirectory/Text Processor for NLP/.venv/lib/python3.11/site-packages/nltk/corpus/util.py", line 120, in __getattr__
    self.__load()
  File "/Users/noahpeter/Desktop/VSCodeDirectory/Text Processor for NLP/.venv/lib/python3.11/site-packages/nltk/corpus/util.py", line 86, in __load
    raise e
  File "/Users/noahpeter/Desktop/VSCodeDirectory/Text Processor for NLP/.venv/lib/python3.11/site-packages/nltk/corpus/util.py", line 81, in __load
    root = nltk.data.find(f"{self.subdir}/{self.__name}")
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/noahpeter/Desktop/VSCodeDirectory/Text Processor for NLP/.venv/lib/python3.11/site-packages/nltk/data.py", line 579, in find
    raise LookupError(resource_not_found)
LookupError: 
**********************************************************************
  Resource words not found.
  Please use the NLTK Downloader to obtain the resource:

  >>> import nltk
  >>> nltk.download('words')
  
  For more information see: https://www.nltk.org/data.html

  Attempted to load corpora/words

  Searched in:
    - '/Users/noahpeter/nltk_data'
    - '/Users/noahpeter/Desktop/VSCodeDirectory/Text Processor for NLP/.venv/nltk_data'
    - '/Users/noahpeter/Desktop/VSCodeDirectory/Text Processor for NLP/.venv/share/nltk_data'
    - '/Users/noahpeter/Desktop/VSCodeDirectory/Text Processor for NLP/.venv/lib/nltk_data'
    - '/usr/share/nltk_data'
    - '/usr/local/share/nltk_data'
    - '/usr/lib/nltk_data'
    - '/usr/local/lib/nltk_data'
**********************************************************************
```

### Errors with finding too many word matches for words with mistakes:

```python
#Container: 
container_example = ['em', 'hk', 'ose', 'jay', 'sk', ...]

else: 
            for word2 in english_words:
                if len(word1) == len(word2):
                    j = 0
                    for i in range(len(word1)):
                        if word1[i] == word2[i]:
                            j += 1
                    if j == len(word1) -1:
                        source_words.append(word2)
                      
#Console: 
['ha', 'Ok', 'ho', 'ak', 'hi', 'he', ...]
```

From the above we can see that when words are matched with the same length as hk in this example there are multiple different words fit the condition of only differing by one character. So instead without implementing algorithims which specify the specific intended word that was misspelt we can just select one word instead of the misspelt word. 

The fix was actually suprisingly easy: I managed to resolve this issue and just append the first word that came up in the dictionary set by using the break keyword after appending to move onto the next word in the dictionary:

```python
#Container: 
container_example = ['em', 'hk', 'ose', 'jay', 'sk', ...]

else: 
            for word2 in english_words:
                if len(word1) == len(word2):
                    j = 0
                    for i in range(len(word1)):
                        if word1[i] == word2[i]:
                            j += 1
                    if j == len(word1) -1:
                        source_words.append(word2)
                        p_e += 1
                        break
#Output: 
['em', 'Ok', 'ose', 'jay', 'Ok', ..] 
```

Although we are including duplicates within the output array this is ok, as the application that this project would pertain to should respect text based entries where there is a presence of repeated characters. 

It is also important that I point out here that especially for words with lower amounts of characters, a potential pitfall for this algorithim chosen was that not necessarily unique words are being chosen to replace the words 'spelt incorrectly'. This can be illustrated by an example and analysing the over simple logic reasoning that the algorithim incorporates:
E.G. Generated word with mistake = 'mk'
List of potential words it could have been = 'ok, me, my, etc' 
This, however, is trivial as the process is almost entirely random so an underlying intention for correctly spelling a word is not neccessary for this process. 

### Potential Improvements for the Project: 

1. I would defintely say that a system to only accept commonly used words, or words defined in English speech as there was a prevalence of accepting words like: 'un, ubi, ur' that are not words used in everyday english and hence are not relevant to the sourcing of the experiment. So a system should take generated words and only accept those which can be readily accepted and understood by humans - to accurately reflect words spelt correctly.

2. Creating that can spell words more efficiently and correctly - but then the purpose becomes what is this for?

3. Extending the generator sequence to something similar to a LLM which generates stories or texts and can be evaluated for topic accuracy, spelling accuracy, explanation clarity, etc. 
