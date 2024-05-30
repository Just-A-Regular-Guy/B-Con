# Import required libraries
import os
import customtkinter
from PIL import Image
import subprocess
import threading
import datetime

# Get the current working directory
current_directory = os.getcwd()

# Initialize variables to store the VPN process and gateway
vpn_process = None
button = True
gateway = None

# Define a threading event to signal termination
terminate_event = threading.Event()

# Function to update the circle color based on the connection status
def set_connected(connected):
    if connected:
        # Set the circle color to green when connected
        circle.configure(fg_color="#5BBA6F")
    else:
        # Set the circle color to black when disconnected
        circle.configure(fg_color="#1a1a1a")

# Function to establish a VPN connection
def connect():
    global vpn_process
    global gateway
    print("Entering connect function")
    # Get the selected gateway from the input field
    gateway = entry_gateway.get()
    print(f"Selected gateway: {gateway}")
    # Construct the OpenVPN command with the selected gateway and credentials
    command = f'sudo openvpn --auth-nocache --config {gateway}.ovpn --auth-user-pass credentials.txt'
    print(f"Command: {command}")
    try:
        print("Running sudo command...")
        # Run the OpenVPN command using subprocess
        vpn_process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # Start a new thread to read the output and error messages
        threading.Thread(target=read_output, args=(vpn_process.stdout, vpn_process.stderr, terminate_event)).start()
        print("sudo command completed.")
    except Exception as e:
        print(f"Error: {e}")
    print(f"Connected to {gateway}")

# Function to read output and error messages from the OpenVPN process
def read_output(stdout, stderr, terminate_event):
    while not terminate_event.is_set():
        global gateway
        # Read output and error messages from the OpenVPN process
        output = stdout.read()
        error = stderr.read()
        print(f"Output: {output.decode()}")
        print(f"Error: {error.decode()}")
        # Create the logs directory if it does not exist
        log_directory = os.path.join(current_directory, 'logs')
        os.makedirs(log_directory, exist_ok=True)
        # Create a log file with the current date and time
        now = datetime.datetime.now()
        log_filename = f"{gateway}-{now.strftime('%d:%m:%y_%H:%M')}.txt"
        with open(os.path.join(log_directory, log_filename), "w") as f:
            f.write(output.decode())
            f.write(error.decode())

# Function to disconnect from the VPN
def disconnect():
    global vpn_process
    global terminate_event
    if vpn_process:
        # Set the termination event to signal the thread to stop
        terminate_event.set()  
        try:
            # Forcefully kill the OpenVPN process
            subprocess.run(["sudo", "pkill", "-9", "openvpn"])  
        except subprocess.CalledProcessError:
            # Ignore the exception
            pass  
        print("Disconnected from VPN")
        vpn_process = None
    else:
        print("No active VPN connection to disconnect")

# Function to toggle the connect/disconnect button
def button_trigger():
    global connect_button
    global button
    if button == True:
        connect_button.configure(text='Disconnect')
        button = False
        connect()
        # Set the circle to green
        set_connected(True)  
    elif button == False:
        connect_button.configure(text='Connect')
        button = True
        disconnect()
        # Set the circle to black
        set_connected(False)  
    else:
        print("Error in button_trigger function")

# Function to position the window
def position_window():
    # Set the window size
    width = 200
    height = 300

    # Get the monitor size
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Set the margin in pixels
    margin = 0

    # Calculate the window position
    x = screen_width + 100
    y = screen_height - height - margin
    
    # Set the window size and position
    root.geometry(f"{width}x{height}+{x}+{y}")
    
# Set GUI global settings
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

# Create the main window
root = customtkinter.CTk()
root.geometry("200x300")

# Set the window title and make it non-resizable
root.title('')
root.resizable(width=False, height=False)
# Call the position_window function after 100 milliseconds
root.after(100, position_window)

# Create top frame
top_frame = customtkinter.CTkFrame(root, fg_color='#af0000', bg_color='#af0000', height=55, width=200, corner_radius=0)
top_frame.pack(side=customtkinter.TOP)

# Load the image using PIL
name_image = Image.open("name.png")

# Create a CTkImage object
ctk_image = customtkinter.CTkImage(light_image=name_image, dark_image=name_image, size=(170, 55))

# Create a label and set the image
name_label = customtkinter.CTkLabel(top_frame, image=ctk_image, text="")
name_label.pack(side=customtkinter.LEFT)

# Create a spacer to add spacing between components
spacer_1 = customtkinter.CTkFrame(top_frame, width=10, height=10, corner_radius=10, bg_color="#af0000", fg_color="#af0000")
spacer_1.pack(side=customtkinter.RIGHT)

# Create the circle indicator
circle = customtkinter.CTkFrame(top_frame, width=12, height=12, corner_radius=10, bg_color="#af0000", fg_color="#1a1a1a", border_width=0, border_color='black')
circle.pack(side=customtkinter.RIGHT)

# Create another spacer
spacer_2 = customtkinter.CTkFrame(top_frame, width=10, height=10, corner_radius=10, bg_color="#af0000", fg_color="#af0000")
spacer_2.pack(side=customtkinter.RIGHT)

# Load the logo image using PIL
image = Image.open("logo.png")

# Create a CTkImage object
ctk_image = customtkinter.CTkImage(light_image=image, dark_image=image, size=(200, 145))

# Create a label and set the image
image_label = customtkinter.CTkLabel(root, image=ctk_image, text="")
image_label.pack(anchor='n')

# Create gateway input field
entry_gateway = customtkinter.CTkComboBox(root, width=165, height=28, fg_color='#404040', border_color='#818181', border_width=1, values= ['Lab_1', 'Lab_2'])
entry_gateway.place(relx=0.1, rely=0.675)
 
# Create connect button
connect_button = customtkinter.CTkButton(root, width=165, height=40, text='Connect', fg_color='#af0000', bg_color='#212121', font=customtkinter.CTkFont(weight='bold'), command=button_trigger)
connect_button.place(rely=0.8, relx=0.1)

# Start the main event loop
root.mainloop()
