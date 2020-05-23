from lab5.search_2dim import search_2dim
import numpy as np
import imageio


def read_as_gray(path):
    img = imageio.imread(path)
    return np.dot(img[..., :3], [0.2989, 0.5870, 0.1140])


def zad5(image_path, pattern_path):
    print("Task 5")
    img = read_as_gray(image_path)
    print("Image:", image_path)
    pattern = read_as_gray(pattern_path)
    print("Pattern:", pattern_path)
    print("Found:", search_2dim(img, pattern))


def zad4(image_path, letter_paths):
    print("Task 4")
    img = read_as_gray(image_path)
    print("Image: ", image_path)
    for letter_path in letter_paths:
        print("Search for letter:", letter_path)
        letter = read_as_gray(letter_path)
        print("Found:", search_2dim(img, letter))


def zad3(lines):
    print("Task 3")
    print("Search for: th\nFound:", search_2dim(lines, ['th', 'th']))
    print("Search for: t h\nFound:", search_2dim(lines, ['t h', 't h']))


def zad2(lines):
    print("Task 2")
    for char in [chr(i) for i in range(ord('A'), ord('Z'))] + [chr(i) for i in range(ord('A'), ord('Z'))]:
        print("Search for: ", char, "Found:", search_2dim(lines, [char, char]))


def main():
    file_path = 'haystack.txt'
    image_path = 'haystack.png'
    letter_paths = ['letters/a.png', 'letters/l.png', 'letters/g.png', 'letters/o.png']
    pattern_path = 'pattern.png'

    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Task 2
    zad2(lines)

    # Task 3
    zad3(lines)

    # Task 4
    zad4(image_path, letter_paths)

    # Task 5
    zad5(image_path, pattern_path)


if __name__ == '__main__':
    main()
