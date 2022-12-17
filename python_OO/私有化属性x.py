'''
Author: chris-ui 15354987248@sina.cn
Date: 2022-12-15 23:37:16
LastEditors: chris-ui 15354987248@sina.cn
LastEditTime: 2022-12-16 14:59:05
FilePath: \python_OO\私有化属性.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# x

class Animal:
    # 类的内部

    x = 10

    def test(self):
        print(Animal.x)
        print(self.x)

    pass


class Dog(Animal):
    # 子类内部

    def test2(self):
        print(Dog.x)
        print(self.x)
    pass

# 模块内部的其他位置


# 测试代码
a = Animal()
a.test()   # 虽然是外界调用，但本质是内部访问

d = Dog()
d.test2()

print(Animal.x)
print(Dog.x)
print(a.x)
print(d.x)

a = 666


