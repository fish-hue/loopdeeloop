```markdown
# loopdeeloop

The **IP Ping Sweep Tool** is a Python script designed to ping a range of IP addresses or a single IP/domain to check for connectivity. It can be used to swiftly determine which devices on a network are active and responding.

## Features

- Pings a range of IP addresses to see which hosts are online.
- Supports both IPv4 addresses and domain names.
- Provides feedback on the status of each IP address (alive or not).
- OS-compatible with checks for Windows and non-Windows operating systems.

## Requirements

- Python 3.x
- Active Internet connection (for domain names)
- Access to a command line/terminal

## Installation

1. **Clone the repository** or create a new Python file on your local machine:

   ```bash
   git clone https://github.com/fish-hue/loopdeeloop.git
   ```

   2. **Ensure you have Python 3.x installed** on your system.

## Usage

1. Open a command prompt (or terminal).
2. Navigate to the directory where `loopdeeloop.py` is located.
3. Run the script:

   ```bash
   python loopdeeloop.py
   ```

4. Enter the start IP address or domain when prompted (e.g., `192.168.1.100` or `google.com`).
5. Enter the end IP address if you are pinging a range, or leave it blank to ping the single start IP.

## Example

```plaintext
Enter the start IP address or domain (e.g., 192.168.1.100 or google.com): 192.168.1.100
Enter the end IP address (only for IP ranges, or leave blank for single address): 192.168.1.110
ITS ALIVE! 192.168.1.100
NOBODY WILL ANSWER THE DOOR! :( 192.168.1.101
ITS ALIVE! 192.168.1.102
NOBODY WILL ANSWER THE DOOR! :( 192.168.1.103
...
```

## Code Overview

Here's a brief breakdown of how the script works:

- The script uses **subprocess** to execute ping commands based on the OS.
- The `ping_sweep` function handles both single IP addresses and ranges.
- It checks if provided addresses are valid IPs before trying to ping them.
- Connectivity status is indicated with friendly messages: "ITS ALIVE!" for reachable IPs and "NOBODY WILL ANSWER THE DOOR!" for unreachable ones.

## Notes

- This script may require administrative privileges to run certain commands in some operating systems.
- The ping utility might behave differently across various platforms, so results may vary depending on the OS you're using.
- Ensure proper network permissions when pinging devices on a network.

```
