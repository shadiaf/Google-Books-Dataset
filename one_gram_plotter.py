import matplotlib.pyplot as plt
import one_gram_reader
import numpy as np
import string

#This function will aid in returning a plot of the relative frequency of certain words over a span of specific years
def plot_words(words, year_range, word_file_path, totals_file_path):

    total = one_gram_reader.read_total_counts(totals_file_path)

    for i in words:

        years, counts = one_gram_reader.read_word_file(i, year_range , word_file_path)
        normalized_counts = one_gram_reader.normalize_counts(years, counts, total)
        plt.plot(years, normalized_counts, label=i)

    plt.xlabel("Years")
    plt.ylabel("Relative Frequency")
    plt.title("Shadia Farah")
    plt.grid()
    plt.legend()
    plt.show()

#This function will create a bar graph of the frequency of letters in a dictionary of word to tuples
def bar_plot_of_letter_frequencies(word_data):

    x = np.arange(26)
    value = one_gram_reader.count_letters(word_data)
    width = 1.0

    plt.xlabel("Letter")
    plt.ylabel("Total Count")
    plt.title("Shadia Farah")
    plt.bar(x, value, width, linewidth = 2, color='g', edgecolor='black')
    plt.autoscale(enable=True, axis='x', tight=True)
    plt.xticks(x, (string.ascii_lowercase))
    plt.show()