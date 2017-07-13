# logs-analysis
Reporting tool that prints out reports (in plain text) based on the data in the database

1. Open Terminal

2. Download and install the VM configuration
    - Navigate to the directory via: cd Downloads/fsnd-virtual-machine

3. Download the database
    - Download the data at this address: https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
    - Put this file into the vagrant directory, which is shared with your virtual machine

3. Start the virtual machine
    - Type ‘vagrant up’ into the command line

4. Connect to the virtual machine
    - Type ‘vagrant ssh’ into the command line

5. Once connected, find the files for running the tests
    - Type ‘cd /vagrant’ to navigate to the directory containing the files, and type ‘ls’
      to list the files in the vagrant directory.
    - Navigate to the logs_analysis folder inside the vagrant directory: type ‘cd logs_analysis’
    - Type ‘ls’ to list the files in the logs_analysis directory

6. Once logs_analysis directory files are listed, select the newsdata.py file
    - Type ‘python newsdata.py’ to execute the test file.
