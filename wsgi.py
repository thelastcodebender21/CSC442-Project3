import sys
import os

# Add the BioSeqAligner directory to Python path
project_root = os.path.dirname(os.path.abspath(__file__))
bioaligner_path = os.path.join(project_root, 'BioSeqAligner')
sys.path.insert(0, bioaligner_path)

# Now import the app
try:
    from backend.app import app
except ImportError as e:
    print(f"Import error: {e}")
    print(f"Python path: {sys.path}")
    raise

if __name__ == '__main__':
    app.run()
