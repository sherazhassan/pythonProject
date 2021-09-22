import unittest


class Apptesting(unittest.TestCase):
    @unittest.SkipTest
    def test_search(self):
        print("This is search test")
    @unittest.skip("I'm skipping this test because it is incomplete")
    def test_advancesearch(self):
        print("This is advance search method")
    @unittest.skipIf(1==1, "Numbers are equal")
    def test_prepaidrecharge(self):
        print("This is prepaid testing method")

    def test_postpaidrecharge(self):
        print("This is postpaid testing method")

    def test_loginbygmail(self):
        print("This is login by email")

    def test_loginbytwitter(self):
        print("This is login by twitter")


if __name__ == "__main__":
    unittest.main
