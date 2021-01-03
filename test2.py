import argparse

# print('YEE')
parser = argparse.ArgumentParser()
parser.add_argument('--mode', help='task to be done', default='train')
opt = parser.parse_args()
print(vars(opt)['mode'])
i = input('Type in...')
print(i)