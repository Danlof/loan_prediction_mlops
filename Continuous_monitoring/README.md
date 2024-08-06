## Working with Prometheus
### Installation steps

- Launch an EC2 instance with Ubuntu and run the below commands
- Open the traffic for all the ports (All Traffic - anywhere ipv4)

```
sudo su -
chmod u=rwx,g=r,o=r 1-install.sh
./1-install.sh
ps aux | grep prometheus
sudo service prometheus start
sudo service prometheus status

cat /etc/prometheus/prometheus.yml

chmod u=rwx,g=r,o=r 3-install-grafana.sh
./3-install-grafana.sh
sudo service grafana-server status

# default username & password is : admin

ps uax | grep prometheus

cat /etc/prometheus/prometheus.yml

```

