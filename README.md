# WIFI Automated Login
## Currently for VIT, Vellore WIFIs only
## Requires selenium package for Python

## How to add your Username and Password
<p>Replace the "username" and "password" in the <b>login.py</b> module with your own Username and Password.</p>

## Examples
<font color="#487799"><i><p>Original</p></i></font>

```sh
driver.find_element_by_name("userId").send_keys("username")
driver.find_element_by_name("password").send_keys("password")
```

<font color="#487799"><i><p>After changes</p></i></font>

```sh
driver.find_element_by_name("userId").send_keys("18BCI00xx")
driver.find_element_by_name("password").send_keys("abcd1234")
```

## How to Use
<p><ul>
  <li>Download the repo to your local system
    <a href="https://ibb.co/bUjj6L"><img src="https://preview.ibb.co/d92FD0/ddddddddddddd.jpg" alt="ddddddddddddd" border="0"></a>
  <li>Extract the zip file in some directory.
  <li>Change username and password in login.py (See the reference above)
  <li>Connect to any VIT Wifi.
  <li>Double click the batch file (.bat extension).
  <li>Thats all, sit back and relax :p
  </ul>
For automated triggering of Wifi Login, use TaskScheduler.exe (For Windows)
</p>

## Debugging
<p>There is another module for checking if Net is Working or not. </p>

## Contribution
<p> Feel free to contribute. :D </p>
