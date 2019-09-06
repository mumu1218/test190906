from Po.MyP2P.MyAccount import MyAccountClass
from Libs.Tools import VerifyClass

class TestClass(VerifyClass):

    def setUp(self):
        self.mc = MyAccountClass()

    def test_success001(self):
        result = self.mc.creditApi()
        # 校验值
        self.checkTextData(result,'操作成功',200)



if __name__ == '__main__':
    ...
