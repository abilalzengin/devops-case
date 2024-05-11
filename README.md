# Devops-case
## The code used to deploy Prometheus Node Exporter and Grafana to a Kubernetes environment:

~~~
helm repo add grafana https://grafana.github.io/helm-charts &&
  helm repo update &&
  helm upgrade --install --atomic --timeout 300s grafana-k8s-monitoring grafana/k8s-monitoring \
    --namespace "default" --create-namespace --values - <<EOF
cluster:
  name: my-cluster
externalServices:
  prometheus:
    host: https://prometheus-prod-13-prod-us-east-0.grafana.net
    basicAuth:
      username: "1571525"
      password: REPLACE_WITH_ACCESS_POLICY_TOKEN
  loki:
    host: https://logs-prod-006.grafana.net
    basicAuth:
      username: "885719"
      password: REPLACE_WITH_ACCESS_POLICY_TOKEN
  tempo:
    host: https://tempo-prod-04-prod-us-east-0.grafana.net:443
    basicAuth:
      username: "880035"
      password: REPLACE_WITH_ACCESS_POLICY_TOKEN
metrics:
  enabled: true
  cost:
    enabled: true
  node-exporter:
    enabled: true
logs:
  enabled: true
  pod_logs:
    enabled: true
  cluster_events:
    enabled: true
traces:
  enabled: true
receivers:
  grpc:
    enabled: true
  http:
    enabled: true
  zipkin:
    enabled: true
opencost:
  enabled: true
  opencost:
    exporter:
      defaultClusterId: my-cluster
    prometheus:
      external:
        url: https://prometheus-prod-13-prod-us-east-0.grafana.net/api/prom
kube-state-metrics:
  enabled: true
prometheus-node-exporter:
  enabled: true
prometheus-operator-crds:
  enabled: true
alloy: {}
alloy-events: {}
alloy-logs: {}
EOF
~~~

## The PromQL codes for the three alarms installed in Grafana:

### Alarm for pods that are not in a ready state:
~~~
sum by (namespace, pod, job, cluster) (
  max by(namespace, pod, job, cluster) (
    kube_pod_status_phase{job!="", phase=~"Pending|Unknown|Failed|ImagePullBackOff|CrashLoopBackOff|ErrImagePull"}
  ) * on(namespace, pod, cluster) group_left(owner_kind) topk by(namespace, pod, cluster) (
    1, max by(namespace, pod, owner_kind, cluster) (kube_pod_owner{owner_kind!="Job"})
  )
) > 0
~~~
### Alarm for pods with potential CPU performance issues
~~~
sum(increase(container_cpu_cfs_throttled_periods_total{container!="", }[5m])) by (cluster, container, pod, namespace)
  /
sum(increase(container_cpu_cfs_periods_total{}[5m])) by (cluster, container, pod, namespace)
  > ( 25 / 100 )
~~~
### Alarm for potential memory shortage within a cluster
~~~
sum(namespace_memory:kube_pod_container_resource_requests:sum{}) by (cluster) - (sum(kube_node_status_allocatable{resource="memory", job!=""}) by (cluster) - max(kube_node_status_allocatable{resource="memory", job!=""}) by (cluster)) > 0
and
(sum(kube_node_status_allocatable{resource="memory", job!=""}) by (cluster) - max(kube_node_status_allocatable{resource="memory", job!=""}) by (cluster)) > 0
~~~


