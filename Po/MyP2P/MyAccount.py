from Libs.Common import LoginClass


class MyAccountClass(LoginClass):

    # 申请信用额度Api
    def creditApi(self):
        # 申请信用额度
        credit_path = '/member.php?ctl=uc_quota&act=do_add_quota'
        credit_data = {
            'money': '1002',
            'referraler': 'haha',
            'memo': 'testting1',
            'other_memo': 'testting2',
        }
        self.loginApi()    
        credit_result = self.sendHttp(path=credit_path, data=credit_data, cookies=self.phpid)
        return credit_result
