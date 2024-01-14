# Write a Python program that takes a text file as input and returns the number of words of a given text file.
# def count_words(fileName):
#     with open(fileName) as f:
#         data = f.read()
#         return len(data.split())
#
# f = open("demo.txt", "r")
# print(f.read())
# print()
# print("There are", count_words("demo.txt"), " words in the file")
# f.close()


# Write a Python program to count the frequency of words in a file.
# from collections import Counter
# def word_count(fileName):
#     with open(fileName) as f:
#         return Counter(f.read().split())
#
# f = open("demo.txt", "r")
# print(f.read())
# print()
# print("Number of words:", word_count("demo.txt"))
# f.close()


# Write a Python program to count the number of lines in a text file.
# def file_lengthy(fileName):
#     with open(fileName) as f:
#         for i, l in enumerate(f):
#             print(l, end="")
#
#     return i + 1
#
# print("\nNumber of lines in the file:", file_lengthy("demo.txt"))


# Write a python program to find the longest words.
# def longest_word(fileName):
#     with open(fileName, 'r') as infile:
#         words = infile.read().split()
#     max_len = len(max(words, key=len))
#     return [word for word in words if len(word) == max_len]
#
# f = open("demo.txt", "r")
# print(f.read())
# print()
# print("The longest word is/are:",longest_word("demo.txt"))
# f.close()