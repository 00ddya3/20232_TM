
from nurphy.word_embeddings.word_embeddings import Word2Vec

word2vec = Word2Vec()
binary=True
#model_file = 'D:\\python_workspace\\yonlu\\yonlu\\models\\word2vec\\korean_wiki_w2v.bin'
model_file = "../embeddings/word2vec/korean_wiki_w2v.bin"
word2vec.load_model(model_file, binary)

print(word2vec.most_similar(positives=['손흥민', '배구'], negatives=['축구'], topn=10))
print('-----------------------------------')

print(word2vec.similar_by_word('손흥민'))