import os
import shutil
import numpy as np
from PIL import Image
import helpers

class DataLoader:
    def get_image_sizes(self, basePath, type):
        basePathWithType = basePath + "/" + type
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
                print("IMAGE", clothingPath, clothing.shape, height, width)

        print("Rows lengths counts", rowsCounts)
        print("Cols lengths counts", colsCounts)



    def resize_images(self, basePath, newPath, type):
        basePathWithType = basePath + "/" + type
        newPathWithType = newPath + "/" + type
        if os.path.exists(newPathWithType):
            shutil.rmtree(newPathWithType)
        os.makedirs(newPathWithType)
        for encodedClothingType in os.listdir(os.fsencode(basePathWithType)):
            decodedClothingType = os.fsdecode(encodedClothingType)
            if decodedClothingType == ".DS_Store":
                continue
            clothingTypePath = basePathWithType + "/" + decodedClothingType
            newClothingTypePath = newPathWithType + "/" + decodedClothingType
            if os.path.exists(newClothingTypePath):
                shutil.rmtree(newClothingTypePath)
            os.makedirs(newClothingTypePath)
            for encodedClothing in os.listdir(os.fsencode(clothingTypePath)):
                decodedClothing = os.fsdecode(encodedClothing)
                clothingPath = clothingTypePath + "/" + decodedClothing
                newClothingPath = newClothingTypePath + "/" + decodedClothing
                clothingImage = Image.open(clothingPath)
                # clothingImage = clothingImage.convert("1")
                newClothingImage = clothingImage.resize((256, 256), Image.LANCZOS)
                newClothingImage.save(newClothingPath, quality=95)
                print("NEW PATH", newClothingPath)


                oldWidth, oldHeight = clothingImage.size
                newWidth, newHeight = newClothingImage.size
                # print(Image.open(newClothingPath).size)
                print("IMAGE", clothingPath, oldHeight, oldWidth, newHeight, newWidth)


    def load_data(self, basePath, type):
        X_full = []
        Y_full = []
        basePathWithType = basePath + "/" + type
        for encodedClothingType in os.listdir(os.fsencode(basePathWithType)):
            decodedClothingType = os.fsdecode(encodedClothingType)

            if decodedClothingType == ".DS_Store":
                continue

            clothingTypePath = basePathWithType + "/" + decodedClothingType
            clothingTypeInt = helpers.get_typeint_from_name(decodedClothingType)

            for encodedClothing in os.listdir(os.fsencode(clothingTypePath)):
                decodedClothing = os.fsdecode(encodedClothing)
                clothingPath = clothingTypePath + "/" + decodedClothing
                clothingImage = Image.open(clothingPath)
                clothing = np.asarray(clothingImage)
                clothingReshaped = clothing.reshape(-1)
                # print(clothingReshaped.shape)

                X_full.append(clothingReshaped)
                Y_full.append(clothingTypeInt)
                
        
        X_np = np.array(X_full)
        Y_np = np.array(Y_full)
        print(X_np.shape)
        print(Y_np.shape)

        return (X_full, Y_full)


# loader = DataLoader()

# Majority of rows are 711 or 400
# Majority of cols are 400
# loader.get_image_sizes("clothing-dataset-small", TEST)

# loader.resize_images("clothing-dataset-small", "clothing-dataset-resized", TEST)

# loader.load_data("clothing-dataset-resized", helpers.TEST)