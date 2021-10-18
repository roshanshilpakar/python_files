import os
import shutil

current_dir = os.path.dirname(os.path.realpath(__file__))

for filename in os.listdir(current_dir):

    if filename.endswith(('.jpg', '.png', '.gif')):
        if not os.path.exists("Images"):
            os.makedirs('Images')
        shutil.copy(filename, 'Images')
        os.remove(filename)
        print('Images folder done')

    if filename.endswith(('.pdf', '.docx')):
        if not os.path.exists("Documents"):
            os.makedirs('Documents')
        shutil.copy(filename, 'Documents')
        os.remove(filename)
        print('Documents folder done')

    if filename.endswith(('.apk', '.exe')):
        if not os.path.exists("Apps"):
            os.makedirs('Apps')
        shutil.copy(filename, 'Apps')
        os.remove(filename)
        print('Apps folder done')

    if filename.endswith(('.mp4', '.wmv')):
        if not os.path.exists("Videos"):
            os.makedirs('Videos')
        shutil.copy(filename, 'Videos')
        os.remove(filename)
        print('Videos folder done')

print('all done')
