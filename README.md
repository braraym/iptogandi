# iptogandi
A script to update my records on Gandi's DNS. It retrieve IP adresses from the specified interfaces, not from the internet.

When executed, the script will retrieve from Gandi the IP address used for each record specified in the configuration. It will then compare it with the current address, and update the record and zone if it doesn't match.


## Configuration
The location of the configuration file is currently hard-coded as `/etc/iptogandi.conf`. The file contains your **private API key**, so it **shouldn't be readable by anyone** except the user running the script.

The file can contains multiple domains/records. To add some, create a new section. The section name as no importance. The data in the `DEFAULT` section will be used when a section doesn't override it.

The sample I provided update two records with the first IP adress on eth0.

## Usage
Once the configuration file has been updated, you only need to execute `iptogandi.py`, manually or better: with a timer.
