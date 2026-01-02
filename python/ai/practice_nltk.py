import nltk
nltk.download('punkt_tab')  

nltk.download('all')

hamlet = nltk.corpus.gutenberg.words('shakespeare-hamlet.txt')
print(hamlet)

## WORD TOKENIZATION
from nltk.tokenize import word_tokenize
import re
words = word_tokenize(hamlet_text)

def is_word(s):
    return bool(re.fullmatch(r"[A-Za-z]+", s)) #filter word_only

words = [word for word in words if is_word(word)]
print(words[:20])
print(len(words))

## SENTENCE TOKENIZATION
from nltk.tokenize import sent_tokenize
hamlet_text = " ".join(hamlet)
sentences = sent_tokenize(hamlet_text)
print(sentences[:5])
print(len(sentences))

## STEMMING
word_list = [
    "running", "flies", "cats", "children", "better", "easily", "happier", "beautifully",
    "singing", "thinking", "faster", "studies", "studying", "builds", "builders", "bigger",
    "strongest", "funniest", "doing", "swimming", "friends", "walking", "played", "eating",
    "worked", "trying", "jumping", "flying", "houses", "mice", "babies", "prettier",
    "softly", "quickest", "saddest", "important", "nicest", "dogs", "programming",
    "machines", "learning", "teacher", "schools", "teaching", "quickly", "slowest",
    "happiest", "dancing", "watching", "easiest"
]

#PorterStemmer
from nltk.stem import PorterStemmer

print("PorterStemmer")
for word in word_list:
    print(word, ":", PorterStemmer().stem(word))

# LancasterStemmer
from nltk.stem import LancasterStemmer

print("LancasterStemmer")
for word in word_list:
    print(word,":", LancasterStemmer().stem(word))

## LEMMATIZATION

word_list = [
    "running", "flies", "cats", "children", "better", "easily", "happier", "beautifully",
    "singing", "thinking", "faster", "studies", "studying", "builds", "builders", "bigger",
    "strongest", "funniest", "doing", "swimming", "friends", "walking", "played", "eating",
    "worked", "trying", "jumping", "flying", "houses", "mice", "babies", "prettier",
    "softly", "quickest", "saddest", "important", "nicest", "dogs", "programming",
    "machines", "learning", "teacher", "schools", "teaching", "quickly", "slowest",
    "happiest", "dancing", "watching", "easiest"
]

from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
print("Lemmatizer")
for word in word_list:
    print(word,":", lemmatizer.lemmatize(word))


## STOP WORD

text = """
The world we live in is full of opportunities, but it is also full of challenges. And while we often think about success, we rarely consider the effort required to achieve it. If you look around, you will see that there are people who work hard every single day. They do not stop, even when the odds are against them. It is clear that resilience is important. You might wonder why some succeed while others do not, but the answer is simple: persistence. For those who continue to try, even after failure, success often comes eventually. With time, patience, and effort, almost anything is possible. This is why so many people emphasize the importance of not giving up. When you face obstacles, it is easy to feel discouraged. But that is when you must remind yourself of your goals. In moments of doubt, think about why you started. That alone can be enough to keep you moving forward.

It is also important to recognize that success is not a straight line. There are ups and downs, twists and turns, and moments of uncertainty. The journey is rarely ever smooth. But it is worth it. As you navigate life, you will encounter people who doubt you. They may say that you cannot do something, but you must not let them define your limits. Your potential is far greater than anyone else can imagine. And while it is good to listen to advice, you should also trust yourself. If you believe in yourself, you can accomplish more than you think. This is not just a motivational statement; it is a proven fact. The most successful people in history are those who refused to give up. By learning from their mistakes and continuing to push forward, they achieved greatness. At the heart of every success story is a person who chose to keep going, no matter how hard it got.

Of course, not everything will go according to plan. Sometimes, you will need to adapt. And that is okay. On the path to success, flexibility is key. When things go wrong, take a moment to reassess and adjust. It is better to change your approach than to give up altogether. This kind of mindset will help you overcome any obstacle. With every challenge, there comes an opportunity to grow. For instance, failing at something can teach you valuable lessons. In fact, most people learn more from failure than from success. That is why failure should never be feared. You should embrace it as part of the process. As long as you keep trying, you will always have a chance to succeed. The only true failure is giving up.

And yet, many people struggle with self-doubt. It is natural to question yourself sometimes. But remember, self-doubt is not a reason to stop. If anything, it is a sign that you are stepping out of your comfort zone. This is where growth happens. When you face your fears, you become stronger. They say courage is not the absence of fear, but the ability to act despite it. You do not need to be fearless; you just need to be brave enough to try. With every step forward, you build confidence. Your efforts, no matter how small, add up over time. And as you progress, you will see results. It may take longer than you expect, but that is okay. The important thing is to keep going.

In addition to resilience, gratitude is also important. When you appreciate what you have, you create space for more positivity in your life. This does not mean you should settle for less, but rather that you should recognize the good things already present. They can serve as a reminder of how far you have come. By focusing on gratitude, you shift your mindset from scarcity to abundance. That shift can make all the difference. For example, instead of dwelling on what you lack, think about what you have achieved so far. As you do this, you will feel more motivated to keep going. The path to success is not just about achieving goals; it is also about enjoying the journey. With the right mindset, every step becomes meaningful.

Of all the challenges you will face, fear of failure is perhaps the most common. But failure is not something to be afraid of. It is simply a part of life. You cannot succeed without taking risks, and risks often lead to failure. This is not a bad thing. When you fail, you learn. And when you learn, you grow. They say that every failure brings you one step closer to success. If you keep this in mind, you will see failure not as an end, but as a beginning. Your perspective matters more than anything else. With a positive outlook, even setbacks can become stepping stones. The key is to keep moving forward, no matter what happens.

And while persistence is important, so is balance. It is essential to take care of yourself along the way. When you are tired, rest. If you are stressed, take a break. This does not mean you are giving up; it means you are recharging. In fact, taking care of yourself is one of the most productive things you can do. By prioritizing your well-being, you ensure that you have the energy and focus to achieve your goals. They say you cannot pour from an empty cup, and this is true. Your health and happiness are just as important as your ambitions.

On the subject of happiness, it is worth noting that success is not the only source of joy. The little things in life matter just as much. As you work toward your goals, do not forget to enjoy the present moment. It is easy to get caught up in the future, but life is happening now. When you appreciate the present, you create memories that last a lifetime. And these memories are just as valuable as any achievement. There is beauty in the journey, not just the destination.
"""

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_word = set(stopwords.words('english'))
word_tokens = word_tokenize(text)

filter = [word for word in word_tokens if not word.lower() in stop_word]

filter_word = [w for w in filter if is_word(w)]
print(filter)
print(f"remove {len(text)-len(filter)} words")
print(filter_word[:100])

## POS TAGGING
from nltk import pos_tag
from nltk.tokenize import word_tokenize
from collections import Counter

word = word_tokenize(hamlet_text)
pos = pos_tag(word)
print(pos[:20])

select_tag = ['NN','VB','JJ']
count_pos_tag = Counter(tag for word, tag in pos if tag in select_tag)
print(count_pos_tag)

## NAME ENITITY RECOGNISATION
from nltk import ne_chunk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

sent = sentences[:10]
sent = " ".join(sent)
word = word_tokenize(sent)
pos = pos_tag(word)
ner = ne_chunk(pos)

def classify(text):
  label_list = {
      'ORGANIZATION': 'Organization',
      'PERSON': 'Person',
      'LOCATION': 'Location'
  }
  for subtree in text.subtrees():

      if subtree.label() in label_list:
          entity = ""
          for leaf in subtree.leaves():
              entity = entity + leaf[0] + " "
          print(subtree.label(), entity)

classify(ner)
