from flask import Flask, jsonify
import requests
import json
from threading import Timer
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

user_info = ''


def getAuth():
    global user_info
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
        "sec-ch-ua": "\"Not A(Brand\";v=\"99\", \"Google Chrome\";v=\"121\", \"Chromium\";v=\"121\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    try:
        response = requests.get(auth_url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        rsp = response.json()
        user_info = rsp.get("user_info", "")
        print("User info updated:", user_info)
    except requests.exceptions.RequestException as e:
        print("Error updating user info:", e)

    # Schedule the function to run again in 30 minutes
    Timer(1800, getAuth).start()


getAuth()  # Initial call to authenticate and set up the timer


def timpi_linie(continut):
    timpi = []
    linia = str(continut)
    for u in range(3):
        if 'x008' in linia:
            timpul = 'este în stație'
            timpi.append(0)
            linia = linia.replace('x008', ' ')
        elif '0<8' in linia:
            timpul = 'ajunge într-un minut'
            timpi.append(1)
            linia = linia.replace('0<8', ' ')
        elif '0x8' in linia:
            timpi.append(2)
            timpul = 'ajunge în două minute'
            linia = linia.replace('0x8', ' ')
        elif 'xb4' in linia:
            timpul = 'ajunge în 3 minute'
            timpi.append(3)
            linia = linia.replace('xb4', ' ')
        elif 'xf0' in linia:
            timpi.append(4)
            timpul = 'ajunge în 4 minute'
            linia = linia.replace('xf0', ' ')
        elif 'xac' in linia:
            timpi.append(5)
            timpul = 'ajunge în 5 minute'
            linia = linia.replace('xac', ' ')
        elif 'xe8' in linia:
            timpi.append(6)
            timpul = 'ajunge în 6 minute'
            linia = linia.replace('xe8', ' ')
        elif 'xa4' in linia:
            timpi.append(7)
            timpul = 'ajunge în 7 minute'
            linia = linia.replace('xa4', ' ')
        elif 'xe0' in linia:
            timpi.append(8)
            timpul = 'ajunge în 8 minute'
            linia = linia.replace('xe0', ' ')
        elif 'x9c' in linia:
            timpi.append(9)
            timpul = 'ajunge în 9 minute'
            linia = linia.replace('x9c', ' ')
        elif 'xd8' in linia:
            timpi.append(10)
            timpul = 'ajunge în 10 minute'
            linia = linia.replace('xd8', ' ')
        elif 'x94' in linia:
            timpi.append(11)
            timpul = 'ajunge în 11 minute'
            linia = linia.replace('x94', ' ')
        elif 'xd0' in linia:
            timpi.append(12)
            timpul = 'ajunge în 12 minute'
            linia = linia.replace('xd0', ' ')
        elif 'x8c' in linia:
            timpi.append(13)
            timpul = 'ajunge în 13 minute'
            linia = linia.replace('x8c', ' ')
        elif 'xc8' in linia:
            timpi.append(14)
            timpul = 'ajunge în 14 minute'
            linia = linia.replace('xc8', ' ')
        elif 'x84' in linia:
            timpi.append(15)
            timpul = 'ajunge în 15 minute'
            linia = linia.replace('x84', ' ')
        elif 'xc0' in linia:
            timpi.append(16)
            timpul = 'ajunge în 16 minute'
            linia = linia.replace('xc0', ' ')
        elif 'xfc' in linia:
            timpi.append(17)
            timpul = 'ajunge în 17 minute'
            linia = linia.replace('xfc', ' ')
        else:
            timpul = 'ajunge în mai mult de 17 minute'
            timpi.append('m')
    return timpi


@app.route('/api/time/<string:time>/<int:stop_id>/<int:line_id>', methods=['GET'])
def get_current_time(time, stop_id, line_id):
    infourl = f'https://info.stbsa.ro/v2/api/web/lines/stop?stop_id={stop_id}&selected_line_id={line_id}'
    headers = {
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
        "User-Info": f"{user_info}",
        "sec-ch-ua": "\"Not A(Brand\";v=\"99\", \"Google Chrome\";v=\"121\", \"Chromium\";v=\"121\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
    }

    try:
        r = requests.get(infourl, headers=headers)
        r.raise_for_status()  # Raise an HTTPError for bad responses
        continut = r.content.split(b'\n')
        timpi = timpi_linie(continut[2])
        if time == 'all':
            return jsonify(timpi)
        else:
            timp = int(time) - 1
            if 0 <= timp < len(timpi):
                return str(timpi[timp])
            else:
                return "Invalid time index", 400
    except requests.exceptions.RequestException as e:
        return str(e)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
