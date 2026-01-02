from underthesea import sent_tokenize
# open text
with open("1.txt", "r", encoding="utf-8") as file:
    one_text = file.read()

with open("2.txt", "r", encoding="utf-8") as file:
    two_text = file.read()

with open("3.txt", "r", encoding="utf-8") as file:
    three_text = file.read()

with open("4.txt", "r", encoding="utf-8") as file:
    four_text = file.read()

with open("5.txt", "r", encoding="utf-8") as file:
    five_text = file.read()


one_text = one_text.replace("\n", ". ")
two_text = two_text.replace("\n", ". ")
three_text = three_text.replace("\n", ". ")
four_text = four_text.replace("\n", ". ")
five_text = five_text.replace("\n", ". ")

# sentence tokenizing
one_sentences = sent_tokenize(one_text)
two_sentences = sent_tokenize(two_text)
three_sentences = sent_tokenize(three_text)
four_sentences = sent_tokenize(four_text)
five_sentences = sent_tokenize(five_text)
print("Tokenised sentences:")
sentences = [one_sentences,two_sentences,three_sentences,four_sentences,five_sentences]

for sentence in sentences:
  print(f"number of sentence: {len(sentence)}")

# word tokenising
from underthesea import word_tokenize
import re

def is_word(s):
    return re.sub(r"[^\w\s]", "", s)

one_wordtext = is_word(one_text)
one_words = word_tokenize(one_wordtext)
two_wordtext = is_word(two_text)
two_words = word_tokenize(two_wordtext)
three_wordtext = is_word(three_text)
three_words = word_tokenize(three_wordtext)
four_wordtext = is_word(four_text)
four_words = word_tokenize(four_wordtext)
five_wordtext = is_word(five_text)
five_words = word_tokenize(five_wordtext)


print("Các từ đã được tách:")
words = [one_words, two_words, three_words, four_words, five_words]
for word in words:
  print(f"number of word: {len(word)}")

# text normalisation
import re

def is_word(s):
    return re.sub(r"[^\w\s]", "", s)

one_normal = [is_word(text) for text in one_sentences]
two_normal = [is_word(text) for text in two_sentences]
three_normal = [is_word(text) for text in three_sentences]
four_normal = [is_word(text) for text in four_sentences]
five_normal = [is_word(text) for text in five_sentences]

print("Các câu đã được chuẩn hóa:")
sentence = [one_normal,two_normal,three_normal,four_normal, five_normal]
for sent in sentence:
  print('5 dòng đầu')
  print(sent[:5])
  print("-"*50)

# pos tagging
from underthesea import pos_tag

pos_one = pos_tag(one_text)
pos_two = pos_tag(two_text)
pos_three = pos_tag(three_text)
pos_four = pos_tag(four_text)
pos_five = pos_tag(five_text)

pos_tag = [pos_one, pos_two, pos_three, pos_four, pos_five]
print("Kết quả gắn nhãn từ loại:")
for pos in pos_tag:
  print(pos[:20])
  print("-"*50)

# text chunking
from underthesea import chunk

chunk_one = chunk(one_text)
chunk_two = chunk(two_text)
chunk_three = chunk(three_text)
chunk_four = chunk(four_text)
chunk_five = chunk(five_text)

chunks = [chunk_one, chunk_two, chunk_three, chunk_four, chunk_five]
print("Kết quả phân đoạn cụm từ:")
for chunk in chunks:
  print(chunk[:5])
  print("-"*50)

# name entity recognisation

from underthesea import ner

def classify(text):
  label_list = {
        'LOC': 'Location',
        'PER': 'Person',
        'ORG': 'Organization'
    }
  ner_result = ner(text)

  entities = []
  for item in ner_result:
      if len(item) >= 4:
          word, _, _, tag = item
          clean_tag = tag[2:] if tag.startswith(("B-","I-")) else tag
          if clean_tag in label_list:
            entities.append((label_list[clean_tag], word))

  for entity_type, entity in entities:
      print(entity_type, ":", entity)

for text in [one_text, two_text, three_text, four_text, five_text]:
  print("-"*50)
  classify(text)

