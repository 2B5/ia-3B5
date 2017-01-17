import unittest
import errorCorrect

from sys import argv
from sys import flags

if len(argv) > 1 and argv[1] == '-v':
	verbose = True
else:
	verbose = flags.verbose

class MyTest(unittest.TestCase):
	def test_correct(self):
		if not verbose:
			print('\n --- Testing function correct("She is mw moom"). Should return "The is my room" ----')
		self.assertEqual(errorCorrect.correct('She is mw moom.'), 'The is my room')

if __name__ == '__main__':
    unittest.main()