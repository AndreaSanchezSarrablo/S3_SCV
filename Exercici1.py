#EXERCICI1

import os

def ex_1(input_video):

    # First of all, we will cut the input video to 5 seconds in order to be able to
    # have quick conversions with all the extensions
    os.system("ffmpeg -i " + str(input_video) + " -ss 0 -t 5 -c:v copy -c:a copy 5secVideo.mp4")

    # Convert the video into 720p, 480p, 360x240, 160x120 but we will only use the 480p to do the other extensions
    # Resize the 5 seconds video to 720p
    # os.system("ffmpeg -i 5secVideo.mp4 -vf scale=-1:720 bbbVideo_720p.mp4")

    # Resize the 5 seconds video to 480p
    os.system("ffmpeg -i 5secVideo.mp4 -vf scale=-1:480 bbbVideo_480.mp4")

    # Resize the 5 seconds video to 360x240
    # os.system("ffmpeg -i 5secVideo.mp4 -vf scale=360:240 bbbVideo_260x240.mp4")

    # Resize the 5 seconds video to 160x120
    # os.system("ffmpeg -i 5secVideo.mp4 -vf scale=160:120 bbbVideo_160x120.mp4")

    # We are only going to convert the input video (480p) into the 4 extensions
    # Convert the video bbbVideo_480.mp4 into VP8 extension
    os.system("ffmpeg -i bbbVideo_480.mp4 -c:v libvpx -crf 30 -b:v 1M -c:a libopus output_vp8.webm")

    # Convert the video bbbVideo_480.mp4 into VP9 extension
    os.system("ffmpeg -i bbbVideo_480.mp4 -c:v libvpx-vp9 -crf 30 -b:v 1M -c:a libopus output_vp9.webm")

    # Convert the video bbbVideo_480.mp4 into h265 extension
    os.system("ffmpeg -i bbbVideo_480.mp4 -c:v libx265 -b:v 1M output_h265.mp4")

    # Convert the video bbbVideo_480.mp4 into  extension
    os.system("ffmpeg -i bbbVideo_480.mp4 -c:v libaom-av1 -b:v 1M output_av1.mkv")


ex_1("1min_cuttedVideo.mp4")
