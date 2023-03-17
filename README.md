# portfolio-
[![CI](https://github.com/dvir-pashut/portfolio-/actions/workflows/ci.yaml/badge.svg?branch=main)](https://github.com/dvir-pashut/portfolio-/actions/workflows/ci.yaml)
### this is the application repo
check the manifist repo [here](https://github.com/dvir-pashut/port-infra).
and the gitops repo  [here](https://github.com/dvir-pashut/port-charts).

## repo summery
this repo contains the apllication itself the static files and the CI-CD file
to build localy you can run <br> 
sh'''
docker compose up -d
''' 


## the project architecture
![Project architecture](nginx/static/images/project/project-detail/project-architecture.jpg)<br>
## the app architecture
![app architecture](nginx/static/images/project/project-detail/app_architecture.jpg)<br>
## the git workflow
![git workflow](nginx/static/images/project/project-detail/git_workflow.jpg)<br>
## grafana dashboard
![grafana dashboard](nginx/static/images/project/project-detail/grafana_dashboard.png)<br>
## kibana dashboard
![kibana dashboard](nginx/static/images/project/project-detail/kibana_dashboard.png)<br>

## simply running terraform apply will give you this 
![argo dashboard](nginx/static/images/project/project-detail/argo_dashboard.png)


## the tools for the project
<ol>
  <li><span>Ci         - github action</span></li>
  <li><span>notifications   - slack</span></li>
  <li><span>cloud      - gcp</span></li>
  <li><span>deployment - k8s</span></li>
  <li><span>database       - mongodb</span></li>
  <li><span>rest api   - Flask(python)</span></li>
  <li><span>logging       - EFK(elastic, fluentd, kibana)</span></li>
  <li><span>monitoring       - prometheus and grafana</span></li>
  <li><span>certification       - let's encrypt</span></li>
  <li><span>IAC       - terraform</span></li>
  <li><span>secrete managment       - bitnami sealed secretes+ google secretes</span></li>
  <li><span>gitops       - argocd</span></li>
  <li><span>static files       - gcp bucket</span></li>
</ol>
