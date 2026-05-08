import sys
import os

# Get absolute paths
root_dir = os.path.abspath(os.path.dirname(__file__))
bioaligner_dir = os.path.join(root_dir, 'BioSeqAligner')
backend_dir = os.path.join(bioaligner_dir, 'backend')

# Add both directories to path
sys.path.insert(0, bioaligner_dir)
sys.path.insert(0, backend_dir)

# Import the Flask app
from app import app

if __name__ == '__main__':
    app.run()
