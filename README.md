
# WIFI Automated Login

## Currently for VIT, Vellore WIFIs only

## How to Use
<p>Replace the "username" and "password" in the <b>login.py</b> module with your own Username and Password.</p>
<p>Also change the default directory for chromedriver to Wifi Automated Login repository location on your PC</p>

## Examples
<font color="#487799"><i><p>Original</p></i></font>

```sh
8 driver.find_element_by_name("userId").send_keys("username")
9 driver.find_element_by_name("password").send_keys("password")
.
.
.
26 driver = webdriver.Chrome('C:/[repodirectory]/chromedriver.exe')
        
```

<font color="#487799"><i><p>After changes</p></i></font>

```sh
8 driver.find_element_by_name("userId").send_keys("18BCI00xx")
9 driver.find_element_by_name("password").send_keys("abcd1234")
.
.
.
26 driver = webdriver.Chrome('C:/Users/Foo/Downloads/WiFi-Automated-Login/chromedriver.exe')
        
```
## Requirements
--Python 3.7: https://www.python.org/downloads/ <br>
--Python<br>
--Selenium Driver for Chrome<br>

## How to Use
<p><ul>
  <li>Download the repo to your local system
    <a href="https://ibb.co/bUjj6L"><img src="https://preview.ibb.co/d92FD0/ddddddddddddd.jpg" alt="ddddddddddddd" border="0"></a>
  <li>Extract the zip file in some directory.
  <li>Change username, password and chromedriver path in login.py (See the reference above)
  <li>Install the Requirements.txt file using python.
  <li>Connect to any VIT Wifi.
  <li>Double click the batch file (.bat extension).
  <li>Thats all, sit back and relax :p
  </ul></p>
<p>For automated triggering of Wifi Login, use TaskScheduler.exe (For Windows)</p>

## Debugging
<p>There is another module for checking if Net is Working or not. </p>

## Troubleshooting 
1. <p>Selenium Package may not be installed. This can be done by</p>

     ```sh
     python -m pip install selenium
     ```
     <p>If this gives you an error, proceed to Step 2.</p>
 2. <p>Check if <b>pip</b> is added to PATH environment variables with</p>
     
     ```sh
     echo %PATH%
     ```
  
     <p>You should see something similar to C:\Python37-32\Scripts listed among all directories.</p>
     <p>If not, add it using</p>
     
     ```sh
     setx PATH "%PATH%;C:\Python37-32\Scripts"
     ```
     <p>or alternatively, use the Control Panel</p>
     
     
## Contribution
<p> Feel free to contribute. :D </p>
