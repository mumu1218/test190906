import unittest
from Libs.Tools import VerifyClass
from Po.Fund import FundClass


class TestClass(VerifyClass):

    def setUp(self):
        self.fc = FundClass()

    def test_success001(self):
        result = self.fc.createBankCard()
        self.checkJsonData(result, 'info', '保存成功', 200)


if __name__ == '__main__':
    unittest.main()
