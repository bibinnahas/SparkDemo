import os
import sys

def set_variables():
    os.environ['access_key'] = "AKIA6OOXLL752YGB2675"
    os.environ['secret_key'] = "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"
    os.environ['input_bucket'] = "sparkdemobucketeygds"
    os.environ['output_bucket'] = "mydemooutputbuck"

if __name__ == '__main__':
    sys.exit(set_variables())