###################################################
#  P2B Exchange Bot Created by Cryptominer8245    #
#       Marker Maker, WashTrade & Info Bot        #
#                Created 3-09-2023                #
###################################################
import requests
import json
import time
import datetime
import random
import os
import termcolor
import hmac
import hashlib
import base64
from prettytable import PrettyTable
from termcolor import colored
from dotenv import load_dotenv
os.system('clear')
while True:
    load_dotenv()

    api_key = os.getenv("api_key")
    secret_key = os.getenv("secret_key")
#############################################################
# Get current date and time
    now = datetime.datetime.now()
    date_string = now.strftime("%B %d %Y")
    time_string = now.strftime("%I:%M:%S %p")
##################_COIN_SETUP_###############################
    symbol = os.getenv("symbol")
    base = os.getenv("base")
    pair = f"{symbol}_{base}"
    market = f"{symbol}/{base}"
    markets = f"{symbol}-{base}"
    url_base = "https://api.p2pb2b.com"
##########_Server_Time__##########
    def get_server_time():
        print(colored("   P2B Exchange Bot Loading   \n", "light_magenta"))
        print(colored(f"Current Time Stamp: {date_string} {time_string}", "yellow"))
    get_server_time()
    print("\n")
    time.sleep(1)
###########_HEADERS_##############
#############################################################
# To get The rest of the working Code you must contact me  
# for Purchasing it - Thank you
