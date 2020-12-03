from imageai.Prediction.Custom import ModelTraining
import os

trainer = ModelTraining()
#trainer.setModelTypeAsDenseNet()
trainer.setModelTypeAsSqueezeNet()
#trainer.setModelTypeAsInceptionV3()
trainer.setDataDirectory("weapons")
trainer.trainModel(num_objects=10, num_experiments=50, enhance_data=True, batch_size=10, show_network_summary=True,transfer_from_model="squeezenet_weights_tf_dim_ordering_tf_kernels.h5", initial_num_objects=1000)