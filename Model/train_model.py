import tensorflow as tf
import data_loader

class TrainModel:
    def get_train_data():
        loader = data_loader.DataLoader()
        (X_train, Y_train) = loader.load_data("clothing-dataset-resized", data_loader.TEST)
        return (X_train, Y_train)

train_model = TrainModel()
(X_train, Y_train) = train_model.get_train_data()