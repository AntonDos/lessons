#  Напишите программу, которая принимает текст и выводит два слова:
#  наиболее часто встречающееся и самое длинное.

from collections import Counter

text = input("Insert text: ").split(", ")  # one enters text and  list created
#  text for input: Tom, Michael, Tom, Michael, Fredy, Jessica, Tom, Benjamin

most = Counter(text).most_common(1)
print("Most repeated word -", most)


# finding the longest word
longest = ""
for i in text:
    if len(i) > len(longest):
        longest = i
print('Longest word -', longest)
