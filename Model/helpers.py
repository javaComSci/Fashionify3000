TRAIN = "train"
TEST = "test"
VALIDATION = "validation"

name_to_typeint = {
    "longsleeve": 0,
    "skirt": 1,
    "dress": 2,
    "pants": 3,
    "t-shirt": 4,
    "hat": 5, 
    "shoes": 6,
    "shorts": 7,
    "outwear": 8,
    "shirt": 9
}

typeint_to_name = {
    0: "longsleeve",
    1: "skirt",
    2: "dress",
    3: "pants",
    4: "t-shirt",
    5: "hat",
    6: "shoes",
    7: "shorts",
    8: "outwear",
    9: "shirt"
}

def get_typeint_from_name(name):
    return name_to_typeint[name]

def get_name_from_typeint(typeint):
    return typeint_to_name[typeint]
