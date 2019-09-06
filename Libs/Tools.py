import requests
import unittest

# 爷爷类
class HttpClass(object):
    # 把Host抽取出来
    host = 'http://localhost'

    # 统一调用Http请求方法
    def sendHttp(self, path,method='post', **kwargs):
        url = '{}{}'.format(self.host, path)
        result = requests.request(method, url=url, **kwargs)
        return result


class VerifyClass(unittest.TestCase):

    # 校验Text值
    def checkTextData(self,result,expectValue,expectCode):
        # 校验状态码
        self.assertEqual(result.status_code, expectCode)
        # 校验是否包含特殊文本值
        self.assertIn(expectValue,result.text)


    # 校验Json值
    def checkJsonData(self,result,expectKey,expectValue,expectCode):
        # 校验状态码
        self.assertEqual(result.status_code, expectCode)
        # 校验是否包含特殊字段
        self.assertIn(result.json().get(expectKey),expectValue)
