# VPC
resource "google_compute_network" "vpc" {
    name                    = "${var.project_id}-vpc"
    auto_create_subnetworks = "false"
}

# Subnet
resource "google_compute_subnetwork" "subnet" {
    name          = "${var.project_id}-subnet"
    region        = var.region
    network       = google_compute_network.vpc.name
    ip_cidr_range = "10.10.0.0/24"
}

/* # Subnet
resource "google_compute_subnetwork" "subnet2" {
    name          = "${var.project_id}-subnet-for-pods1"
    region        = var.region
    network       = google_compute_network.vpc.name
    ip_cidr_range = "10.11.0.0/24"
}

# Subnet
resource "google_compute_subnetwork" "subnet3" {
    name          = "${var.project_id}-subnet-for-pods2"
    region        = var.region
    network       = google_compute_network.vpc.name
    ip_cidr_range = "10.12.0.0/24"
} */