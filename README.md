
# Simple Network Scanner

This Python script allows you to scan a network for active devices using ARP requests. It's a simple yet effective tool for network administrators and security enthusiasts to discover hosts on a local network.

## Features

- Scans a specified IP range to discover active hosts
- Displays the IP addresses and MAC addresses of discovered devices
- Easy-to-use command-line interface

## Prerequisites

- Python 3.x installed
- Scapy library installed (`pip install scapy`)

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/ngirimba/simple-network-scanner.git
    ```

2. Navigate to the project directory:

    ```bash
    cd simple-network-scanner
    ```

3. Run the network scanner:

    ```bash
    python network_scanner.py
    ```

4. Enter the IP range you want to scan when prompted.

5. View the results displayed on the terminal.

## Example

```bash
$ python network_scanner.py
Enter the IP range to be scanned (e.g., 192.168.1.0/24): 192.168.1.0/24

Scanning...

IP Address       MAC Address
---------------------------------
192.168.1.1      00:11:22:33:44:55
192.168.1.2      00:aa:bb:cc:dd:ee
...
```

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

Moses Mwambura

---

