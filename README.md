# MYSQL-python-scripts
How to install MYSQL on Linux server and use Python scripts to manage your database


# :zap: How to prepare our Linux server :zap: 
:star: Step 1: Update repository index. 
```
sudo apt-get update
```
##
<img src=images/1.PNG  alt="alt text" width="550" height="250">

##

:star: Step 1: Upgrade repository index.
```
sudo apt-get upgrade
```
##
<img src=images/2.PNG  alt="alt text" width="550" height="250">

##

:star: Step 2: Install MySQL server with apt

```
sudo apt-get install mysql-server 
```
##
<img src=images/3.PNG  alt="alt text" width="650" height="450">

##

:star: Step 3: Verify the installation (optional)
```
mysql --version 
```
##
<img src=images/4.PNG  alt="alt text" width="550" height="250">

##


## Step 4: Make security configurations by running the provided security script: 


```
sudo mysql_secure_installation
```
##
<img src=images/5.PNG  alt="alt text" width="600" height="250">

##
Morteza123@$
##
<img src=images/6.PNG  alt="alt text" width="600" height="200">

##
##
<img src=images/7.PNG  alt="alt text" width="600" height="550">

##

Testing if MySQL is running
```
systemctl status mysql.service
```
##
<img src=images/9.PNG  alt="alt text" width="600" height="300">

##




Step 1: Start MySQL Shell

```
sudo mysql
```

##
<img src=images/8.PNG  alt="alt text" width="600" height="350">

##
##

Testing if SSH is running
```
sudo systemctl status ssh
```
##
<img src=images/10.PNG  alt="alt text" width="600" height="350">

##
##
Enabling SSH on Ubuntu

```
sudo apt install openssh-server
```

##
##
Testing again if SSH is running
```
sudo systemctl status ssh
```
##
<img src=images/12.PNG  alt="alt text" width="600" height="350">

##

Testing SSH connection from Windows 10: 
```
ssh morti@192.168.8.194
```
##
<img src=images/13.PNG  alt="alt text" width="600" height="650">

##
