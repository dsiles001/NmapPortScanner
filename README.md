# NmapPortScanner

It's the same idea as the previous port scanner in terms of the input, which stays the same. The user will enter the domain of the target they want to scan. They will after be prompted to enter the port(s) they want to scan. If there is more than one port, the user will enter the port numbers with commas between each number (ex: 20,21,80,443). If no ports are entered, the scanner will scan ports 21-1024 by default.

The output will look slightly different now. Ports are grouped under the protocol they use (ex. TCP). The status of the port will also be shown, displaying whether or not the port is open.
