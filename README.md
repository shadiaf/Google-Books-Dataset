# Google-Books-Dataset

An Ngram is defined simply as a sequence of N contiguous items. Given a text, we can count all of the 1grams, 2grams, 3grams, etc that appear in the text. The N refers to the number of items in the Ngram.

Ngram frequencies are useful because they provide a quantitative measure of which items tend to follow others in a certain data domain. Ngrams are used heavily in statistical processing of natural languages or other strings. For example, you can use Ngram frequencies to identify what language a particular text comes from. Similarly, you can use them to identify which species a given sequence comes from.

In this project, I will be working with only 1grams of words. Given a text, and assuming we care about the words (as opposed to the letters, or syllables, or whatever else), the set of 1grams is just the set of words that appear in the text (with disregard to whitespace).

### One_gram_reader.py:

1) read_word_file: the first function will read a tab delimited file and return the number of times that a given word has appeared in all (evaluted)texts throughout history. For example, the word "wandered" appeared 108634 times during the year 2007. This can be tested using the file very_short.txt

2) read_total_counts: The second function will read a comma separated file (CSV) and return the total number of words collected from all sources for a given year. For example, Google counted a total of 16,206,118,071 English words in 2007. It will essentially return a dictionary of counts for the appropriate year. This can be tested using total_counts.csv. 

3) normalize_counts: This function will return a list of normalized version of counts using a list of years, list of counts and dictionary of counts for each year as the input. 
  The inputs are: 
      * years: A list of years as returned by the one_gram_reader.read_word_file()
      * counts: A list of counts, same as returned by the one_gram_reader.read_word_file()
      * total: A dictionary of counts for each year, same as returned by your one_gram_reader.read_total_counts
      
4) read_entire_word_file:  Returns the counts and years for all words. More specifically this function takes a csv file and returns a dictionary mapping words to a list of tuples containing the year the word is found in and the count the number of times the word appeared that year
  The inputs are:
      * word_file_path: A string giving the file path of a one_gram csv file. I used "data/very_short.txt" as an example

5) total_occurrences: Returns total occurrences of word. More specifically this function takes the dictionary of words to tuples created by the first function and any word and returns the total number of times the word has appeared. 
  The inputs are:
      * word_data: A dictionary of word to tuples created by read_entire_word_file. 
        for example: word_data = read_entire_word_file("data/very_short.txt").
      * word: An English word. Not guaranteed to exist in word_data.
        for example: total_occurrences(word_data, "quetzalcoatl") or total_occurrences(word_data, "wandered")

6) count_letters:  Returns a list of length 26 corresponding to letter frequencies. More specifically, this function takes the dictionary of words to tuples created by the first function and returns a length of 26 where each element is frequency of the letters in the alphabet (0th is "a", 1st is "b" etc.)
     The inputs are: 
       * word_data: A dictionary of word to tuples created by read_entire_word_file. 
        for example: word_data = read_entire_word_file("data/very_short.txt").


### One_gram_plotter: 

In this file, we will create functions that will return plots to help us visualize daya. 

1) plot_words: This function will aid in returning a plot of the relative frequency of certain words over a span of specific years.
  The inputs are: 
      * words: A list of words to calculate normalized counts for and then plot. 
      * year_range: A list of 2 numbers defining the year range we are interested in
      * word_file: Name of the word txt file (all_words.text) (This file was too big to attach here) 
      * total_file: Name of the totals csv file (total_counts.csv)
      
  example: 
  plot_words(["horse", "fish", "dog"], [1800, 2000], "data/all_words.txt", "data/total_counts.csv")
  
2) bar_plot_of_letter_frequencies: This function will create a bar graph of the frequency of letters in a dictionary of word to tuples. 
     The inputs are: 
       * word_data: A dictionary of word to tuples created by read_entire_word_file. 
        for example: word_data = read_entire_word_file("data/very_short.txt").


