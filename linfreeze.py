#!/usr/bin/python
# -*- coding: utf-8 -*-

import getpass
import os
import shutil
import sys

print "Checking your user privileges"
if getpass.getuser() == "root":
    pass
else:
    "You are not root. Please rerun with sudo privileges."
    sys.exit()
print "LinFreeze console user interface"
option1 = "1) Setup"
option2 = "2) Remove"
option3 = "3) About"
print option1
print option2
print option3
chosen_option = raw_input("Enter option: ")
if chosen_option == "1":
    print "LinFreeze installation"
    print "This script will set up and configure LinFreeze"
    username = raw_input("Username to be frozen ")
    print "Checking your username..."
    import os

    home_list = os.listdir("/home")
    if username in home_list:
        pass
    else:
        print "Entered username is incorrect"
        sys.exit()
    print "Verification successful"
    answer = raw_input("Do you want to continue? (y/n): ")
    if answer == "n":
        print "Exiting..."
        sys.exit()
    else:
        print "Resuming..."
    print "Saving your configuration..."
    os.system("cp -R /home/%s/ /root" % username)
    print "Giving right permissions to the saved folder..."
    os.system("chown -R %s:%s /root/%s" % (username, username, username))
    print "Saving configuration to LinFreeze configuration folder..."
    os.mkdir("/usr/share/linfreeze")
    shutil.copy("/etc/conf.d/local.start", "/usr/share/linfreeze")
    opened_file = open("/etc/conf.d/local.start", "a")
    opened_file.write("rsync –del -av /root/%s/ /home/%s/" % (username, username))
    print "Process completed"
    isl = raw_input("Do you want to reboot? (y/b): ")
    if isl == "y":
        print "REBOOTING"
        os.system("reboot")
    else:
        print "Exiting"
        sys.exit()
if chosen_option == "2":
    print "LinFreeze removing system"
    answer = raw_input("Do you want to continue? (y/n): ")
    if answer == "n":
        print "Exiting"
        sys.exit()
    else:
        pass
    print "Dropping old configuration"
    os.remove("/etc/conf.d/local.start")
    print "Copying backed configuration"
    shutil.copy("/usr/share/linfreeze/local.start", "/etc/conf.d/")
    print "Process completed"
    print "Exiting..."
if chosen_option == "3":
    print """
LinFreeze freezing application
Version 1.0
The interface is not ready yet
This program has GNU/GPLv2 license
Thank you
@fortran
@YVZ_61
Translated by Camilo Sampedro <camilo.sampedro@udea.edu.co> @camilosampedro
  """
    sys.exit()
else:
    print "Unrecognized option, please try again and select one"
    sys.exit()
