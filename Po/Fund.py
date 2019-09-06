from Libs.Common import LoginClass


class FundClass(LoginClass):

    def createBankCard(self):
        bank_card_path = '/member.php?ctl=uc_money&act=savebank'
        bank_card_data = {
            'real_name': 'liudehua',
            'bank_id': '1',
            'otherbank': '',
            'region_lv1': '1',
            'region_lv2': '3',
            'region_lv3': '38',
            'region_lv4': '417',
            'bankzone': 'gongshang',
            'bankcard': '1234 5678 94',
            'reBankcard': '1234 5678 94',
        }
        self.loginApi()
        result = self.sendHttp(path=bank_card_path, data=bank_card_data, cookies=self.phpid)
        return result


if __name__ == '__main__':
    ...
