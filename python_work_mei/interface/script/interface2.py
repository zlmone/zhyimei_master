# coding:utf-8
import requests
import unittest
import json
class test_wuye2(unittest.TestCase):
    def setUp(self):
        print(u"开始")
    def test_interface2(self):
        lp2={"token":"e10adc3949ba59abbe56e057f20f8824","username":"13000000000"}
        rd2=requests.get("http://172.16.4.120/wuye/public/index.php/index/index//allCommunityId?",params=lp2)
        print(rd2.status_code)
        print(rd2.text)
        data=json.loads(rd2.text)
        self.assertEqual("success",data["message"])
    def tearDown(self):
        print(u"结束")
if __name__ == '__main__':
    unittest.main
