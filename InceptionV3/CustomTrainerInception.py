from imageai.Prediction.Custom import ModelTraining
import os

trainer = ModelTraining()
trainer.setModelTypeAsInceptionV3()
trainer.setDataDirectory("weapons")
trainer.trainModel(num_objects=10, num_experiments=50, enhance_data=True, batch_size=15, show_network_summary=True,transfer_from_model="inception_v3_weights_tf_dim_ordering_tf_kernels.h5", initial_num_objects=1000)