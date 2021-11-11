import yaml


class ReadYaml:

    @staticmethod
    def read_yaml():
        with open(r'F:\PycharmProjects\api_practice\config\data.yaml') as f:
            cfg = yaml.load(stream=f, Loader=yaml.FullLoader)
            print(f"读取到的url为：{cfg}")
        return cfg

    @staticmethod
    def swap_num(num1, num2):
        print('交换前两个数为: %d, %d' % (num1, num2))
        # 临时变量
        c = num1
        num1 = num2
        num2 = c
        print('交换前两个数为: %d, %d' % (num1, num2))


a = 5
b = 6
a, b = b, a
# ReadYaml().swap_num(a, b)
print(a, b)
ReadYaml().read_yaml()
