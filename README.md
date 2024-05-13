# 1-Infrastructure Setup
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

Later on, a pod was created with an incorrect image, triggering the 'pod-not-ready' alarm, and it was observed to be functioning. Additionally, it was noted that an email notification was received at the email address defined along with the rule.

![Image Alt text](/images/alarm-firing.png)
![Image Alt text](/images/e-mail.png)



# 2-Infrastructure Design
Ansible was installed as the configuration management tool. Ansible-related files can be found at https://github.com/abilalzengin/devops-case/tree/main/config-files/ansible directory. In the example 'inventory.txt' file, 'webservers' and 'dbservers' groups were created to include VMs deployed on AWS, with only a total of 3 VMs defined due to limited resources. Subsequently, the 'add-host.yaml' file was executed with the 'ansible-playbook' command to append the line '192.168.0.10 example.com' to the '/etc/hosts' files of VMs in the 'webservers' group. Later, this action was reverted using the 'delete-host.yaml' file. With Ansible, different groupings can be made for thousands of nodes within the same file, or each group can be added to different 'inventory.txt' files, enabling specific configuration settings for specific groups.

![Image Alt text](/images/ansible-ping.png)
![Image Alt text](/images/ansible-add-host.png)
![Image Alt text](/images/ansible-delete-host.png)


# 3-Software Development
A Python code was written to display the certificates of Kubernetes services along with their expiration dates. The code includes fetching the certificates from the kube-master, decrypting the encrypted certificate contents to find the desired information, and displaying this information on the screen. The code was pushed to a GitHub repository, and a Dockerfile was written for Docker image operations. The image was minimized using the python-slim image, and Dockerization processes were performed in two stages, with unnecessary files being deleted in the first stage before moving on to the second stage. A GitHub Actions workflow file was created for CI/CD processes. Due to security requirements, sensitive content was defined as secrets in the file. The file can be found at https://github.com/abilalzengin/devops-case/blob/main/config-files/cicd-pipeline/github-actions-deploy.yaml. The CI/CD was executed, resulting in the creation of the image and automatic deployment of the created image to our Kubernetes cluster. The application output was viewed by entering the port via the server IP using the created deployment and service for the application. The Kubernetes deployment file can be found at https://github.com/abilalzengin/devops-case/blob/main/config-files/k8s/deployment.yaml .

![Image Alt text](/images/k8s-app-pod.png)
![Image Alt text](/images/k8s-app-screen.png)




 


