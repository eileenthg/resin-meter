# Genshin Resin Meter
Rainmeter skin to display Genshin notes.

![image](https://github.com/eileenthg/resin-meter/assets/40307498/5371ac10-6293-49e8-a0a5-deb33496e482)

![image](https://github.com/eileenthg/resin-meter/assets/40307498/ebabfac7-05d8-4951-8b54-1c0e69724b4e)

Shows current amount of resin in game using a small display on the top right corner.

Click on the arrow to display full travel notes. Close it by clicking on the full travel note or clicking the arrow again.

Travel notes fetched from Hoyolab API, which includes:
- Current resin
- How much time until resin is full + when it caps (MM/DD/YY, HH:MM:SS)
- Number of commissions completed
- Realm currency
- How much time until realm currency is full + when it caps (MM/DD/YY, HH:MM:SS)
  - note: countdown may be inaccurate. Refer to the cap timestamp.
- Number of expeditions completed

Built on code from [hoyolab-resin-counter](https://github.com/eileenthg/hoyolab-resin-counter-3.0/blob/main/README.md), originally by seriaati.

Data obtained with the help of [genshin.py](https://github.com/thesadru/genshin.py) by thesadru.

# How to install
If you haven't install Rainmeter yet, go [here](https://www.rainmeter.net/) and install it.

Download the latest rmskin [here](https://github.com/eileenthg/resin-meter/releases/), and run it.

Click "Install". Make sure the "Apply included layout" is checked or else the skin will be wonky.
![image](https://github.com/eileenthg/resin-meter/assets/40307498/db29b7f6-b13f-4699-aa28-74cb3caab14c)

If you want the layout setup, load **both** resin/resin.ini and small/arrow.ini and have them running at the same time.
![image](https://github.com/eileenthg/resin-meter/assets/40307498/fa35c0c7-b494-4b7f-9530-e168cd0fc009)

# IMPORTANT!! CONFIGURATION!
You need to link your account to the python file in order to correctly display your stats. Update your data inside the rainmeter skin files.

Right click the skin file and open folder.
![image](https://github.com/eileenthg/resin-meter/assets/40307498/ca8f9406-886a-4834-a116-02b20eb10d3d)

There will be three folders. Navigate to **Resin/full** and **Resin/resin** to access real-time-notes.py for their respective skins.
![image](https://github.com/eileenthg/resin-meter/assets/40307498/5f6dfd84-4a9a-4b74-807d-b4d3b8dad315)
![image](https://github.com/eileenthg/resin-meter/assets/40307498/0455e585-75ea-4a70-a882-818b3f0d5920)

Update these two rows with your own information, for **both** files. Resin/full is for the large display, Resin/resin is for the small display.
![image](https://github.com/eileenthg/resin-meter/assets/40307498/23af1cc7-70bb-4caf-91fd-b9d3bbd1693e)

To get the ltuid and ltoken, refer [here](https://thesadru.github.io/genshin.py/authentication/#how-can-i-get-my-cookies).

