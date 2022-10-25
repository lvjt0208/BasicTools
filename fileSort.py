import os
from shutil import copy

baseRoot = "T:/blurResult/GoPro"
filePath = os.path.join(baseRoot, 'ours', 'DeepRFT', 'GoPro')
resultPath = os.path.join(baseRoot, "summary", "Ours")

cnt = 0
if not os.path.exists(resultPath):
    os.makedirs(resultPath)
for file in os.listdir(filePath):
    videoName, imgName = file.split('-')
    videoPath = os.path.join(resultPath, videoName)
    if not os.path.exists(videoPath):
        os.makedirs(videoPath)
    copy(os.path.join(filePath, file), videoPath)
    # print(os.path.join(filePath, file))
    # print(videoPath)
    print(imgName)
    cnt += 1
print("总数：", cnt)
