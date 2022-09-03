# 在双引号的中间粘贴上executable code, 点击运行即可

from main_by_file import tranlate
text = """
    0:        00200093        addi x1 x0 2
    4:        00600113        addi x2 x0 6
    8:        00000193        addi x3 x0 0
    c:        00100213        addi x4 x0 1
    10:        004181b3        add x3 x3 x4
    14:        fe315ee3        bge x2 x3 -4
"""


mem = tranlate(text)
print(mem)


# 运行之后结果如下
"""
00 60 04 13
00 90 04 93
00 94 05 33
00 60 04 13
00 90 04 93
00 94 05 33
"""
