from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins.functions import print_result
import os

def backup_configurations(task):
    # Send command to retrieve configuration
    command = "show running-config"
    result = task.run(task=netmiko_send_command, command_string=command)
    
    # Define directory based on site
    site_dir = f"backups/{task.host['site']}"
    os.makedirs(site_dir, exist_ok=True)
    
    # Save the configuration to a file
    config_file = os.path.join(site_dir, f"{task.host.name}_config.txt")
    with open(config_file, "w") as f:
        f.write(result.result)

def main():
    # Initialize Nornir
    nr = InitNornir(config_file="config.yaml")
    
    # Run the backup task
    result = nr.run(task=backup_configurations)
    
    # Print the result
    print_result(result)

if __name__ == "__main__":
    main()
