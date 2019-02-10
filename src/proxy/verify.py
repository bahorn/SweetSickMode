import ihash
import sys
import io
import PIL

class CheckImage:
    def __init__(self, hashes_file):
        self.known = []
        self._load_hashes(hashes_file)

    def _load_hashes(self, filename):
        with open(filename) as hashes_file:
            hashes = hashes_file.read().split('\n')
            for h in hashes:
                try:
                    self.known.append(ihash.load_hash(h))
                except:
                    continue

    def _compare_hash(self, inp):
        for i in self.known:
            if ihash.compare_hash(inp, i):
                return True
        return False

    def check_file(self, filename):
        # get the hash for the data
        inp = ihash.generate_hash(filename)
        return self._compare_hash(inp)

    def check_stream(self, stream):
        mem_stream = io.BytesIO(stream)
        inp = ihash.generate_hash_stream(mem_stream)
        print(inp)
        return self._compare_hash(inp)

if __name__ == "__main__":
    d = CheckImage('./hashes.txt')
    print(d.check_file('../cat.jpg'))
