from enum import Enum
import os
import numpy as np
from PIL import Image

TRAIN = "train"
TEST = "test"
VALIDATION = "validation"

class DataLoader:
    def load_data(self, type):
        data = []

        basePath = "clothing-dataset-small"
        basePathWithType = basePath + "/" + type
    
        for encodedClothingType in os.listdir(os.fsencode(basePathWithType)):
            decodedClothingType = os.fsdecode(encodedClothingType)
            clothingTypePath = basePathWithType + "/" + decodedClothingType
            for encodedClothing in os.listdir(os.fsencode(clothingTypePath)):
                decodedClothing = os.fsdecode(encodedClothing)
                clothingPath = clothingTypePath + "/" + decodedClothing
                print(clothingPath)
                clothingImage = Image.open(clothingPath)
                clothing = np.asarray(clothingImage)
                data.append(clothing)
        
        print(data)


loader = DataLoader()
loader.load_data(TEST)