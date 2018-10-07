import unittest
from app.models import Articles


class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Articles(
            'abc-news', 'ABC News', 'ABC News', 'WATCH: Arrest warrant issued for man in murder of wife, Amber Alert for 2 missing sons', 'An Amber Alert was issued for Jonathan and Victor Coronado Nunez, ages 5 and 8, on Saturday.', 'https://abcnews.go.com/US/video/arrest-warrant-issued-man-murder-wife-amber-alert-57572297', 'https://s.abcnews.com/images/US/180903_vod_orig_amber_alert_hpMain_16x9_992.jpg', '2018-09-03T11:47:56Z')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Articles))


if __name__ == '__main__':
    unittest.main()
