# Input: Long text
text = """
Artificial Intelligence is the ability of a computer or a robot controlled by a computer to do tasks that are usually done by humans.
AI has become an essential part of the technology industry. It helps in problem-solving, learning, and reasoning.
AI is used in many fields such as healthcare, finance, education, and more. With rapid advancements, AI is changing our world.
"""

# Step 1: Split text into sentences
sentences = text.split('.')

# Step 2: Count word frequency
word_freq = {}
for sentence in sentences:
    for word in sentence.strip().lower().split():
        word = word.strip('.,!?')
        if word:
            word_freq[word] = word_freq.get(word, 0) + 1

# Step 3: Score each sentence
sentence_scores = {}
for sentence in sentences:
    score = 0
    for word in sentence.lower().split():
        word = word.strip('.,!?')
        score += word_freq.get(word, 0)
    sentence_scores[sentence] = score

# Step 4: Pick top 2 sentences
top_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:2]

# Step 5: Join and print summary
summary = '. '.join(top_sentences).strip()
print("🔹 Summary:\n", summary + ".")