provider "kubernetes" {
    host     = "https://${google_container_cluster.primary.endpoint}:443"
    username = var.gke_username
    password = var.gke_password

    client_certificate     = google_container_cluster.primary.master_auth.0.client_certificate
    client_key             = google_container_cluster.primary.master_auth.0.client_key
    cluster_ca_certificate = local_file.cert.content
}


resource "kubernetes_namespace" "for_the_memes" {
    metadata {
        name = "my-first-namespace"
    }
}