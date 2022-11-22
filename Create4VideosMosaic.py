#FUNCTION TO GENERATE THE VIDEO WITH THE 4 VIDEOS
import os


def mosaic_4videos():
   os.system('ffmpeg -i output_vp8.webm -i output_vp9.webm -i output_h265.mp4 -i output_av1.mkv -filter_complex "nullsrc=size=640x480 [base]; [0:v] setpts=PTS-STARTPTS, scale=320x240 [upperleft]; [1:v] setpts=PTS-STARTPTS, scale=320x240 [upperright]; [2:v] setpts=PTS-STARTPTS, scale=320x240 [lowerleft]; [3:v] setpts=PTS-STARTPTS, scale=320x240 [lowerright]; [base][upperleft] overlay=shortest=1 [tmp1]; [tmp1][upperright] overlay=shortest=1:x=320 [tmp2]; [tmp2][lowerleft] overlay=shortest=1:y=240 [tmp3]; [tmp3][lowerright] overlay=shortest=1:x=320:y=240" -c:v libx264 mosaic_4videos.mkv')

mosaic_4videos()
