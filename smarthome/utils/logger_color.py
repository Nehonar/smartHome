import colorama
import logging
logging.basicConfig(level=logging.INFO)

def print_data(data):
    logging.info(colorama.Fore.BLUE + str(data) + colorama.Style.RESET_ALL)    