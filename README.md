# STB Time API

This project simulates an API for Societatea de Transport Bucuresti (STB), providing real-time bus/tram arrival information for a specific location and line. It serves as an example of how an API for STB's services might function **if it were available.**

## Description

The API I made for myself fetches real-time public transport arrival information . It mimics the behavior of STB's API by retrieving user authentication data and then querying the STB server for the bus arrival times.

## Usage

### Endpoints

#### 1. Get Current Time for a Specific Stop and Line

- **URL**: `/api/time/<time>/<stop_id>/<line_id>`
- **Method**: `GET`
- **URL Parameters**:
  - `time` (string): Specifies the specific time to retrieve. If set to `'all'`, all times will be returned.
  - `stop_id` (integer): The ID of the stop. - Explained Below
  - `line_id` (integer): The ID of the line. - Explained Below

- **Success Response**:
  - **Code**: 200 OK
  - **Content**:
    - If `time` is `'all'`:
      ```json
      [1, 2, "m"]
      ```
      This indicates the next bus is currently at the stop, another one will arrive in 1 minute, the next in 2 minutes, and another in more than 17 minutes (```m```).
    - If `time` is a specific value (e.g., `1`):
      ```json
      "0"
      ```
      This indicates the next bus is currently at the stop.

- **Error Response**:
  - **Code**: 400 Bad Request
  - **Content**:
    ```json
    "Invalid time index"
    ```
  - **Code**: 500 Internal Server Error
  - **Content**:
    ```json
    "Error message"
    ```

#### Example Usage
 **Retrieve All Times for line 226, Piata Romana Direction, At Piata Romana Stop**:
   ```sh
   curl -X GET http://<your_server_ip>:5000/api/time/all/7317/831
   ```

#### How do I get `station_id` and `line_id`? 👆
- Head to [info.stbsa.ro](https://info.stbsa.ro) and open the developer console
- Select your desired line, then your stop
- Head to the network tab in the developer options and click on the API call that contains the stop ID and line ID as payload
- Change the GET payload and run the API

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
GET localhost:5000/api/time/.../.../...
```

## License
You are free to use this as long as you don't claim it's yours. 
