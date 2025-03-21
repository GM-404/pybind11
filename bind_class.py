# # 定义一个模拟的 ttdv 模块
# class TTDV:
#     def add(self, x, y):
#         return x + y

# # 创建 ttdv 对象
# ttdv = TTDV()

# # 初始化变量
# a = 0
# # 调用 add 方法
# a = ttdv.add(1, 2)
# # 打印结果
# print(a)

#调用类的方法
import bind_class as bc

# 创建 ExampleClass 的实例
obj = bc.ExampleClass(42)

# 调用 getData 方法
print(obj.getData())

# 调用 setData 方法
obj.setData(100)

# 再次调用 getData 方法
print(obj.getData())

    
