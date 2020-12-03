from imageai.Prediction.Custom import ModelTraining
import os

trainer = ModelTraining()
trainer.setModelTypeAsDenseNet()
trainer.setDataDirectory("weapons")
trainer.trainModel(num_objects=10, num_experiments=50, enhance_data=True, batch_size=10, show_network_summary=True,transfer_from_model="DenseNet-BC-121-32.h5", initial_num_objects=1000)