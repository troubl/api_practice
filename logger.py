import logging

# 实例化对象
logger = logging.getLogger('test')

# 输出所有大于DEBUG级别的log
logger.setLevel(logging.DEBUG)

# 设置日志输出格式
fmt = logging.Formatter('[%(filename)-6s]: [%(levelname)-6s]: [%(asctime)s]: %(message)s')
stream_hd1 = logging.StreamHandler()
stream_hd1.setFormatter(fmt)
stream_hd1.setLevel(logging.DEBUG)
logger.addHandler(stream_hd1)

# if __name__ == '__main__':
#     logger.info('this is info')
