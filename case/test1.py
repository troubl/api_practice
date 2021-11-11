''' 实力一  get:'''

import os
import sys
curpath = os.path.abspath(os.path.dirname(__file__))
sys.path.append(curpath)

from read_yaml import ReadYaml
import requests
import json
import unittest
from ..logger import logger

'''封装'''


class TestCase(unittest.TestCase):
    '''仅仅写测试用例的请求'''

    def test_demo(self):
        data = ReadYaml().read_yaml()
        url = data['api_url']
        data = {"shop_id": "122212111111"}  # 字典类型
        data = json.dumps(data)  # 讲字典转行为json字符串
        res = requests.get(url=url, params=data)  # 发送请求，返回接口消息体

        logger.info(res.json())


if __name__ == '__main__':
    unittest.main()
    # import pytest
    #
    # pytest.main(['-s', 'test1.py', '--html=test1.html'])
