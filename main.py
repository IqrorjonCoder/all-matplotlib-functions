import matplotlib as mt
import os

# functions = [i for i in os.listdir('/home/iqrorjoon/PycharmProjects/all matplotlib functions/venv/lib/python3.8/site-packages/matplotlib/')
#              if i[0] != '_' and i[-3:] != '.so']
#
# for i, v in enumerate(functions):
#     print(i, v)
#     if v[-3:] == '.py':
#         os.makedirs(f"/home/iqrorjoon/PycharmProjects/all matplotlib functions/learn/{v[:-3]}")
#         # break
#     else:
#         os.makedirs(f"/home/iqrorjoon/PycharmProjects/all matplotlib functions/learn/{v}")
#         # break


from matplotlib import pyplot as plt

funcs = [i for i in dir(plt) if i[0] != '_']

for i,v in enumerate(funcs):
    print(i,v)
