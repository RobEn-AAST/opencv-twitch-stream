from twitchstream.outputvideo import TwitchBufferedOutputStream
import argparse
import numpy as np
import cv2
import time
from rovlib.cameras import RovCam


STREAM_FROM = 0


def convert_to_twitch_frame(recieved_frame, resize=True, bgr_to_rgb=True):
    if resize:
        width = int(640)
        height = int(480)
        dim = (width, height)
        recieved_frame = cv2.resize(recieved_frame, dim, interpolation = cv2.INTER_AREA)
    if bgr_to_rgb:
        recieved_frame = cv2.cvtColor(recieved_frame, cv2.COLOR_BGR2RGB)

    output_frame = np.zeros((480, 640, 3), dtype=np.float32)    
    output_frame = recieved_frame[:, :] / 255.0
    return output_frame


if __name__ == "__main__":
    cam = RovCam(RovCam.FRONT)
    parser = argparse.ArgumentParser(description=__doc__)
    required = parser.add_argument_group('required arguments')
    required.add_argument('-s', '--streamkey',
                          help='twitch streamkey',
                          required=True)
    args = parser.parse_args()

    with TwitchBufferedOutputStream(
            twitch_stream_key=args.streamkey,
            width=640,
            height=480,
            fps=30,
            verbose=True,
            enable_audio=False) as videostream:

        while True:
            if videostream.get_video_frame_buffer_state() < 30:
                frame = cam.read()
                videostream.send_video_frame(convert_to_twitch_frame(frame))