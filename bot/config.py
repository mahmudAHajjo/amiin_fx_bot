from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
VIP_CHANNEL_ID = int(os.getenv('VIP_CHANNEL_ID'))
TRC20_ADDRESS = os.getenv('TRC20_ADDRESS')

# More robust ADMIN_IDS handling
admin_ids_str = os.getenv('ADMIN_IDS', '')
try:
    # Remove any comments and split by commas
    clean_ids = [id.split('#')[0].strip() for id in admin_ids_str.split(',')]
    ADMIN_IDS = [int(id) for id in clean_ids if id]
except ValueError as e:
    print(f"Error parsing ADMIN_IDS: {e}")
    ADMIN_IDS = []

SUPPORT_EMAIL = 'mohamedamiin1301@gmail.com'
SUPPORT_TELEGRAM = '@amiin_fx10'
PAYMENTS_CONTACT = '@AmiinFXpayments'