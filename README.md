# Presenter Tracking Camera

This repository contains the software for a low-cost video camera for hybrid teaching with presenter movement detection, localization & tracking capability.

### Installation
1. Clone this repo
```sh
git clone https://github.com/pasxn/presenter-tracking-camera.git
cd presenter-tracking-camera
 ```
2. Install dependencies
```sh
pip3 install -r requirements.txt
```
### Testing each module
To test each module seperately run the test scripts.
```sh
python3 test_detectord.py
python3 test_trackerd.py
python3 test_framed.py
python3 test_gimbald.py
```
### Running on your local computer
```sh
./main.py
```
