# Setup the EKS Cluster for OpenRMF
`AWS_PROFILE=xxxxxxxx eksctl create cluster -f demo-bottlerocket.yaml`

# Setup metrics

https://docs.aws.amazon.com/eks/latest/userguide/metrics-server.html

Run `kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml`

Run `kubectl get deployment metrics-server -n kube-system` to make srue it is working.

# Prometheus Metrics
Run the following to install it into your K8s space in EKS
https://www.infracloud.io/blogs/prometheus-operator-helm-guide/

```
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm install openrmfprotest-prometheus prometheus-community/kube-prometheus-stack
```

Check status with `kubectl --namespace default get pods -l "release=openrmfprotest-prometheus`. 

Run `kubectl get prometheus -o yaml --all-namespaces` and look for the "serviceMonitorSelector" to find the release and release value. Those get plugged into the values.yaml file.

```
    securityContext:
      fsGroup: 2000
      runAsGroup: 2000
      runAsNonRoot: true
      runAsUser: 1000
    serviceAccountName: openrmfprotest-prometheus-prometheus
    serviceMonitorNamespaceSelector: {}
    serviceMonitorSelector:
      matchLabels:
        release: openrmfprotest-prometheus
    shards: 1
    version: v2.28.1
```

You can run the `kubectl get pods -o wide` in the main default namespace or wherever you installed the Prometheus and Grafana pods to get the pod names. 

Redirect with `kubectl port-forward prometheus-openrmfprotest-prometheus-prometheus-0 9090` to show the information in Prometheus. 

Redirect with `kubectl port-forward openrmfprotest-prometheus-grafana-77546d745-vq6s2 3000` to show the information in Grafana.

Run `kubectl get secret openrmfprotest-prometheus-grafana -o jsonpath="{.data.admin-user}" | base64 --decode ; echo` to get the username. Usually `admin`.

Run `kubectl get secret openrmfprotest-prometheus-grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo` to get the password. Usually `prom-operator`.

To expose the URL to the world, you can follow https://github.com/prometheus-operator/kube-prometheus/blob/main/docs/exposing-prometheus-alertmanager-grafana-ingress.md 

# Logging in your EKS Cluster

Follow the instructions in https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-setup-logs-FluentBit.html for logging if you have no logging at all.

Parameters:
```
ClusterName=cluster-name
RegionName=cluster-region
FluentBitHttpPort='2020'
FluentBitReadFromHead='Off'
[[ ${FluentBitReadFromHead} = 'On' ]] && FluentBitReadFromTail='Off'|| FluentBitReadFromTail='On'
[[ -z ${FluentBitHttpPort} ]] && FluentBitHttpServer='Off' || FluentBitHttpServer='On'
```
Make sure you follow the prerequisites for https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-prerequisites.html the logging correctly for this method. 

Setup the namespace:
`kubectl apply -f https://raw.githubusercontent.com/aws-samples/amazon-cloudwatch-container-insights/latest/k8s-deployment-manifest-templates/deployment-mode/daemonset/container-insights-monitoring/cloudwatch-namespace.yaml`

Run this command to load the logs into CloudWatch from the information above: 
`kubectl create configmap fluent-bit-cluster-info --from-literal=cluster.name=openrmfpro-demo --from-literal=http.server=On --from-literal=http.port=2020 --from-literal=read.head=Off --from-literal=read.tail=On --from-literal=logs.region=us-east-1 -n amazon-cloudwatch`

`kubectl create configmap fluent-bit-cluster-info --from-literal=cluster.name=openrmfpro-test --from-literal=http.server=On --from-literal=http.port=2020 --from-literal=read.head=Off --from-literal=read.tail=On --from-literal=logs.region=us-east-2 -n amazon-cloudwatch`

Then

`kubectl apply -f https://raw.githubusercontent.com/aws-samples/amazon-cloudwatch-container-insights/latest/k8s-deployment-manifest-templates/deployment-mode/daemonset/container-insights-monitoring/fluent-bit/fluent-bit.yaml`

# K8s Dashboard
If you want the dashboard follow https://docs.aws.amazon.com/eks/latest/userguide/dashboard-tutorial.html 

# Setup Networking

kubectl apply -f https://raw.githubusercontent.com/aws/amazon-vpc-cni-k8s/release-1.6/config/v1.6/calico.yaml

# Example Output

```
[ℹ]  node "ip-192-168-24-42.us-east-2.compute.internal" is ready
[ℹ]  node "ip-192-168-40-179.us-east-2.compute.internal" is ready
[ℹ]  node "ip-192-168-75-107.us-east-2.compute.internal" is ready
```

# Connect to Grafana and Prometheus

`kubectl port-forward -n default prometheus-prometheus-operator-158963-prometheus-0 9090`

`kubectl port-forward -n default deploy/prometheus-operator-1595075655-grafana 3000`

# Deleting Stack not working
Check the load balancer as you create one when you run the NGINX Ingress setup. If you do not manually delete all you create, this may hang you up on 100% removal of the stack.

# Storage Driver

aws iam attach-role-policy --policy-arn arn:aws:iam::xxxxxxxxxxxxxxxxxx:policy/Amazon_EBS_CSI_Driver --role-name eksctl-openrmf-test-nodegroup-ope-NodeInstanceRole-1JRJM8G2NS1VL