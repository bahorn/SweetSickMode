import os
import PIL
import cv2
import imagehash

# We're using a Perceptual hash. Had to increase the size
# as we're otherwise 
def generate_hash(filename):
    return _generate_hash(PIL.Image.fromarray(cv2.imread(filename)))

def generate_hash_stream(stream):
    return _generate_hash(PIL.Image.open(stream))

def _generate_hash(stream):
    return imagehash.phash(
        stream,
        hash_size=32
    )


def load_hash(h):
    return imagehash.hex_to_hash(h)


# Uses the hamming distance between the two hashes to confirm if we've got
# a hit.
def compare_files(file1, file2, distance=430):
    h1 = generate_hash(file1)
    h2 = generate_hash(file2)
    return compare_hash(h1, h2, distance=distance)

def compare_hash(h1, h2, distance=440):
    return (h1 - h2) < distance

if __name__ == "__main__":
    # Test used to make sure we've got a good distance.
    print(compare_files('../hashthing/tests/aim2.jpg', '../hashthing/tests/seen.jpg'))
