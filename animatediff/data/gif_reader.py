from PIL import Image, ImageSequence
import numpy as np

def load_frames(image: Image, mode='RGBA'):
    return np.array([
        np.array(frame.convert(mode))
        for frame in ImageSequence.Iterator(image)
    ])





<<<<<<< HEAD
class GifReader:
=======
class GifReader():
>>>>>>> 76d7fd6c2f9fc95978d0c06e344db5211b5e87a7
    def __iter__(self, gif_path):
        self.gif_path = gif_path

        with Image.open(self.gif_path) as im:
            self.frames = load_frames(im)
<<<<<<< HEAD
            print(f"loaded {self.gif_path} to frames: {self.frames.shape}")
=======
>>>>>>> 76d7fd6c2f9fc95978d0c06e344db5211b5e87a7

    def __len__(self):
        return self.frames.shape[0]

    def get_batch(self, indices):
<<<<<<< HEAD
        print(f"get_batch: {indices}")
=======
>>>>>>> 76d7fd6c2f9fc95978d0c06e344db5211b5e87a7
        return self.frames.shape[indices, :, :, :]