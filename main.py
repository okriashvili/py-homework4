# print("python 4th homework!!!!!!!")
#
# # დავალება 1:დაწერეთ პროგრამა, რომელიც მომხმარებელს შემოაყვანინებს წინადადებას,
# # პირველ სიტყვას და მეორე სიტყვას და შემოყვანილ წინადადებაში
# # პირველ სიტყვას ჩაანაცვლებს მეორე სიტყვით
#
# sentence = input("Enter sentence: ")
# word1 = input("Enter word you want to be replaced: ")
# word2 = input("Enter word which will replace the word1: ")
# replaced_sentnece = sentence.replace(word1, word2)
# print(replaced_sentnece)
#
#
# # დავალება 2: დაწერეთ პროგრამა, რომელიც მომხმარებლის მიერ შემოყვანილ წინადადებაში იპოვის ყველაზე გრძელ სიტყვას
# # და დაბეჭდავს მას. არ გამოიყენოთ max() ფუნქცია!
# sentence = input("Enter sentence: ")
# splited_sentence = sentence.split(" ")
#
# longest_words = ""
#
# for word in splited_sentence:
#     if len(word) > len(longest_words):
#         longest_words = word
# print(longest_words)




# # დავალება 3:დაწერეთ პროგრამა, რომელიც მომხმარებელს შეეკითხება ორ სიტყვას შეამოწმებს არის თუ არა ერთმანეთის ანაგრამა
# ანაგრამა არის ერთ სიტყვაში ასოების გადაადგილებით მიღებული მეორე სიტყვა,
# მაგალითად ("listen", "silent" ), ("Triangle", "Integral")
# და ა.შ. უნდა იყოს case-insensitive, ანუ მომხმარებელი დიდი ასოებით შემოიყვანს თუ არა ტექსტს,
# არ უნდა ჰქონდეს მნიშვნელობა. და არ გამოიყენოთ sorted() ფუნქცია.


# text1 = input("Enter text: ").lower()
# text2 = input("Enter text: ").lower()
# text1_len = ""
# text2_len = ""
# if len(text1_len) < len(text2_len):
#     print("არაა ანაგრამა")
#
# i = 0
# while i < len(text1_len):
#     i=+1
#     j = 0
#     while j < len(text2_len):
#         j=+1
#         if text1_len[i] == text2_len[j]:
#             print("ანაგრამა")
#
# # split_text1 = text1.split()
# # split_text2 = text2.split()







# Input from user
text1 = input("Enter first word: ").lower()
text2 = input("Enter second word: ").lower()

# Remove spaces (optional for phrases)
new_text1 = ""
new_text2 = ""

i = 0
while i < len(text1):
    if text1[i] != " ":
        new_text1 = new_text1 + text1[i]
    i = i + 1

i = 0
while i < len(text2):
    if text2[i] != " ":
        new_text2 = new_text2 + text2[i]
    i = i + 1

if len(new_text1) != len(new_text2):
    print("არაა ანაგრამა")
else:
    i = 0
    is_anagram = True

    while i < len(new_text1):
        letter_count = False
        j = 0
        while j < len(new_text2):
            if new_text1[i] == new_text2[j]:
                # Remove letter from temp_text2 (simulate using slicing)
                new_text2 = new_text2[:j] + new_text2[j+1:]
                letter_count = True
                break
            j = j + 1
        if not letter_count:
            is_anagram = False
            break
        i = i + 1

    if is_anagram:
        print("ანაგრამებია")
    else:
        print("არაა ანაგრამა")
































