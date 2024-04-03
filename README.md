## TCP Analysis Project

The goal of this project is to add proxy detection to Nginx's capabilities. To accomplish this, we needed to understand TCP variables set by the kernel of each machine. When using a proxy, the TCP connection and the TLS connection have different exit nodes, this means that the TLS user-agent and the TCP connection will have differing operating systems. 

If we can detect this difference through machine learning or a database of known TCP connections, we can detect proxies and block the connection at the server layer. Both of these methods, Machine Learning and a static database are detailed below.

Currently this code as of 4/3/2024 is running on https://fingerprint.byu.edu

## Nginx Changes

We have made some changes to the Nginx configuration and Nginx source code in order to implement proxy detection.

### default-sites-enabled

In this file, we exposed all TCP INFO variables to display them on our website. We also enabled TLS and redirect all HTTP traffic to the HTTPS.

### nginx.conf

The main configuration change is changing the logformat to log each of the TCP INFO variables. This allows us to use fail2ban to ban IPs after one connection.

### ngx_http_variables.c

In the actual Nginx source code, we use the TCP INFO struct from the kernel and add it as a variable accessible in the logs and in JavaScript with every connection.

## Scripts

### api.py and data.json

This is the API to lookup a fingerprint in the database. The data.json is an example of how the database could look.

### auto_gen_nginx.py

This automatically generates the Nginx source code changes, HTML/JS code, and Nginx configuration changes for the variables we want to expose. For example, if we only wanted to expose TCP_RTT, TCP_OPTIONS, and TCP_SND_WND then we could pass this script tcpi_rtt,tcpi_options,tcpi_snd_wnd.

### ban.py

This is the beginner code to use fail2ban in conjunction with Machine Learning for banning proxies and detecting operating system differences.

### commands.sh

Use this script to compile Nginx.

### final.variables.txt

This text file is to be used in conjunction with auto_gen_nginx.py and contains every variable in the kernel and keeps the order that nginx originally uses.

### format.py

Format.py takes the log from /var/log/nginx/access.log and formats it to be analyzed in machine learning.

### ml.py

This file uses machine learning to detect operating systems based on the TCP fingerprint.

## Website

### css

The CSS files for formatting the website.

### images

The images that are loaded on the website. This is to test how the TCP variables change depending on what is loaded.

### js

The js folder contains stats.js which changes the text on page3.html to the variables of TCP connection. It also sets the color which shows if the connection is detected to be a proxy or not.

### databaseTest.csv

This is the beginning of our database for known fingerprints.

### HTML pages

These pages include a form that sends the data to the nginx logs to be analyzed such as ISP, OS, and location. The html also includes redirects, cookies, images, and all of the TCP information and other relevant information collected by Nginx. The last page displays this information so the user can see what their TCP connection information is.