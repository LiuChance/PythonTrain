import imageio
import os

path = 'F:/11111'
filenames = []
for files in os.listdir(path):
    if files.endswith('jpg') or files.endswith('jpeg') or files.endswith('png'):
        file = os.path.join(path, files)
        filenames.append(file)

images = []
for filename in filenames:
    images.append(imageio.imread(filename))
imageio.mimsave('F:/my.gif', images, duration=0.5)
