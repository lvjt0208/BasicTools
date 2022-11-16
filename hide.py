import os
from shutil import copy

def main():
    cnt=0
    baser=r"D:\2022_11\11_16_HIDE\ours"
    baseRoot=r"D:\2022_11\11_16_HIDE\ours\YzbTestHIDE"
    filelist=os.listdir(baseRoot)
    for file in filelist:
        frame,video=file.split("fromGOPR")
        if "MP4" in file.split("."):
            videoname,_,__=video.split(".")
        else:
            videoname,_=video.split(".")
        print(videoname,frame)
        srcPath=os.path.join(baseRoot,file)
        dstPath=os.path.join(baser,"sortbyvideo",videoname)
        if not os.path.exists(dstPath):
            os.makedirs(dstPath)
        copy(srcPath,dstPath)
        cnt+=1
        #break
    print(cnt)
main()
def test():
    file="22fromGOPR1040.MP4.png"
    if "MP4" in file.split("."):
        pass