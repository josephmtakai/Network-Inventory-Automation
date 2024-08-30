# Network Inventory Automation

This project provides an automated solution for retrieving and documenting network device configurations using Python and Nornir. The script connects to specified network devices, executes commands to retrieve the running configuration, and saves the output in a well-organized directory structure.

## Features

- **Automated Configuration Backup:** Automatically retrieve and save running configurations from network devices.
- **Organized Storage:** Configurations are saved in a directory structure organized by site and device name.
- **Scalability:** Easily add more devices to the inventory by updating the YAML configuration files.
- **Extensibility:** The script can be extended to include additional tasks such as configuration comparisons, compliance checks, and more.

## Project Structure

```plaintext
Network Inventory Automation/
│
├── backup_configs.py        # Main Python script for automating backups
├── config.yaml              # Nornir configuration file
├── hosts.yaml               # Inventory of network devices
├── groups.yaml              # Group settings and credentials
└── backups/                 # Directory where configurations are saved

Requirements
Python 3.x
Required Python packages: nornir, nornir_netmiko, nornir_utils

To install the required packages, run:
pip install nornir nornir_netmiko nornir_utils

Setup
Clone the Repository:
git clone https://github.com/yourusername/network-inventory-automation.git
cd network-inventory-automation

Configure the Inventory:

Edit the hosts.yaml file to include your network devices.
Edit the groups.yaml file to set your credentials and connection options.

Example hosts.yaml
---
rtr1:
  hostname: "192.168.1.1"
  groups:
    - cisco
  data:
    role: "router"
    site: "HQ"

Example groups.yaml:
---
cisco:
  platform: "ios"
  username: "your_username"
  password: "your_password"
  connection_options:
    netmiko:
      extras:
        secret: "your_enable_password"
        global_delay_factor: 2


Run the Script:

Execute the script to start the configuration backup process:
python backup_configs.py

Output
The configurations are saved in the backups directory, organized by site and device name:
backups/
├── HQ/
│   └── rtr1_config.txt
└── Branch1/
    └── rtr2_config.txt

Future Enhancements
Configuration Comparison: Compare current and previous configurations to detect changes.
Compliance Checks: Validate configurations against predefined standards.
Notification System: Integrate with messaging platforms (e.g., Slack, Email) to notify about backups and issues.
Contributing
Contributions are welcome! Feel free to fork this repository, make your changes, and submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Happy automating!

### Key Sections in the README:
- **Introduction:** Explains the purpose of the project.
- **Features:** Highlights key capabilities of the script.
- **Project Structure:** Provides an overview of the directory and file organization.
- **Requirements:** Lists the Python version and packages needed.
- **Setup:** Detailed steps for setting up the project, including cloning the repository, configuring the inventory, and running the script.
- **Output:** Describes how and where the output (configurations) will be saved.
- **Future Enhancements:** Suggestions for extending the project.
- **Contributing:** Encourages contributions and collaboration.
- **License:** Indicates the licensing for the project.

This README provides clear and detailed information to help users understand, set up, and contribute to your project.

