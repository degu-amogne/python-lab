import string

def read_file(Group8):
    #This function does take File as an argument and read file content
    # also inside the function there are exception hanling it handle exceptions  
    try:
       with open(Group8, 'r' , encoding="utf-8") as f:
          return f.read()
    except FileNotFoundError:
        print(" ")
        print(f"Error: File {Group8} not found.")
        return ""
    except:
        print(f"Error: An unexpected error occurred while reading {Group8}.")
        return ""


def textCleaner(text):
    
    # Create a list of all special characters to remove
    special_chars = string.punctuation  
    # Iterate through the string and remove all special characters
    clean_text = ''
    for char in text:
        if char not in special_chars:
            clean_text += char
    return clean_text

def WordFrequencyCounter(text):
    
    words = text.split()#split text into list
    
    word_count = {}#we initialize empty dictionary
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
   # we use sorted() method for sorting words in decresing order
   # syntax of Sorted() method :-  sorted(iterable, key=None, reverse=False) 
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True) #function for sorrting
    

    # To display word and their frequency we use Lists 
    
    word_freq_list = []
    for word, count in sorted_words:
        word_freq_list.append((word, count))
        
    print(word_freq_list)

def CharacterFrequencyCounter(text):
    #First we initialize empty dictionary to store characters 
    char_count = {} 
    #In the below for loop it iterates through each character in the input text, 
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
   # we use sorted() method for sorting characters by their frequency 
   # syntax of Sorted() method :-  sorted(iterable, key=None, reverse=False)
    sorted_chars = sorted(char_count.items(), key=lambda x: x[1], reverse=True)
    
   #In the below for loop it print the first five characters and their frequencies 
   #also we use enumerate() method for iterate over a sequence Sorted Characters 
   # Sorted and have access to the index and the value of each element in the sequence.
    for i, (char, count) in enumerate(sorted_chars):
        if i < 6:
        
             if ( i == 0):
                continue
             print(f'{char}: {count}')

def main():
    Group8 = 'Group8.txt'
    text = read_file(Group8)
    text = textCleaner(text)
    
    print(" ")
    print("To display word and their frequency we use Lists ")
    print("Word frequency = ")
    WordFrequencyCounter(text)
    print("\nCharacter frequency = ")
    CharacterFrequencyCounter(text)
    print("\nStatistical Information From Writen File = ")
    print(" ")
    
    lines = text.count("\n") + 1

    #This code return the length of words from the given input
    words = len(text.split())

    #This code return the length of Characters from the given input
    characters = len(text)
    print("|Total lines: = ", lines)
    print("|Total words: = ", words)
    print("|Total characters: = ", characters)
    print(" ")

if __name__ == '__main__':
    main()