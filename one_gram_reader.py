import csv
import numpy as np

# This function will look into a file for a specific word and will return 2 lists
# The first list is a list of the years the word is found in within a given year range
# The second list is a list of the counts (number of times that the word appeared in any book that year.) for that word in that year range
def read_word_file(search_word, year_range, file_path):
    f = open(file_path, "r")
    years = []  # assigning both year and count to an empty list
    count = []

    for line in f:
        line = (line.split("\t"))  # splitting the line into a list using the /t as a delimiter

        if search_word in line and (int(line[1]) >= year_range[0] and int(line[1]) <= year_range[1]):
            # the above line is saying that if the word is in the line AND if in the line it's the appropriate year (if both these are true), you can go ahead to the next line
            years.append(int(line[1]))
            count.append(int(line[2]))  # adding the appropriate years and count to the empty list as it goes through the loop

    f.close()
    return years, count  # will return a list of years and count in integer form


# This function will go through a filename and return a dictionary of counts for the appropriate year
def read_total_counts(filename):
    f = open(filename, 'r')
    csv_reader = csv.reader(f, delimiter=',')  # letting python read the csv file
    counts = {}  # assigning counts as a dictionary

    for row in csv_reader:
        # in this for loop we're assigning the year in our dictionary counts and associating it with the #s from the 2nd column (total number of words recorded from all texts that year)
        year = int(row[0])
        counts[year] = int(row[1])

    f.close()
    return counts  # will return dictionary of counts


# This function will return a list of normalized version of counts using a list of years, list of counts and dictionary of counts for each year as the input
def normalize_counts(years, counts, total):
    norm_counts = []

    for i in range(len(years)):
        count_loop = counts[i]
        total_counts = total[years[i]]
        norm_counts.append(count_loop / total_counts)

    return norm_counts


# This function takes a csv file and returns a dictionary mapping words to a list of tuples containing the year the word is found in and the count
# the number of times the word appeared that year
def read_entire_word_file(word_file_path):
    f = open(word_file_path, 'r')
    csv_reader = csv.reader(f, delimiter="\t")

    word_tuple = {}

    for row in csv_reader:
        # iterating through the file and seperating out words, year and counts
        words = row[0]
        year = int(row[1])
        counts = int(row[2])

        # using the get function to initialize the the word(key in our dictionary)
        # to an empty list if it's not in our word_tuple dictionary. we then append
        # the tuple (year_counts) to the list and assign the word (key) to its
        # value (the list of tuples: year_counts)
        year_counts = year, counts
        yearcountlist = word_tuple.get(words, [])
        yearcountlist.append(year_counts)

        word_tuple[words] = yearcountlist

    f.close()
    return word_tuple


# This function takes the dictionary of words to tuples created by the first function and any word
# and returns the total number of times the word has appeared
def total_occurrences(word_data, word):
    total = 0
    for key in word_data:

        if key == word:
            # we are iterating through the values of the key
            # and summing the 2nd element of the tuple (which is the count) for that key
            for values in word_data[word]:
                total += values[1]
            return total
    else:
        return 0


#This function takes the dictionary of words to tuples created by the first function and returns a length
#of 26 where each element is frequency of the letters in the alphabet(0th is "a", 1st is "b" etc.)
def count_letters(word_data):
    sum_numer = [0] * 26
    add_denom = 0

    for key in word_data:
        # we need to divide (numerator: the total number of times >letter< occurs)/(denominator:total number of letters in all words)
        numer = []
        denom = len(key) * total_occurrences(word_data, key)  # formula for total #of letters in each key
        add_denom += denom  # summing up total # of letters for all keys, this is our denominator value

        for letter in "abcdefghijklmnopqrstuvwxyz":

            if letter in key:
                # if the letter is in the key we can count how many times the letter appears
                # we multply the count by total occurence, to get the total amount of times the letter occurs
                # we can append to an empty list. if the letter isn't there, we're just appending 0
                # each key will have a seperate list all of which have 26 elements for each letter
                count_letter = key.count(letter)
                numer.append(count_letter * total_occurrences(word_data, key))
            else:
                numer.append(0)

        sum_numer += np.array(numer)  # converting all the lists to an array so we can sum up all the lists

    numerator = (sum_numer)
    denominator = (add_denom)
    output = np.divide(numerator, denominator)  # now we're diving to get the output we want
    output = list(output)  # converting to a list

    return (output)