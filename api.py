from flask import Flask, jsonify
import requests
import json

app = Flask(__name__)

# CHANGE THESE
stop_id = ""
line_id = ""

infourl = f'https://info.stbsa.ro/v2/api/web/lines/stop?stop_id={stop_id}&selected_line_id={line_id}'

def timpi_linie(continut):
    timpi = []
    linia = str(continut)
    for u in range(3):
        if linia.find('x008') != -1:
            timpul = 'este în stație'
            timpi.append(0)
            linia = linia.replace('x008', ' ')
        elif linia.find('0<8') != -1:
            timpul = 'ajunge într-un minut'
            timpi.append(1)
            linia = linia.replace('0<8', ' ')
        elif linia.find('0x8') != -1:
            timpi.append(2)
            timpul = 'ajunge în două minute'
            linia = linia.replace('0x8', ' ')
        elif linia.find('xb4') != -1:
            timpul = 'ajunge în 3 minute'
            timpi.append(3)
            linia = linia.replace('xb4', ' ')
        elif linia.find('xf0') != -1:
            timpi.append(4)
            timpul = 'ajunge în 4 minute'
            linia = linia.replace('xf0', ' ')
        elif linia.find('xac') != -1:
            timpi.append(5)
            timpul = 'ajunge în 5 minute'
            linia = linia.replace('xac', ' ')
        elif linia.find('xe8') != -1:
            timpi.append(6)
            timpul = 'ajunge în 6 minute'
            linia = linia.replace('xe8', ' ')
        elif linia.find('xa4') != -1:
            timpi.append(7)
            timpul = 'ajunge în 7 minute'
            linia = linia.replace('xa4', ' ')
        elif linia.find('xe0') != -1:
            timpi.append(8)
            timpul = 'ajunge în 8 minute'
            linia = linia.replace('xe0', ' ')
        elif linia.find('x9c') != -1:
            timpi.append(9)
            timpul = 'ajunge în 9 minute'
            linia = linia.replace('x9c', ' ')
        elif linia.find('xd8') != -1:
            timpi.append(10)
            timpul = 'ajunge în 10 minute'
            linia = linia.replace('xd8', ' ')
        elif linia.find('x94') != -1:
            timpi.append(11)
            timpul = 'ajunge în 11 minute'
            linia = linia.replace('x94', ' ')
        elif linia.find('xd0') != -1:
            timpi.append(12)
            timpul = 'ajunge în 12 minute'
            linia = linia.replace('xd0', ' ')
        elif linia.find('x8c') != -1:
            timpi.append(13)
            timpul = 'ajunge în 13 minute'
            linia = linia.replace('x8c', ' ')
        elif linia.find('xc8') != -1:
            timpi.append(14)
            timpul = 'ajunge în 14 minute'
            linia = linia.replace('xc8', ' ')
        elif linia.find('x84') != -1:
            timpi.append(15)
            timpul = 'ajunge în 15 minute'
            linia = linia.replace('x84', ' ')
        elif linia.find('xc0') != -1:
            timpi.append(16)
            timpul = 'ajunge în 16 minute'
            linia = linia.replace('xc0', ' ')
        elif linia.find('xfc') != -1:
            timpi.append(17)
            timpul = 'ajunge în 17 minute'
            linia = linia.replace('xfc', ' ')
        else:
            timpul = 'ajunge în mai mult de 17 minute'
            timpi.append('m')
    return timpi

auth_url = 'https://info.stbsa.ro/v2/api/web/user/auth'
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en,en-CA;q=0.9,ro;q=0.8",
    "App-Id": "buc1d6a5c1a-d152-4b00-a61c-e8f48432824e",
    "App-Version": "0.0.0",
    "App-key": "gcALgRyZHC,qFonZ=Jde",
    "Connection": "keep-alive",
    "Cookie": "_ga=GA1.2.886525681.1707415060; _ga_JJ2M3NQBNH=GS1.1.1707423965.2.0.1707423965.0.0.0",
    "Device-Name": "Chrome",
    "Host": "info.stbsa.ro",
    "Lang": "ro",
    "OS-Type": "Web",
    "OS-Version": "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Referer": "https://info.stbsa.ro/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Source": "ro.radcom.smartcity.web",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "User-Info": "$2a$10$wBghlxGtKeo3mtGAsBZJ4eR4PAMNOHNPUyVjblNSUYNP6Rl6KCty2",
    "sec-ch-ua": "\"Not A(Brand\";v=\"99\", \"Google Chrome\";v=\"121\", \"Chromium\";v=\"121\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}


@app.route('/api/time/<int:time>', methods=['GET'])
def get_current_time(time):
    response = requests.get(auth_url, headers=headers)
    rsp = json.loads(response.text)
    user = rsp["user_info"]

    header = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en,en-CA;q=0.9,ro;q=0.8",
        "App-Id": "buc1d6a5c1a-d152-4b00-a61c-e8f48432824e",
        "App-Version": "0.0.0",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Cookie": "_ga=GA1.2.886525681.1707415060; _ga_JJ2M3NQBNH=GS1.1.1707423965.2.0.1707423965.0.0.0",
        "Device-Name": "Chrome",
        "Host": "info.stbsa.ro",
        "Lang": "ro",
        "OS-Type": "Web",
        "OS-Version": "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "Referer": "https://info.stbsa.ro/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Source": "ro.radcom.smartcity.web",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "User-Info": f"{user}",
        "sec-ch-ua": "\"Not A(Brand\";v=\"99\", \"Google Chrome\";v=\"121\", \"Chromium\";v=\"121\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",

    }
    r = requests.get(infourl, headers=header)
    continut = r.content.split(b'\n')
    timpi = timpi_linie(continut[2])
    timp = time - 1
    return str(timpi[timp])

# Change the DEBUG value!
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
