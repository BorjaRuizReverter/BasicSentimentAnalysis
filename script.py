'''
Firt, let's import the required packages
'''
import os
import emoji
import keras_nlp

os.environ["KERAS_BACKEND"] = "tensorflow"  # or "tensorflow" or "torch"

'''
This Basic Sentiment Analysis is based on a pretrained backbone taken from keras_npl models
'''
classifier = keras_nlp.models.BertClassifier.from_preset("bert_tiny_en_uncased_sst2")

'''
Now type in the sentence that it is going to be analysed
'''
sentence = input("Type a sentence: ")
sentiment_matrix = classifier.predict([sentence])

'''
This is to print the result in terms of a 1x2 matrix
'''
print("The result of this binary classification is {} negative and {} positive".format(sentiment_matrix[0,0], sentiment_matrix[0,1]))

if (sentiment_matrix[0,0] >= 1.5):
    print(emoji.emojize('Therefore, this sentence is classified as very negative :thumbs_down: :thumbs_down:'))
elif (sentiment_matrix[0,0] >= 0.5):
    print(emoji.emojize('Therefore, this sentence is classified as negative :thumbs_down:'))
elif (sentiment_matrix[0,0] >= -0.5):
    print(emoji.emojize('Therefore, this sentence is classified as neutral :man_shrugging:'))
elif (sentiment_matrix[0,0] >= -1.5):
    print(emoji.emojize('Therefore, this sentence is classified as positive :thumbs_up:'))
else: #sentiment_matrix[0,0] < -1.5
    print(emoji.emojize('Therefore, this sentence is classified as very positive :thumbs_up: :thumbs_up:'))
