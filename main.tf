provider "google" {
  project = "seu-projeto-gcp"
  region  = "us-central1"
}

resource "google_storage_bucket" "ml_bucket" {
  name     = "ml-bucket-${var.project_id}"
  location = "US"
}

resource "google_composer_environment" "ml_composer" {
  name   = "ml-composer-env"
  region = "us-central1"

  config {
    node_count = 3
    node_config {
      machine_type = "n1-standard-1"
      zone         = "us-central1-a"
    }
  }
}

resource "google_vertex_ai_dataset" "ml_dataset" {
  display_name = "ml-dataset"
  region       = "us-central1"
}

resource "google_vertex_ai_training_job" "ml_training_job" {
  display_name = "ml-training-job"
  region       = "us-central1"
  dataset_id   = google_vertex_ai_dataset.ml_dataset.id
  model_display_name = "ml-model"
  training_container_spec {
    image_uri = "gcr.io/cloud-aiplatform/training/tf-cpu.2-3:latest"
  }
}