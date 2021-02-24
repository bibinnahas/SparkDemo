import os
import sys

def set_variables():
    os.environ['access_key'] = "**"
    os.environ['secret_key'] = "**"
    os.environ['input_bucket'] = "sparkdemobucketeygds"
    os.environ['output_bucket'] = "mydemooutputbuck"

if __name__ == '__main__':
    sys.exit(set_variables())