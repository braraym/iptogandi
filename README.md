# iptogandi
A script to update my records on Gandi's DNS. It retrieve IP addresses from the specified interface, not from the internet.

When executed, the script will update the IP address used for each record specified in the configuration, or create it if it doesn't exists.


## Configuration
The location of the configuration file is currently hard-coded as `/usr/local/etc/iptogandi.conf`. The file contains your **private API key**, so it **shouldn't be readable by anyone** except the user running the script.

The file can contains multiple domains/records. To add some, create a new section. The section name (`[SECTION_NAME]`) as no importance. The data in the `DEFAULT` section will be used when a section doesn't override it.

The sample I provided update two records with the first IP address on eth0.

## Usage
Once the configuration file has been updated, you only need to execute `iptogandi.py`, manually or better: with a timer.
