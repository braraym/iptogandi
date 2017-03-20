# iptogandi
A script to update my records on Gandi's DNS. It retrieve IP adresses from the specified interfaces, not from the internet.

## Configuration
The location of the configuration file is currently hard-coded as `/etc/iptogandi.conf`.

The file can contains multiple domains/records. To add some, create a new section. The data in the `DEFAULT` section will be used when a section doesn't override it.
