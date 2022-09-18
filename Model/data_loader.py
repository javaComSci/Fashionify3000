from enum import Enum
import os
import numpy as np
from PIL import Image

TRAIN = "train"
TEST = "test"
VALIDATION = "validation"

class DataLoader:
    def resize_images(self, type):
        basePath = "clothing-dataset-small"
        basePathWithType = basePath + "/" + type

        newPath = "clothing-dataset-resized"
        newPathWithType = newPath + "/" + type
        if os.path.exists(newPathWithType):
            shutil.rmtree(newPathWithType)
        os.makedirs(dir)

        rowsCounts = {}
        colsCounts = {}
    
        for encodedClothingType in os.listdir(os.fsencode(basePathWithType)):
            decodedClothingType = os.fsdecode(encodedClothingType)
            clothingTypePath = basePathWithType + "/" + decodedClothingType

            if decodedClothingType == ".DS_Store":
                continue

            for encodedClothing in os.listdir(os.fsencode(clothingTypePath)):
                decodedClothing = os.fsdecode(encodedClothing)
                clothingPath = clothingTypePath + "/" + decodedClothing
                clothingImage = Image.open(clothingPath)
                clothing = np.asarray(clothingImage)

                if clothing.shape[0] not in rowsCounts:
                    rowsCounts[clothing.shape[0]] = 1
                else:
                    rowsCounts[clothing.shape[0]] += 1
                
                if clothing.shape[1] not in colsCounts:
                    colsCounts[clothing.shape[1]] = 1
                else:
                    colsCounts[clothing.shape[1]] += 1
                
                width, height = clothingImage.size
                print(clothingPath)
                print(clothing.shape)
                print("IMAGE", height, width)

        # Majority of rows are 711 or 400, so will resize them to 400
        print("Rows lengths counts", rowsCounts)

        # Majority of cols are 400
        print("Cols lengths counts", colsCounts)


    def load_data(self, type):
        data = []

        basePath = "clothing-dataset-small"
        basePathWithType = basePath + "/" + type
    
        for encodedClothingType in os.listdir(os.fsencode(basePathWithType)):
            decodedClothingType = os.fsdecode(encodedClothingType)
            clothingTypePath = basePathWithType + "/" + decodedClothingType

            if decodedClothingType == ".DS_Store":
                continue

            for encodedClothing in os.listdir(os.fsencode(clothingTypePath)):
                decodedClothing = os.fsdecode(encodedClothing)
                clothingPath = clothingTypePath + "/" + decodedClothing
                clothingImage = Image.open(clothingPath)
                clothing = np.asarray(clothingImage)
                data.append(clothing)
        
        print(data)


loader = DataLoader()
loader.resize_images(TEST)