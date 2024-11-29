import re
from os import getenv, environ
import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)
id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information *
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ['API_ID', "25061703"])
API_HASH = environ['API_HASH', "744a017a9c53f3ab489ea0bfa0ffce3f"]
BOT_TOKEN = environ['BOT_TOKEN']

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
PICS = (environ.get('PICS', 'https://envs.sh/5mw.jpg https://envs.sh/5mq.jpg https://envs.sh/5m0.jpg https://envs.sh/5mW.jpg https://envs.sh/GDG.jpg https://envs.sh/5mS.jpg')).split()
PRIME_LOGO = (environ.get('PRIME_LOGO', 'https://telegra.ph/file/ca18e2c794f4ea1c3135b.jpg'))

# Admins, Channels & Users *
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6899946963').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002442475857').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL',"-1002386346176")
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information *
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://lucifer00007860:wsK7LVPHAPqnyAs7@cluster0.lpsb0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = environ.get('DATABASE_NAME', "LazyDeveloper")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# LOG CHANNELS *
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', "-1002366234351"))
LAZY_GROUP_LOGS = int(environ.get('LAZY_GROUP_LOGS', 0))
REQ_CHANNEL = int(environ.get('REQ_CHANNEL'))
PRIME_MEMBERS_LOGS = int(environ.get('PRIME_MEMBERS_LOGS'))

# PREMIUM ACCESS *
lazydownloaders = [int(lazydownloaders) if id_pattern.search(lazydownloaders) else lazydownloaders for lazydownloaders in environ.get('PRIME_DOWNLOADERS', '').split()]
PRIME_USERS = (lazydownloaders) if lazydownloaders else [] # users who can get & download file without url shortner
lazy_renamers = [int(lazrenamers) if id_pattern.search(lazrenamers) else lazrenamers for lazrenamers in environ.get('LAZY_RENAMERS', '').split()]
LAZY_RENAMERS = (lazy_renamers + ADMINS) if lazy_renamers else [] #Add user id of the user in this field those who you want to be Authentic user for file renaming features
LZURL_PRIME_USERS = [int(lazyurlers) if id_pattern.search(lazyurlers) else lazyurlers for lazyurlers in environ.get('LZURL_PRIME_USERS', '5965340120').split()]

QR_CODE_IMG = environ.get('QR_CODE_IMG','https://telegra.ph/file/ca18e2c794f4ea1c3135b.jpg') #add url link of your qr code to recieve money - use telegraph bot or other source to get image
UPI_ID = environ.get('UPI_ID', 'lazydeveloper@ybl') #enter your upi id here - grab it from your online payment methods.

# Others
TUTORIAL = environ.get('TUTORIAL', 'https://t.me/real_MoviesAdda3/186') # Tutorial video link for opening shortlink website 
IS_TUTORIAL = bool(environ.get('IS_TUTORIAL', True))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'LazyDeveloper')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "False")), False)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "False")), False)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<b>Your Query: {query}</b> \n‌‌‌‌🎁Support: @LazyDeveloper 🎁\n\n🏷 Title: <a href={url}>{title}</a>\n🎭 Genres: {genres}\n📆 Year: <a href={url}/releaseinfo>{year}</a>\n🌟 Rating: <a href={url}/ratings>{rating}</a> / 10 \n\n♥️ we are nothing without you ♥️ \n\n💛 Please Share Us 💛\n\n⚠️Click on the button 👇 below to get your query privately")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), False)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "True")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "False")), False)

#LazyRenamer Configs
FLOOD = int(environ.get("FLOOD", "10"))
LAZY_MODE = bool(environ.get("LAZY_MODE")) #make it true to enable file renaming feature in bot

# Requested Content template variables --- 
ADMIN_USRNM = environ.get('ADMIN_USRNM','Nishant_0786') # WITHOUT @
MAIN_CHANNEL_USRNM = environ.get('MAIN_CHANNEL_USRNM','Ni_Movies') # WITHOUT @
DEV_CHANNEL_USRNM = environ.get('DEV_CHANNEL_USRNM','Ni_Movies') # WITHOUT @
LAZY_YT_HANDLE = environ.get('LAZY_YT_HANDLE','LayDeveloperr')  # WITHOUT @ [  add only handle - don't add full url  ] 
MOVIE_GROUP_USERNAME = environ.get('MOVIE_GROUP_USERNAME', "Ni_Movie_Request_Group") #[ without @ ]

# Url Shortner
URL_MODE = is_enabled((environ.get("URL_MODE","True")), False) # make it true to enable url shortner in groups or pm
URL_SHORTENR_WEBSITE = environ.get('URL_SHORTENR_WEBSITE', 'atglinks.com') #Always use website url from api section 
URL_SHORTNER_WEBSITE_API = environ.get('URL_SHORTNER_WEBSITE_API', '72a7f0131e5e657e37cf7e2a9e928a616b671cf5')
lazy_groups = environ.get('LAZY_GROUPS','')
LAZY_GROUPS = [int(lazy_groups) for lazy_groups in lazy_groups.split()] if lazy_groups else None # ADD GROUP ID IN THIS VARIABLE 
my_users = [int(my_users) if id_pattern.search(my_users) else my_users for my_users in environ.get('MY_USERS', '').split()]
MY_USERS = (my_users) if my_users else [] #input the id of that users who can share file in file protection mode

# Online Stream and Download
PORT = int(environ.get('PORT', 8080))
NO_PORT = bool(environ.get('NO_PORT', False))
APP_NAME = None
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = environ.get('APP_NAME')
else:
    ON_HEROKU = False
BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
URL = "https://{}/".format(FQDN) if ON_HEROKU or NO_PORT else \
    "http://{}:{}/".format(FQDN, PORT)
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
WORKERS = int(environ.get('WORKERS', '4'))
SESSION_NAME = str(environ.get('SESSION_NAME', 'LazyBot'))
MULTI_CLIENT = False
name = str(environ.get('name', 'LazyPrincess'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = str(getenv('APP_NAME'))

else:
    ON_HEROKU = False
HAS_SSL=bool(getenv('HAS_SSL',False))
if HAS_SSL:
    URL = "https://{}/".format(FQDN)
else:
    URL = "http://{}/".format(FQDN)
BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "")).split())) 
OWNER_USERNAME = "Nishant_0786"

lazydownloaders = [int(lazydownloaders) if id_pattern.search(lazydownloaders) else lazydownloaders for lazydownloaders in environ.get('PRIME_DOWNLOADERS', '').split()]
PRIME_DOWNLOADERS = (lazydownloaders) if lazydownloaders else []

# URL UPLOADING
BANNED_USERS = set(int(x) for x in environ.get("BANNED_USERS", "").split())
DOWNLOAD_LOCATION = "./DOWNLOADS"
MAX_FILE_SIZE = 4194304000
TG_MAX_FILE_SIZE = 4194304000
FREE_USER_MAX_FILE_SIZE = 4194304000
CHUNK_SIZE = int(environ.get("CHUNK_SIZE", 128))
HTTP_PROXY = environ.get("HTTP_PROXY", "")
OUO_IO_API_KEY = ""
MAX_MESSAGE_LENGTH = 4096
PROCESS_MAX_TIMEOUT = 0
DEF_WATER_MARK_FILE = ""
LOGGER = logging

# Adding Language Feature : 
LANGUAGES = ["hindi", "hin", "english", "eng", "korean", "kor", "urdu", "urd","chinese","chin","tamil", "tam", "malayalam", "mal",  "telugu", "tel", "kannada", "kan"]
SEASONS = ["season 1" , "season 2" , "season 3" , "season 4", "season 5" , "season 6" , "season 7" , "season 8" , "season 9" , "season 10"]
QUALITIES = ["360P", "", "480P", "", "720P", "", "1080P", "", "1440P", "", "2160P", ""]

MAX_B_TN = environ.get("MAX_B_TN", "10")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)


# Auto Delete For Group Message (Self Delete) #
SELF_DELETE_SECONDS = int(environ.get('SELF_DELETE_SECONDS', 300))
SELF_DELETE = environ.get('SELF_DELETE', True)
if SELF_DELETE == "True":
    SELF_DELETE = True

DISCUSSION_TITLE = "Click Here"
DISCUSSION_CHAT_USRNM = "Discusss_Here" #without @

# Download Tutorial Button #
DOWNLOAD_TEXT_NAME = "📥 HOW TO DOWNLOAD 📥"
DOWNLOAD_TEXT_URL = "https://t.me/real_MoviesAdda3"

# Custom Caption Under Button #
CAPTION_BUTTON = "Get Updates"
CAPTION_BUTTON_URL = "https://t.me/real_MoviesAdda3"

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
# Credit @LazyDeveloper.
# Please Don't remove credit.
# Born to make history @LazyDeveloper !
# Thank you LazyDeveloper for helping us in this Journey
# 🥰  Thank you for giving me credit @LazyDeveloperr  🥰
# for any error please contact me -> telegram@LazyDeveloperr or insta @LazyDeveloperr 
# rip paid developers 🤣 - >> No need to buy paid source code while @LazyDeveloperr is here 😍😍
