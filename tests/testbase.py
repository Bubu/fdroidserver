import inspect
import unittest
import os
import sys
import logging
import optparse

from fdroidserver import common

localmodule = os.path.realpath(
    os.path.join(os.path.dirname(inspect.getfile(inspect.currentframe())), '..'))
print('localmodule: ' + localmodule)
if localmodule not in sys.path:
    sys.path.insert(0, localmodule)


class TestBase(unittest.TestCase):
    def setUp(self):
        logging.basicConfig(level=logging.INFO)
        self.localmodule = localmodule
        self.basedir = os.path.join(self.localmodule, 'tests')
        self.tmpdir = os.path.abspath(os.path.join(self.basedir, '..', '.testfiles'))
        if not os.path.exists(self.tmpdir):
            os.makedirs(self.tmpdir)
        os.chdir(self.basedir)

    @classmethod
    def main(cls):
        parser = optparse.OptionParser()
        parser.add_option("-v", "--verbose", action="store_true", default=False,
                          help="Spew out even more information than normal")
        (common.options, args) = parser.parse_args(['--verbose'])

        newSuite = unittest.TestSuite()
        newSuite.addTest(unittest.makeSuite(cls))
        unittest.main(failfast=False)
