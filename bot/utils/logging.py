import logging
from pathlib import Path

def setup_logging():
    """Set up logging configuration"""
    logs_dir = Path(__file__).parent.parent.parent / 'logs'
    logs_dir.mkdir(exist_ok=True)
    
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        filename=str(logs_dir / 'bot.log'),
        filemode='a'
    )