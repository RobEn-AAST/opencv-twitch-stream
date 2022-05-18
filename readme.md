# setup process

### get you stream key from here
http://www.twitch.tv/youruser/dashboard/streamkey

### Dependencies  

```bash
sudo pip install python-twitch-stream
```

```bash
sudo apt update
sudo apt install ffmpeg
ffmpeg -version
```

```bash
python stream.py -s <your stream key>
```
## How to use it
```python
""" use 0 or 1 to stream from a camera """
STREAM_FROM = 'vid.mp4' # change this vid path
```


