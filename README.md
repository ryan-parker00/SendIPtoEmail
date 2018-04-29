# SendIPtoEmail
Send IP to email (For Raspberry Pi using DHCP

1. Files should be in /home/pi/code/SendIPtoEmail directory
2. You’ll need to update the file ‘myconfig.py’
                This should be self explanatory.  We can walk through it to make sure there are no questions.
3. If it didn’t come across, you’ll need to make SendIP.sh executable
                ->chmod 755 SendIP.sh
                ->Make sure the CODE_PATH is correct for your installation
4. You should be able to run things now.
                ->/home/pi/code/SendIPtoEmail/SendIP.sh

Now to make it run when the network is available:

1.	Edit SendIP.sh.service
  a. User should be the user you want to run this as.  pi is default
  b. WorkingDirectory should be the location of the files
  c. ExecStart should be the full path to SendIP.sh
2.  Copy SendIP.sh.service to /etc/systemd/system
  a.	->sudo cp SendIP.sh.service /etc/systemd/system
3.	Change ownership to root
  a.	->sudo chown root:root /etc/systemd/system/SendIP.sh.service
4.	Enable the service
  a.	->sudo systemctl enable SendIP.sh
5.	Reboot
  a. You should get an email of our Raspberry Pi's IP address on eth0.  
