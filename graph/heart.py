import matplotlib.pyplot as plt
import numpy as np

# # 定义心形函数
# def heart_shape(x, y):
#     return (np.sqrt(abs(x)**2 + abs(y)**2 - 1)**3 - x**2 * y**3) <= 0

# # 创建网格
# x = np.linspace(-2, 2, 400)
# y = np.linspace(-2, 2, 400)

# X, Y = np.meshgrid(x, y)
# Z = heart_shape(X, Y)

# # 绘制图形
# plt.contourf(X, Y, Z, cmap=plt.cm.Reds_r)
# plt.axis('equal')
# plt.show()


def print_heart():
    # 定义心形使用的字符串
    love_string = "love"

    # 循环遍历行数
    for y in range(30, -30, -1):
        # 初始化每行的字符串
        line = ''

        # 遍历每行的列数
        for x in range(-30, 30):
            # 计算当前位置的字符，基于一个心形函数的逻辑
            char_index = (x - y) % len(love_string)
            condition = ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (x * 0.05) ** 2 * (y * 0.1) ** 3 <= 0
            char = love_string[char_index] if condition else ' '

            # 将字符添加到当前行
            line += char

        # 打印换行后的完整行
        print(line)

# 调用函数打印心形
print_heart()
