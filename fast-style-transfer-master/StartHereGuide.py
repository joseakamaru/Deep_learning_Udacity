#How to run the file:

#Copy and past the followin lines in order to create the enviroment
#     conda create -n style-transfer python=2.7.9

#Copy and past the follwoing line in ordre to initiate enviroment
#source activate style-transfer

#proceed with the follwoing lines to finish setting up the enviroment
#pip install tensorflow
#conda install scipy pillow
#pip install moviepy

# Run this file

import imageio
imageio.plugins.ffmpeg.download()

#Then Copy and past the following text into the terminal.

#python evaluate.py --checkpoint ./rain-princess.ckpt --in-path <path_to_input_file> --out-path ./output_image.jpg
