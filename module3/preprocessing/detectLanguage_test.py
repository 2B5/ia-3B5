import unittest
import detectLanguage

from sys import argv
from sys import flags

if len(argv) > 1 and argv[1] == '-v':
	verbose = True
else:
	verbose = flags.verbose

class MyTest(unittest.TestCase):
	def test_detectLang_en(self):
		if not verbose:
			print('\n --- Testing function detectLang("Is just a text to test a request what is wrong with you?"). Should return "en"... ----')
		self.assertEqual(detectLanguage.detectLang('Is just a text to test a request what is wrong with you?'), 'en')

	def test_detectLang_other(self):
		if not verbose:
			print('\n --- Testing function detectLang("Afara ninge linistit."). Should return "other" ----')
		self.assertEqual(detectLanguage.detectLang('Afara ninge linistit.'), 'other')

if __name__ == '__main__':
    unittest.main()