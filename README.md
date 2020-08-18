<center> <h1>AirBnB clone - Deploy static</h1> </center>

This project focuses on deploying your `web_static` work using `Fabric`.

---

<center><h3>Repository Contents by Project Task</h3> </center>

| Tasks | Files | Description |
| ----- | ----- | ------ |
| 0: Prepare your web servers | [0-setup_web_static.sh](https://github.com/corbinenterline1/AirBnB_clone_v2/0-setup_web_static.sh) | Bash script that sets up web servers for deployment of `web_static`. |
| 1: Compress before sending | [1-pack_web_static.py](https://github.com/corbinenterline1/AirBnB_clone_v2/1-pack_web_static.py) | Fabric script that generates a .tgz archive from the contents of the `web_static` folder, using function `do_pack`. |
| 2. Deploy archive! | [2-do_deploy_web_static.py](https://github.com/corbinenterline1/AirBnB_clone_v2/2-do_deploy_web_static.py) | Fabric script that distributes an archive to your web servers, using the function `do_deploy`. |
| 3. Full deployment | [3-deploy_web_static.py](https://github.com/corbinenterline1/AirBnB_clone_v2/3-deploy_web_static.py) | Fabric script that creates & distrubtes an archive to your web servers, using the function `deploy`. |
| 4. Keep it clean! | [100-clean_web_static.py](https://github.com/corbinenterline1/AirBnB_clone_v2/100-clean_web_static.py) | **ADVANCED** Fabric script that deletes out-of-date archives, using the function `do_clean`. |
| 5. Puppet for setup | [101-setup_web_static.pp](https://github.com/corbinenterline1/AirBnB_clone_v2/101-setup_web_static.pp) | **ADVANCED** Task #0 using Puppet! |
<br>
<br>
<center> <h2>Lessons Learned</h2> </center>
<ul>
  <li>What is Fabric</li>
  <li>How to deploy code to a server easily</li>
  <li>What is a `tgz` archive</li>
  <li>How to execute Fabric command locally</li>
  <li>How to execute Fabric command remotely</li>
  <li>How to transfer files with Fabric</li>
  <li>How to manage NGINX configuration</li>
  <li>What is the difference between `root` and `alias` in a NGINX configuration</li>
