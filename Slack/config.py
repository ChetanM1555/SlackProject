import subprocess
def install_simple_term():
    #installs simple_term
    try:
        subprocess.check_call(['pip', 'install', 'simple-term'])
        print("simple-term package installed successfully.")
    except subprocess.CalledProcessError:
        print("Failed to install simple-term package.")

def install_slack_sdk():
    # installs Slack    
    try:
        subprocess.check_call(['pip', 'install', 'slack-sdk'])
        print("slack-sdk package installed successfully.")
    except subprocess.CalledProcessError:
        print("Failed to install slack-sdk package.")



