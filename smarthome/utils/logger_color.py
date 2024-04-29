import colorama
import logging
logging.basicConfig(level=logging.INFO)

def print_info(info):
    logging.info(colorama.Fore.BLUE + str(info) + colorama.Style.RESET_ALL)
    
def print_data(data):
    logging.info(colorama.Fore.GREEN + str(data) + colorama.Style.RESET_ALL)
    
def print_error(error):
    logging.error(colorama.Fore.RED + str(error) + colorama.Style.RESET_ALL)
    
def print_warning(warning):
    logging.warning(colorama.Fore.YELLOW + str(warning) + colorama.Style.RESET_ALL)