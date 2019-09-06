from Libs.Tools import HttpClass

# 爸爸类
class LoginClass(HttpClass):
    phpid = {
            'PHPSESSID': ''
        }
    
    def loginApi(self):
        # 登录接口
        lgn_path = '/index.php?ctl=user&act=dologin'
        # 登录数据
        lgn_data = {
            'email': 'woshinin002',
            'user_pwd': 'Z0x0Z3hsalVDd0tjcHlBWEdDZE1ua0JQVGhpQ1JpbHl3UnV1UFlKUXpmc2lyelJyWkQlMjV1NjVCOSUyNXU3RUY0c2YxMjM0NTYlMjV1OEY2RiUyNXU0RUY2',
            'ajax': '1',
        }

        # 登录
        lgn_result = self.sendHttp(path=lgn_path, data=lgn_data)
        cookies = lgn_result.cookies['PHPSESSID']
        self.phpid['PHPSESSID'] = cookies
    