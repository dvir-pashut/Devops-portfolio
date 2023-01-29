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
    prefix  = "portfolio/state"
  }
}

provider "google" {
  project = var.project_id
  region  = var.region
  zone    = var.zone
}
