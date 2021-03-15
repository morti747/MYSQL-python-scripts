# MYSQL-python-scripts
How to install MYSQL on Linux server and use Python scripts to manage your database


# :zap: How to prepare our Linux server :zap: 
:star: . 
```
sudo apt-get update
```
##
<img src=images/1.PNG  alt="alt text" width="550" height="250">

##


```
sudo apt-get upgrade
```
##
<img src=images/2.PNG  alt="alt text" width="550" height="250">

##



```
sudo apt-get install mysql-server 
```
##
<img src=images/3.PNG  alt="alt text" width="550" height="450">

##


```
mysql --version 
```
##
<img src=images/4.PNG  alt="alt text" width="550" height="250">

##


## :one: Make security configurations by running the provided security script: 


```
sudo mysql_secure_installation
```
##
<img src=images/5.PNG  alt="alt text" width="600" height="250">

##
##
<img src=images/6.PNG  alt="alt text" width="600" height="200">




## :zap: This is our topology :zap:
:star: we will use one router and one switch with three vlans and each vlan will receive IP address directly from DHCP server configured on my router.
<img src=images/1.PNG  alt="alt text" width="650" height="500">


#  :pushpin: Configuration of Router:

## :one: Connecrting remotely using SSH: 
:star: Connecting to our router from distance usign this set of commands. SSH helps us to connect to our router with our username and password: 
