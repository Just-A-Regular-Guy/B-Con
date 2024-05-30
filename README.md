# B-Con

This repository contains a Python-based GUI application for establishing a VPN connection using OpenVPN. The application provides a user-friendly interface to connect and disconnect from VPN servers, monitor the connection status, and log the output of the VPN process.

## Features

- **User-friendly GUI**: Built with the `customtkinter` library.
- **VPN Connection**: Connects to VPN servers using OpenVPN.
- **Connection Status Indicator**: Displays the connection status with a colored circle.
- **Log Management**: Logs the output and error messages from the VPN process.
- **Credential Management**: Uses a credentials file for authentication.

## Requirements

- `Python 3.x`
- `customtkinter`
- `PIL` (Pillow)
- `openvpn`

## Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/your-username/vpn-connection-gui.git
   cd vpn-connection-gui
   ```

2. **Install the required Python libraries**:
   ```sh
   pip install -r requirements.txt
   ```

3. **Ensure OpenVPN is installed**:
   ```sh
   sudo apt-get install openvpn
   ```

## Usage

1. **Prepare your VPN configuration**:
   - Place your `.ovpn` configuration file in the same directory as the script.
   - Ensure you changed the `credentials.txt` file containing your VPN credentials directory.

2. **Run the application**:
   ```sh
   sudo python vpn_gui.py
   ```

3. **Using the GUI**:
   - Select the desired VPN gateway from the dropdown menu (if you didn't change the .ovpn file name with Lab_1 or Lab_2. Type your specific filename inside the dropdown menu).
   - Click the "Connect" button to establish a VPN connection.
   - A circle (green for connected, black for disconnected) will indicate the connection status.
   - Click the "Disconnect" button to terminate the VPN connection.

## File Structure

- `vpn_gui.py`: Main script for the VPN connection GUI.
- `credentials.txt`: File containing VPN credentials (username and password).
- `logs/`: Directory where log files are stored.
- `name.png`: Image used in the GUI.
- `logo.png`: Image used in the GUI.

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.

## License

B-Con is licensed under the MIT License. See the `LICENSE` file for more details.

B-Con is provided "as is" without any warranties or guarantees. The developers and contributors of B-Con make no representations or warranties of any kind, express or implied, regarding the tool's functionality, reliability, or suitability for any purpose.

By using B-Con, you acknowledge that you have read, understood, and agreed to the terms outlined in this LICENSE: https://github.com/Just-A-Regular-Guy/B-Con/blob/main/LICENSE . The developers and contributors of B-Con reserve the right to modify or update this LICENSE at any time.

## Acknowledgments

- [customtkinter](https://github.com/TomSchimansky/CustomTkinter)
- [Pillow](https://python-pillow.org/)
- [OpenVPN](https://openvpn.net/)
