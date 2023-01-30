resource "google_service_account" "default" {
  account_id   = "for-the-nodes"
  display_name = "Service Account"
}

resource "google_container_cluster" "primary" {
  name     = "${var.project_id}-gke"
  location = var.region
  network    = google_compute_network.vpc.name
  subnetwork = google_compute_subnetwork.subnet.name
  node_locations = ["us-central1-f","us-central1-a"]

  # We can't create a cluster with no node pool defined, but we want to only use
  # separately managed node pools. So we create the smallest possible default
  # node pool and immediately delete it.
  remove_default_node_pool = true
  initial_node_count       = 1
}

resource "google_container_node_pool" "primary_preemptible_nodes" {
  name       = "my-pool-of-nodes"
  cluster    = google_container_cluster.primary.id
  node_count = 1
  
  autoscaling {
    min_node_count = 1
    max_node_count = 2
  }
  

  node_config {
    preemptible  = true
    machine_type = "e2-medium"
    disk_size_gb = 100

    # Google recommends custom service accounts that have cloud-platform scope and permissions granted via IAM Roles.
    service_account = google_service_account.default.email
    oauth_scopes = [
      "https://www.googleapis.com/auth/cloud-platform"
    ]
  }
}
