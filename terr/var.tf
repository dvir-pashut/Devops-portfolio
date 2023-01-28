variable "gke_num_nodes" {
    default     = 2
    description = "number of gke nodes"
}

variable "project_id" {
    description = "project id"
}

variable "region" {
    description = "region"
}

provider "google" {
    project = var.project_id
    region  = var.region
}