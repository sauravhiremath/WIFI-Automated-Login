# WIFI Automated Login
## Currently for VIT, Vellore WIFIs only

## How to add your Username and Password
<p>Replace the "username" and "password" in the login.py module with your own Username and Password.</p>

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
  <li>Connect to any VIT Wifi.
  <li>Double click the batch file (.bat extension).
  <li>Thats all, sit back and relax :p
</p>
<br>
For automated triggering of Wifi Login, use TaskScheduler.exe (For Windows)

## Additional Notes

## Debugging

<p>There is another module for checking if Net is Working or not. </p>

## Contribution

<p> Feel free to contribute. :D </p>
