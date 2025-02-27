output "bucket_name" {
  value = google_storage_bucket.ml_bucket.name
}

output "composer_env_name" {
  value = google_composer_environment.ml_composer.name
}

output "training_job_name" {
  value = google_vertex_ai_training_job.ml_training_job.name
}