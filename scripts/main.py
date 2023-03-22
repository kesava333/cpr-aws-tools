import configparser
import os

dir_name = os.path.expanduser('~/.aws')

if not os.path.exists(dir_name):
    os.makedirs(dir_name)
    
file_name = 'config'
# Create a new configparser object
config = configparser.ConfigParser()
file_path = os.path.join(dir_name, file_name)
    
config = configparser.ConfigParser()
# Add a new section to the config file for AWS SSO
config.add_section('default')

# Set the region value
config.set('default', 'region', 'us-east-2')

# Set the SSO start URL and SSO account ID values
config.set('default', 'sso_start_url', 'https://clearpathaws.awsapps.com/start')
config.set('default', 'sso_region', 'us-east-1')
config.set('default', 'sso_account_id', '444871232312')

# Set the SSO role name and AWS CLI profile name values
config.set('default', 'sso_role_name', 'AdministratorAccess')
config.set('default', 'profile', 'YOUR_AWS_CLI_PROFILE_NAME')

# Write the config to a file named 'config' in the current directory
with open(file_path, 'w') as f:
    config.write(f)
    
print(f'Config file {file_path} was created and written.')
