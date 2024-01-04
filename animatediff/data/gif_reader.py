from PIL import Image, ImageSequence
import numpy as np

def load_frames(image: Image, mode='RGB'):
    return np.array([
        np.array(frame.convert(mode))
        for frame in ImageSequence.Iterator(image)
    ])





class GifReader:

    def __init__(self, gif_path):
        self.gif_path = gif_path

        with Image.open(self.gif_path) as im:
            self.frames = load_frames(im)
            #print(f"loaded {self.gif_path} to frames: {self.frames.shape}")


    def __len__(self):
        return self.frames.shape[0]

    def get_batch(self, indices):
        #print(f"get_batch: {indices}")

        to_return  = self.frames[indices, :, :, :]

        #print(f"returning: {to_return.shape}")
        return to_return