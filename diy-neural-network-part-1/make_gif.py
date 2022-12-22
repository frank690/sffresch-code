from pathlib import Path
import imageio.v3 as iio
import numpy as np


folder = Path("./plots")
files = [f.absolute() for f in folder.glob("*.png")]

gif_path = "decision_boundaries.gif"

frames = np.stack([iio.imread(file) for file in files], axis=0)

iio.imwrite(gif_path, frames)
