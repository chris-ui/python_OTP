'''
Author: chris-ui 15354987248@sina.cn
Date: 2022-12-16 15:08:30
LastEditors: chris-ui 15354987248@sina.cn
LastEditTime: 2022-12-16 15:21:34
FilePath: \python_OO\私有化属性_y.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
class Animal:
    # 类的内部

    __x = 10

    def test(self):
        print(Animal.__x)
        print(self.__x)

    pass


# class Dog(Animal):
#     # 子类内部

#     def test2(self):
#         print(Dog.__x)
#         print(self.__x)
#     pass


# # 测试代码
# a = Animal()
# a.test()   # 虽然是外界调用，但本质是内部访问

# d = Dog()
# d.test2()

# print(Animal.__x)  # 会有警告
# print(Dog.__x)
# print(a.__x)
# print(d.__x)

__all__ = ['__a']
__a = 666

