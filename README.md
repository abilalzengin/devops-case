# Infrastructure Setup
## K8s Cluster Installation
Kubeadm was used to deploy a cluster consisting of 2 nodes on AWS.

![Image Alt text](/images/k8s-node-info.png)
![Image Alt text](/images/aws-node-info.png)

## Prometheus Node Exporter and Grafana Installation 
Prometheus-Node-Exporter and Grafana were installed using Helm. The installation code can be found at https://github.com/abilalzengin/devops-case/blob/main/config-files/prometheus-grafana/install-prometheus.node.exporter.and.grafana.txt directory.

![Image Alt text](/images/prom-grafana-pods.png)

The nodes and other components were displayed in the Grafana interface.

![Image Alt text](/images/grafana-nodes.png)

Three alarm rules were created in the Grafana interface using PromQL. The codes for the rules can be found at https://github.com/abilalzengin/devops-case/tree/main/config-files/prometheus-grafana directory.

![Image Alt text](/images/grafana-rules.png)



# Infrastructure Design

# Software Development
