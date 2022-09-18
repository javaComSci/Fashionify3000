import tensorflow as tf
import data_loader
import helpers

class TrainModel:
    def get_train_data(self):
        loader = data_loader.DataLoader()
        (X_train, Y_train) = loader.load_data("clothing-dataset-resized", helpers.TEST)
        self.X_train = X_train
        self.Y_train = Y_train

    def create_model(self):
        self.model = tf.keras.models.Sequential([
            tf.keras.layers.Dense(128, activation='relu')
        ])
    
    def train(self):
        self.model.compile(optimizer="adam")
        self.model.fit(self.X_train[:1], self.Y_train[:1], epochs=1)

train_model = TrainModel()
train_model.get_train_data()
train_model.create_model()
train_model.train()