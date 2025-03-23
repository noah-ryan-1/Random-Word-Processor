#Imports: 
import re  
import random
import nltk
from nltk.corpus import words
from datetime import datetime

# Downloading the required NLTK Data:
nltk.download('words')

# Loading the English Dictionary: 
english_words = set(words.words())

# Main Function: 
def text_processor():
    #Generating Words and time
    text, time1 = random_text_generator()
    #Lowercase Conversion:
    processed = [text.lower() for text in text]
    #Removing non-vowel words
    processed = [ word for word in processed if re.search(r'[aeiou]', word)]
    #Removing single letters:
    processed = [ word for word in processed if len(word) > 1 ]
    lists, weights = dictionary_sourcing(processed)
    #Probability and Display section:
    return display_function(lists, weights, time1)
    


def dictionary_sourcing(cont):
    #Storage box for the sourced words 
    source_words = []
    #Number that will determine the quality of the generation by
    p_e = [0]*3
    for word1 in cont:
        #Add the word if it is an English word
        if word1 in english_words:
            source_words.append(word1)
            p_e[0] += 1 
        
        else:
            # Check for word with the same number of letters 
            for word2 in english_words:
                if len(word1) == len(word2):
                    j = 0
                    #Check how many similarities between sourced words and given generated word
                    for i in range(len(word1)):
                        if word1[i] == word2[i]:
                            j += 1
                    # Case 1: There is only 1 difference in the word        
                    if j == len(word1) -1:
                        source_words.append(word2)
                        p_e[1] += 1
                        break
                    # Case 2: There are 2 differences in the word (but also has to be over 3 letters to count)
                    if len(word1) > 3 and j == len(word1) -2:
                        source_words.append(word2)
                        p_e[2] += 1
                        break
    return source_words, p_e

def display_function(list, numbers, start):
    print(f"\n\n\n\n{'='*24}\n NLP Processing Results \n{'='*24}")
    print("\n --- Text Evaluation ---")
    print(f"\nFor the total number of generated random words: {1000:>13} (100.00%)")
    print(f'\nThe number of words after correction was: {len(list):>19} ({(len(list)/1000)*100:.2f}%)')
    print(f'\nThe number of correctly spelled english words were: {numbers[0]:>9} ({(numbers[0]/1000)*100:.2f}%)')
    print(f'\nThe number of words with 1 spelling mistake was: {numbers[1]:>12} ({(numbers[1]/1000)*100:.2f}%)')
    print(f'\nThe number of words with 2 spelling mistakes were: {numbers[2]:>10} ({(numbers[2]/1000)*100:.2f}%)')
    print(f'\n\nThe overall spelling weighted score of the generation: {(numbers[0]+numbers[0]*1/2+numbers[2]*1/4)/1000:>14.2f}%')
    end = datetime.now() 
    duration = str(end - start)[5:] 
    print(f'The total duration of the process took: {float(duration):>29.2f}s')
    print("\n --- Sample Tokenization ---\n")
    print(random.choices(list, k=15))
    print(f"\n\n{'*'*18}\n PROCESS COMPLETE \n{'*'*18}\n")
      
# Random text Generator Function:
def random_text_generator():
    initial_inference = datetime.now()
    print(f"{'='*26}\n Generating Random Words! \n{'='*26}")
    #Seperated Characters and Respective Probabilities:
    cont = 'aeiouAEIOUbcdfghjklmnprstBCDFGHJKLMNPRSTqvwxyzQVWXYZ'
    dd = [0.6]*10 + [0.35]*30 +[0.05]*12
    #Returned Random of 1000 Words with cont and dd distribution:
    return  [''.join(random.choices(cont, weights = dd, k = random.randint(1,6))) for x in range(1000)], initial_inference

#Starting the Process
text_processor()
