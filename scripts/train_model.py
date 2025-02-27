from google.cloud import aiplatform
from google.cloud import storage
import os

def train_model():
    aiplatform.init(project="seu-projeto-gcp", location="us-central1")

    job = aiplatform.CustomTrainingJob(
        display_name="ml-training-job",
        script_path="gs://ml-bucket-seu-projeto-gcp/train_script.py",
        container_uri="gcr.io/cloud-aiplatform/training/tf-cpu.2-3:latest",
        requirements=["gcsfs==2021.4.0"],
        model_serving_container_image_uri="gcr.io/cloud-aiplatform/prediction/tf2-cpu.2-3:latest",
    )

    model = job.run(
        dataset="ml-dataset",
        model_display_name="ml-model",
        args=["--epochs=10", "--batch_size=32"],
    )

    storage_client = storage.Client()
    bucket = storage_client.bucket("ml-bucket-seu-projeto-gcp")
    blob = bucket.blob("models/ml-model/")
    blob.upload_from_filename("model.h5")

    aiplatform.Model.upload(
        display_name="ml-model",
        artifact_uri="gs://ml-bucket-seu-projeto-gcp/models/ml-model/",
        serving_container_image_uri="gcr.io/cloud-aiplatform/prediction/tf2-cpu.2-3:latest",
    )

if __name__ == "__main__":
    train_model()