# Sample Linux Commands

## User Management

* `sudo su -`: Change to root user.
* `su - user_name`: Switch to a specific user.
* `useradd -m -p password -d /home/user_name user_name`: Add a new user in Linux.
* `usermod -aG sudo user_name`: Grant sudo privileges to a user.
* `userdel user_name`: Delete a user.
* `sudo passwd user_name`: Reset a user's password.
* `sudo userdel -r username`: Delete user account along with home directory and files.
* `sudo passwd -l username`: Lock user account.
* `sudo deluser USER GROUPNAME`: Remove user from group.

## File Operations

* `ls`: List files in current directory.
* `ls -l`: List files and directories in long format.
* `chmod u+rwx sample.txt`: Change file permissions.
* `chown user_name sample.txt`: Change file owner.
* `chgrp user_name sample.txt`: Change file group owner.
* `umask 022`: Set default permissions.
* `cd /home/user_name/wFolder`: Navigate to a directory.
* `pwd`: Print current directory.
* `mkdir newFolder`: Create a new folder.
* `touch sample.txt`: Create a file.
* `rm sample.txt`: Delete a file.
* `rm -r my_directory`: Delete a directory and its contents.
* `rm -f file.txt`: Forcefully delete a file.
* `cp -r directory destination`: Copy a directory and its contents.
* `cp file.txt destination`: Copy a file.
* `mv file.txt new_name.txt`: Rename a file.
* `mv file.txt directory`: Move a file.
* `cat file.txt`: Display file contents.

## SSH and Networking

* `ssh -i filename username@IpAddress`: Connect to a Debian instance.
* `ssh user@hostname`: Initiate an SSH connection.
* `who`: Show logged-in users.
* `finger`: Display user information.
* `finger username`: Provide user details.

## Navigation

* `Ctrl + A`: Move to beginning of line.
* `Ctrl + E`: Move to end of line.
* `Ctrl + B`: Move back one character.
* `Ctrl + F`: Move forward one character.
* `Alt + B`: Move back one word.
* `Alt + F`: Move forward one word.

## Editing

* `Ctrl + U`: Cut/delete from cursor to beginning of line.
* `Ctrl + K`: Cut/delete from cursor to end of line.
* `Ctrl + W`: Cut/delete word before cursor.
* `Ctrl + Y`: Paste last cut text.
* `Ctrl + L`: Clear screen.

## History

* `Ctrl + R`: Search command history (reverse search).
* `Ctrl + G`: Escape from history search mode.
* `Ctrl + P`: Go to previous command.
* `Ctrl + N`: Go to next command.
* `Ctrl + C`: Terminate current command.
