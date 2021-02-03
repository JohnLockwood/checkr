import unittest as t
from lev import *


class Suite(t.TestCase):
    def test_known_score(self):
        self.assertEqual(lev('foot', 'fool'), 1)

    # Etc.

