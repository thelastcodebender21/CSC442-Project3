import sys
import os

# Get absolute paths
root_dir = os.path.abspath(os.path.dirname(__file__))
bioaligner_dir = os.path.join(root_dir, 'BioSeqAligner')

# Add BioSeqAligner to path
sys.path.insert(0, bioaligner_dir)

# Import the Flask app from backend
from backend.app import app

if __name__ == '__main__':
    app.run()
