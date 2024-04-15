# STB Time API

This project simulates an API for Societatea de Transport Bucuresti (STB), providing real-time bus/tram arrival information for a specific location and line. It serves as an example of how an API for STB's services might function **if it were available.**

## Description

The API I made for myself fetches real-time bus arrival information for line 25 at a specific location. It mimics the behavior of STB's API by retrieving user authentication data and then querying the STB server for the bus arrival times.

## Usage

### Edit the API info

- To edit which station to get times from, edit the following lines:
`stop_id = "x"` and `line_id = "y"` where `x` and `y` represent IDs that ou get from the official website

#### How? 👆
- Head to [info.stbsa.ro](https://info.stbsa.ro) and open the developer console
- Select your desired line, then your stop
- Head to the network tab in the developer options and click on the API call that contains the stop ID and line ID as payload
- Change the code and run the API


### Endpoints

- `/api/time/<number>`: Returns the arrival time of the next bus/tram for the specified position in your selected line.

### Example

To get the arrival time of the next tram/bus at the position specified in the flask app:

GET /api/time/1

### ESP32 Example

![image](https://github.com/cristilmao/stb-time-api/assets/68418256/132d1e78-7eeb-460f-a6ff-70b242f709cc)

This example shows one use case of the API I created - matrix display on which you can print times remotely only by having internet access - would be useful for someone busy!
ESP32 Code avaliable to download in /example/

## Installation

1. Clone the repository:

```
git clone https://github.com/your-username/stb-time-api.git
cd stb-time-api
```

2. Install requirements & run:
```
pip install -r requirements.txt
python api.py
```

3. Access the API:
```
GET localhost:5000/api/time/1
```

## License
You are free to use this as long as you don't claim it's yours. 
