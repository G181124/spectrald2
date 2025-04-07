
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import argparse
from sigunit.checker import run_username_check
from sigunit.utils import color_text

def print_banner():
    banner = r"""
                          __             __    __
    _________  ___  _____/ /__________ _/ /___/ /
   / ___/ __ \/ _ \/ ___/ __/ ___/ __ `/ / __  / 
  (__  ) /_/ /  __/ /__/ /_/ /  / /_/ / / /_/ /  
 /____/ .___/\___/\___/\__/\__/_/   \__,_/_/\__,_/   
     /_/                                          
    """
    print(color_text(banner, 'yellow'))

def main():
    print_banner()
    parser = argparse.ArgumentParser(description="SpectraLD RLD - Investigative Username OSINT Tool")
    parser.add_argument("--username", help="Username yang ingin dicari", required=True)
    parser.add_argument("--verbose", action="store_true", help="Tampilkan metadata jika tersedia")
    parser.add_argument("--fast", action="store_true", help="Aktifkan multithread untuk kecepatan maksimal")
    args = parser.parse_args()
    run_username_check(args.username, verbose=args.verbose)

if __name__ == "__main__":
    main()
