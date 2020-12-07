import PIL.Image


class Image:
    characters = r'B8&WM#YXQO{}[]()I1i!pao;:,.    '
    n = len(characters)

    def __init__(self, path):
        self.__file = PIL.Image.open(path).convert('L')
        self.__ascii = self.__to_ascii(self.__resize())

    def __str__(self):
        return self.__to_ascii(self.__resize())

    def save(self, path='ascii_image.txt'):
        with open(path, 'w') as f:
            f.write(self.__ascii)

    def __resize(self, new_width=120):
        width, height = self.__file.size
        new_height = int(new_width * (height / width))
        return self.__file.resize((new_width, new_height))

    def __to_ascii(self, image):
        width, height = image.size
        ascii_image = ''
        for h in range(0, height):
            for w in range(0, width):
                pixel = image.getpixel((w,h))
                ascii_image += self.characters[int(((self.n - 1) * pixel) / 256)]
            ascii_image += '\n'
        return ascii_image
