# Captive-Portal-Auto-Login
A small python script to automatically login to the captive portal in the NITK's intranet.


## Pre-Requisites:
Selenium Webdriver library for Python  
geckodriver for Firefox (support for Chrome coming soon)

## Usage:
```
 $ git clone /https://github.com/samvid25/Captive-Portal-Auto-Login.git
 $ cd Captive-Portal-Auto-Login
 $ gedit login.py
```
Replace "staff" with your username and password:
Save and exit.

Replace /path/to/login.py with the path of login.py in your PC:
```
 $ gedit login
```
Save and exit.

Make the 'login' shell script executable:
```
 $ chmod +x login
```

Now whenever you want to log-on, use `./login` to automatically log-on.
If you want to add the script to your path:
```
 $ sudo cp login /usr/local/bin
```




