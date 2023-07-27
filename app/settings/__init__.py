from .base import *
from dotenv import main
import os

main.load_dotenv()

if os.environ.get('PRODUCTION') == 'True':
    from .production import *
else:
    from .development import *
