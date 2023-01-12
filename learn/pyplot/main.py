from matplotlib import pyplot as plt
import os

funcs = [i for i in dir(plt) if i[0] != '_']

for i,v in enumerate(funcs):
    print(i,v)
    # with open(f'pyplot.{v}.ipynb', 'w+') as f:
    #     f.close()
    # break
