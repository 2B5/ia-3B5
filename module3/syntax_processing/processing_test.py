import unittest
import processing
import nltk

from sys import argv
from sys import flags

_wordnet = nltk.corpus.wordnet

if len(argv) > 1 and argv[1] == '-v':
	verbose = True
else:
	verbose = flags.verbose

class MyTest(unittest.TestCase):
	def test_word_tag_noun(self):
		if not verbose:
			print('\n --- Testing function word_tag() ----')
		self.assertEqual(processing.TextProcessor('Initial text').word_tag(['Hello', 'NN']), _wordnet.NOUN)

	def test_word_tag_adj(self):
		if not verbose:
			print('\n --- Testing function word_tag() ----')
		self.assertEqual(processing.TextProcessor('Initial text').word_tag(['Hello', 'JJ']), _wordnet.ADJ)

	def test_word_tag_verb(self):
		if not verbose:
			print('\n --- Testing function word_tag() ----')
		self.assertEqual(processing.TextProcessor('Initial text').word_tag(['Hello', 'VB']), _wordnet.VERB)

	def test_word_tag_adv(self):
		if not verbose:
			print('\n --- Testing function word_tag() ----')
		self.assertEqual(processing.TextProcessor('Initial text').word_tag(['Hello', 'RB']), _wordnet.ADV)

	def test_get_sentiment_neutral(self):
		if not verbose:
			print('\n --- Testing function get_sentiment_neutral() ----')
		self.assertEqual(processing.TextProcessor('Initial text').get_sentiment(0.1), 'neutral')

	def test_get_sentiment_happy(self):
		if not verbose:
			print('\n --- Testing function get_sentiment_happy() ----')
		self.assertEqual(processing.TextProcessor('Initial text').get_sentiment(0.75), 'happy')

	def test_get_sentiment_sad(self):
		if not verbose:
			print('\n --- Testing function get_sentiment_sad() ----')
		self.assertEqual(processing.TextProcessor('Initial text').get_sentiment(-0.1), 'sad')

	def test_processing(self):
		if not verbose:
			print('\n --- Testing function get_sentiment_sad() ----')

		result = processing.TextProcessor('Initial text').processing()
		expected = {'Subject': 'john', 'Predicate': 'live', 'Verbs': ['live', 'bear'], 'Sentance': ['john', 'have', 'be', 'live', 'in', 'this', 'city', 'since', 'he', 'be', 'bear'], 'Sentiment': 'neutral', 'Proper Nouns': ['john'], 'Noun Phrase': ['john'], 'Pronouns': ['he']}

		self.assertEqual(result, expected)
		

if __name__ == '__main__':
    unittest.main()