from PIL import Image, ImageSequence
import numpy as np

def load_frames(image: Image, mode='RGBA'):
    return np.array([
        np.array(frame.convert(mode))
        for frame in ImageSequence.Iterator(image)
    ])





class GifReader():
    def __iter__(self, gif_path):
        self.gif_path = gif_path

        with Image.open(self.gif_path) as im:
            self.frames = load_frames(im)

    def __len__(self):
        return self.frames.shape[0]

    def get_batch(self, indices):
        return self.frames.shape[indices, :, :, :]