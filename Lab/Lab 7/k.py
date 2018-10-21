import os
print(os.path.basename('/Users/liumeiling/PycharmProjects/Lab/Lab7/k.py'))
# >>> k.py
print(os.path.commonprefix(['/usr/lib', '/usr/local/lib']))
# >>> /usr/l
print(os.path.commonpath(['/Users/liumeiling/PycharmProjects/Lab/Lab7/k.py', '/Users/local/lib']))
# >>> /Users (two /Users need to the same)
print(os.path.dirname('/Users/liumeiling/PycharmProjects/Lab/Lab7/k.py'))
# >>> /Users/liumeiling/PycharmProjects/Lab/Lab7
print(os.path.join(os.path.dirname('/Users/liumeiling/PycharmProjects/Lab/Lab7/k.py'), "k.py"))
# >>> /Users/liumeiling/PycharmProjects/Lab/Lab7/k.py
print(os.listdir('/Users/liumeiling/PycharmProjects/Lab/Lab7'))
# >>> ['.DS_Store', 'aaa', 'k.py', 'README file.txt', 'recursive.py', 'recursive_dir_traversal.py']
print(os.path.isfile('aa.py'))