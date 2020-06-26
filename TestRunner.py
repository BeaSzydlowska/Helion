from unittest import TestLoader, TestSuite, TextTestRunner

from Tests.loginTest import LoginTest
from Tests.accountTest import AccountTest
from Tests.registerTest import RegisterTest
from Tests.searchTest import SearchTest
from Tests.basketTest import BasketTest
import testtools as testtools

if __name__ == '__main__':

    loader = TestLoader()
    suite = TestSuite((
        # loader.loadTestsFromTestCase(RegisterTest),
        # loader.loadTestsFromTestCase(LoginTest),
        # loader.loadTestsFromTestCase(AccountTest),
        # loader.loadTestsFromTestCase(SearchTest),
        loader.loadTestsFromTestCase(BasketTest)))

    runner = TextTestRunner()
    runner.run(suite)

concurrent_suite = testtools.ConcurrentStreamTestSuite(lambda: ((case, None) for case in suite))
concurrent_suite.run(testtools.StreamResult())