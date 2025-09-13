# Cyber Station
import subprocess
import re
import platform


def get_wifi_profiles():
    """
    Retrieves all saved WiFi profiles on the system based on the platform.
    """
    system = platform.system()
    
    if system == 'Windows':
        try:
            # Fetch the output of 'netsh wlan show profiles'
            data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'], stderr=subprocess.DEVNULL).decode('utf-8')
            # Extract WiFi profile names
            profiles = [line.split(":")[1].strip() for line in data.split('\n') if "All User Profile" in line]
            return profiles
        
        except subprocess.CalledProcessError:
            print("Error: Failed to retrieve WiFi profiles. Make sure you're running as Administrator.")
            return []
    
    elif system == 'Linux':
        try:
            # Fetch the list of saved WiFi profiles
            data = subprocess.check_output(['nmcli', 'device', 'wifi', 'list'], stderr=subprocess.DEVNULL).decode('utf-8')
            # Extract WiFi profile names
            profiles = re.findall(r'\*?\s*(\S+)\s+\S+\s+\S+', data)  # Extract SSID names
            return profiles
        except subprocess.CalledProcessError:
            print("Error: Failed to retrieve WiFi profiles.")
            return []
    
    else:
        print("Error: Unsupported platform.")
        return []


def get_wifi_password(profile):
    """
    Retrieves the password of a specific WiFi profile based on the platform.
    """
    system = platform.system()
    
    if system == 'Windows':
        try:
            # Fetch the details of the specific profile
            data = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear'], stderr=subprocess.DEVNULL).decode('utf-8')
            # Extract the password if it exists
            password_lines = [line.split(":")[1].strip() for line in data.split('\n') if "Key Content" in line]
            return password_lines[0] if password_lines else None
        except subprocess.CalledProcessError:
            return None
    
    elif system == 'Linux':
        try:
            # Fetch the details of the specific profile
            data = subprocess.check_output(['sudo', 'cat', f'/etc/NetworkManager/system-connections/{profile}'], stderr=subprocess.DEVNULL).decode('utf-8')
            # Extract the password if it exists
            match = re.search(r'psk=(\S+)', data)  # Search for the 'psk' (pre-shared key)
            return match.group(1) if match else None
        except subprocess.CalledProcessError:
            return None
        except FileNotFoundError:
            print(f"Error: Profile {profile} not found.")
            return None
    
    else:
        return None


def main():
    print("{:<30}|  {:<}".format("WiFi Network", "Password"))
    print("-" * 50)
    
    # Get all WiFi profiles based on the platform
    profiles = get_wifi_profiles()
    if not profiles:
        print("No WiFi profiles found.")
        return
    
    # Retrieve and display passwords for each profile
    for profile in profiles:
        password = get_wifi_password(profile)
        print("{:<30}|  {:<}".format(profile, password if password else "No password found"))

    # Pause the script to allow the user to view the output
    input("\nPress Enter to exit...")


if __name__ == "__main__":
    main()
