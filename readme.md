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

## Docker setup

#### docker-compose.yml file

```docker
# docker-compose.yml
services:
  streaming-twitch:
    build: .
    command: python3 -u stream.py -s <your stream key>
    ports:
      - "1935:1935"
     # - "5000:5000/udp"
     # - "5100:5100/udp"
    volumes:
      - ./codes:/twitch

```
