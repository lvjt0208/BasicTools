import os
from shutil import copy


def main():
    baseRoot = "T:/blurResult/GoPro/summary"
    models = ['DeepRFT_PLUS', 'DMPHN', 'MPRNet', 'MPRNetLocal', 'NAFNet_width64', 'Ours', 'Restormer',
              'RestormerLocal']
    resultPath = os.path.join("T:/blurResult/GoPro", 'compare')
    videoName = "GOPR0410_11_00"
    imageName = videoName + "-000191.png"
    for model in models:
        srcPath = os.path.join(baseRoot, model, videoName, imageName)
        dstPath = os.path.join(resultPath, videoName, model)
        if not os.path.exists(dstPath):
            os.makedirs(dstPath)
        copy(srcPath, dstPath)
        print(dstPath)


def teshu():
    baseRoot = "T:/blurResult/GoPro/summary"
    videoName = "GOPR0410_11_00"
    mimoImg = videoName + "-000191mimo.png"
    resultPath = os.path.join("T:/blurResult/GoPro", 'compare')
    srcPath = os.path.join(baseRoot, "MIMO", videoName, mimoImg)
    dstPath = os.path.join(resultPath, videoName, "MIMO")
    if not os.path.exists(dstPath):
        os.makedirs(dstPath)
    copy(srcPath, dstPath)
    print(dstPath)
    stripImg = "000191.png"
    srcPath = os.path.join(baseRoot, "Stripformer", videoName, stripImg)
    dstPath = os.path.join(resultPath, videoName, "StripFormer")
    if not os.path.exists(dstPath):
        os.makedirs(dstPath)
    copy(srcPath, dstPath)
    print(dstPath)


if __name__ == '__main__':
    main()
    teshu()
