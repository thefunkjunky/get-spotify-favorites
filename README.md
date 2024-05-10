# get-spotify-favorites
Gets a Spotify user's saved albums and returns their respective urls

## Pre-Installation Setup
1. Create Spotify developer account
1. Add an application to your developer account (https://developer.spotify.com/documentation/web-api/tutorials/getting-started)
1. Get your application's client_id and client_secret
1. If using MacOs, install homebrew in your Terminal app (https://brew.sh/)
1. Install zotify (https://github.com/zotify-dev/zotify/blob/main/INSTALLATION.md)
1. Configure Zotify (https://github.com/zotify-dev/zotify/blob/main/README.md#configuration). Note that you should set the root path, the output format, and select the audio quality (if you're a premium user, you can get high quality lossless files).

## Installation
1. Clone this git repo (https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
1. Create a python virtualenv:
  ```python3 venv venv```
1. Activate python virtualenv:
  ```activate venv/bin/activate```
1. Install dependencies:
  ```pip3 install -r requirements.txt```

## Configuration
1. Create `credentials.toml` and fill in your client id and secret:
  ```
client_id = "[client_id]"
client_secret = "[client_secret]"
  ```

## Usage
```
└─▶ python3 get-spotify-favorites.py --help
usage: get-spotify-favorites.py [-h] [--config_file CONFIG_FILE]
                                [--redirect_uri REDIRECT_URI]
                                (--tracks | --albums)

Generate and/or execute new terraform environments.

options:
  -h, --help            show this help message and exit
  --config_file CONFIG_FILE
                        TOML Configuration file for Spotify
                        credentials.
  --redirect_uri REDIRECT_URI
                        Application redirect URI
  --tracks              Return user's liked tracks.
  --albums              Return user's saved albums.
```

### Download tracks
1. Output the URIs from the script above to a file (ex: saved albums)
  ```
python3 get-spotify-favorites.py --albums > uris.txt
  ```
1. Use zotify with URIs list:
  ```
  zotify -d [path to uris list]
  ```

## Contributors
- Garrett Anderson <garrett@devnull.rip>
