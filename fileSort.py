import os
from shutil import copy


def main(model_name, test_name, results_name,next_name):
    baseRoot = "T:\\blurResult\Dong_cvpr2022"
    filePath = os.path.join(baseRoot, "baseline", "GoPro", model_name, test_name, "results", results_name, next_name)
    resultPath = os.path.join(baseRoot, "summary", model_name)
    print(filePath)
    cnt = 0
    if not os.path.exists(resultPath):
        os.makedirs(resultPath)
    for file in os.listdir(filePath):
        print(file)
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


main("3DeepRFT_w_haar", "code220630_deeprft_affhaar_b8_test", "DeepRFT_affhaar_b8", "3DeepRFT_w_haar_GoPro")
