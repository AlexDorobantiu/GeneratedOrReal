
import os

def get_image_paths():
    image_dir = os.path.join('app', 'static', 'images')
    image_paths = []
    for root, dirs, files in os.walk(image_dir):
        for file in files:
            if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):
                image_paths.append(os.path.relpath(os.path.join(root, file), image_dir))
    return image_paths