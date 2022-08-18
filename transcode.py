import subprocess
import os

ffmpeg = "/usr/bin/ffmpeg"

def transcode(folderpath):
    #full_path = os.path.join(folderpath, file)
    video_name = folderpath.split(os.path.sep)[-1]
    # originFile = folderpath.split(os.path.sep)[-1] + '.mp4'
    # command_list = [
    #     ffmpeg,
    #     "-i",
    #     folderpath + "/" + "m_" + video_name + ".mp4",
    #     "-c:v",
    #     "libx264",
    #     "-b:v",
    #     "3M",
    #     "-preset",
    #     "superfast",
    #     folderpath + "/" + video_name + ".mp4"
    #     ]
    command_list = [
        ffmpeg,
        "-i",
        folderpath + "/" + video_name + ".mp4",
        "-c:v",
        "copy",
        "-c:a",
        "copy",
        folderpath + "/" + "m_" + video_name + ".mp4"
    ]

    print("Transcode: " + str(command_list))
    if subprocess.run(command_list).returncode == 0:
        print("FFmpeg run successfully.")
    else:
        print("Error transcod.")

    delCmd = [
        "rm",
        folderpath + "/" + video_name + ".mp4"
    ]
    if subprocess.run(delCmd).returncode == 0:
        print("rm run successfully.")
    else:
        print("Error rm.")


    mvCmd = [
        "mv",
        folderpath + "/" + "m_" + video_name + ".mp4",
        folderpath + "/" + video_name + ".mp4",
    ]

    if subprocess.run(mvCmd).returncode == 0:
        print("mv run successfully.")
    else:
        print("Error mv.")
     
