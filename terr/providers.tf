terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "4.50.0"
    }
    local = {
      source  = "hashicorp/local"
      version = "2.3.0"

    }
  }
  backend "gcs" {
    bucket  = "tf-state-dvir"
    prefix  = "terraform/state"
  }
}

provider "google" {
  project = "task-1"
  region  = "us-central1"
  zone    = "us-central1-c"
}
