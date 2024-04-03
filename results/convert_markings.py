import os
import json
from PIL import Image
import numpy as np

def convert_rle_to_png(rle_data, width: int, height: int, filename):
    # based on the code from: https://stackoverflow.com/questions/74339154/how-to-convert-rle-format-of-label-studio-to-black-and-white-image-masks
    class InputStream:
        def __init__(self, data):
            self.data = data
            self.i = 0

        def read(self, size):
            out = self.data[self.i:self.i + size]
            self.i += size
            return int(out, 2)

    def convert_to_numpy_array(rle_data, width, height):
        def access_bit(data, num):
            """ from bytes array to bits by num position"""
            base = int(num // 8)
            shift = 7 - int(num % 8)
            return (data[base] & (1 << shift)) >> shift
        def bytes2bit(data):
            """ get bit string from bytes data"""
            return ''.join([str(access_bit(data, i)) for i in range(len(data) * 8)])
        rle_input = InputStream(bytes2bit(rle_data))

        num = rle_input.read(32)
        word_size = rle_input.read(5) + 1
        rle_sizes = [rle_input.read(4) + 1 for _ in range(4)]
        # print('RLE params:', num, 'values,', word_size, 'word_size,', rle_sizes, 'rle_sizes')

        i = 0
        out = np.zeros(num, dtype=np.uint8)
        while i < num:
            x = rle_input.read(1)
            j = i + 1 + rle_input.read(rle_sizes[rle_input.read(2)])
            if x:
                val = rle_input.read(word_size)
                out[i:j] = val
                i = j
            else:
                while i < j:
                    val = rle_input.read(word_size)
                    out[i] = val
                    i += 1

        image = np.reshape(out, [height, width, 4])[:, :, 3]
        return image

    image = convert_to_numpy_array(rle_data, width, height)
    Image.fromarray(image).save(filename)


def main():
    # Get current directory
    current_dir = os.getcwd()
    
    # Get all JSON files in current directory
    json_files = [file for file in os.listdir(current_dir) if file.endswith(".json")]
    
    # Deserialize JSON files to dictionaries
    for json_file in json_files:
        with open(json_file, "r") as file:
            if not json_file.endswith("_brush.json"):
                continue
            data = json.load(file)
            png_filename = json_file.removesuffix(".json") + ".png"
            rle_data = data["value"]["rle"]
            width = data['original_width']
            height = data['original_height']
            convert_rle_to_png(rle_data, width, height, png_filename)

if __name__ == "__main__":
    main()