import unittest
import tweeter.reader as reader
import tweeter.config


class ReaderTest(unittest.TestCase):

    def setUp(self):
        config = tweeter.config.get()
        self.r = reader.Reader(config['app_name'], config['consumer_key'],
                               config['consumer_secret'])

    def test_tweets(self):
        a = self.r.tweets('twitter', 2)
        self.assertIsInstance(a, list)
        [self.assertIsInstance(t, unicode) for t in a]

    def test_tokenize(self):
        word = '#tweeter'
        a = self.r.tokenize(word)
        self.assertEquals(a, ['#', 8, 11, 5, 5, 8, 5, 6])

    def test_all_words(self):
        a = self.r.all_words('twitter', 1)
        self.assertIsInstance(a, list)
        [self.assertIsInstance(s, unicode) for s in a]

    def test_all_tokens(self):
        a = self.r.all_tokens('twitter', 1)
        self.assertIsInstance(a, list)
        self.assertIsInstance(a[0], list)
        [self.assertTrue(is_int_or_unicode(e)) for e in a[0]]
    

def is_int_or_unicode(var):
    return (var.__class__ == int or var.__class__ == unicode)

if __name__ == "__main__":
    unittest.main()
