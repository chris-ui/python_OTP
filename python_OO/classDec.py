'''
Author: chris-ui 15354987248@sina.cn
Date: 2022-12-14 15:53:36
LastEditors: chris-ui 15354987248@sina.cn
LastEditTime: 2022-12-14 17:21:26
FilePath: \python_OO\类的描述.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
"""
Author: chris-ui 15354987248@sina.cn
Date: 2022-12-14 15:53:36
LastEditors: chris-ui 15354987248@sina.cn
LastEditTime: 2022-12-14 17:01:43
FilePath: \python_OO\类的描述.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
"""


class Person:
    """
    关于这个类的描述，类的作用，类的构造函数等等：类属性的描述
    Attributes:
        count: int 代表是人的个数
    """
    # 这个表示，是人的个数
    count = 0

    def run(self, distance, step):
        """
        这个方法的作用效果
        :param distance:参数的含义，参数的类型，是否有默认值
        :param step:
        :return:返回的结果的含义（时间），返回数据的类型int
        """

        print('人在跑')
        return distance / step


# int  ctrl 可以看文档注释

help(Person)  # 生成文档


def xxx():
    """
    这是一个xxx函数，有xxx作用
    :return:
    """
    print("xxx")

property










