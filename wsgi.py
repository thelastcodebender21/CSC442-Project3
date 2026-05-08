import sys
import os

# Add BioSeqAligner to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'BioSeqAligner'))

# Import the Flask app
from backend.app import app

if __name__ == '__main__':
    app.run()
