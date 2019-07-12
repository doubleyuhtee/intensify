import sys
from PIL import Image, ImageChops
import random
import argparse
import os


def get_time_per_frame(PIL_Image_object):
    """ Returns the average framerate of a PIL Image object """
    PIL_Image_object.seek(0)
    frames = duration = 0
    while True:
        try:
            frames += 1
            duration +=  PIL_Image_object.info['duration'] if 'duration' in PIL_Image_object.info else 1
            PIL_Image_object.seek(PIL_Image_object.tell() + 1)
        except EOFError:
            try:
                return duration / frames
            except:
                return 1
    return 1


argument_parser = argparse.ArgumentParser(description="Intensifies gifs poorly")
argument_parser.add_argument("--file", "-f", action='store',
                             help="file path", required=True)
argument_parser.add_argument("--scale", "-s", action='store',
                             help="factor to scale frame duration (default 1)", default=1, required=False)
argument_parser.add_argument("--loops", "-l", action='store',
                             help="Number of times to loop (default 1)", default=1, required=False)
argument_parser.add_argument("--duplicate", "-d", action='store',
                             help="Number of times to duplicate frames (default 1)", default=1, required=False)
argument_parser.add_argument("--shift", action='store',
                             help="Max distance to shift (default 5)", default=5, required=False)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        argument_parser.print_help()
        exit(0)

    parsed_args = argument_parser.parse_args(sys.argv[1:])

    im = Image.open(parsed_args.file)

    frames = 1
    if hasattr(im, 'is_animated'):
        print(im.is_animated)
        print(im.n_frames)
        frames = im.n_frames
    zoom = (im.height+10, im.width+10)
    print("dim " + str(zoom))
    out_frames = []
    shift_range = range(int(parsed_args.shift) * -1, int(parsed_args.shift))
    for loop in range(0, int(parsed_args.loops)):
        for frame in range(0, frames):
            im.seek(frame)
            for d in range(0, int(parsed_args.duplicate)):
                x = random.choice(shift_range)
                y = random.choice(shift_range)
                zoomed = ImageChops.offset(im, x, y)
                out_frames.append(zoomed)

    out = os.path.splitext(parsed_args.file)[0] + "-intensifies.gif"
    print(out)
    out_frames[-1].save(out, format='GIF', append_images=out_frames[0:-1], save_all=True,
                        duration=(get_time_per_frame(im) * float(parsed_args.scale)), transparency=1, loop=0)