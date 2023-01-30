output "region" {
    value       = var.region
    description = "GCloud Region"
}

output "project_id" {
    value       = var.project_id
    description = "GCloud Project ID"
}

output "kubernetes_cluster_name" {
    value       = google_container_cluster.primary.name
    description = "GKE Cluster Name"
}

output "kubernetes_cluster_host" {
    value       = google_container_cluster.primary.endpoint
    description = "GKE Cluster Host"
}

output "cert" {
    value = google_container_cluster.primary.master_auth.0.cluster_ca_certificate
    description = "for tests"
}

resource "local_file" "cert" {
    content  = google_container_cluster.primary.master_auth.0.cluster_ca_certificate
    filename = "cert.pem"
}
