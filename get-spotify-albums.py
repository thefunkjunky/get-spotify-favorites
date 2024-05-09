#!/usr/bin/env python3

import argparse
import json

import toml
import spotipy
from spotipy.oauth2 import SpotifyOAuth


def main():
  """The meat and potatoes"""
  parser = argparse.ArgumentParser(
    description="Generate and/or execute new terraform environments."
  )
  parser.add_argument(
    "--config_file",
    type=str,
    default="credentials.toml",
    help="TOML Configuration file for Spotify credentials."
  )
  parser.add_argument(
    "--redirect_uri",
    type=str,
    default="http://localhost:3000",
    help="Application redirect URI"
  )
  parser.add_argument(
    "--get_liked_tracks",
    action="store_true",
    default=False,
    help="Return user's liked tracks instead of albums."
  )
  args = parser.parse_args()

  with open(args.config_file, "r") as f:
    credentials = toml.loads(f.read())

    scope = "user-library-read"
    sp = spotipy.Spotify(
      auth_manager=SpotifyOAuth(
        client_id=credentials["client_id"],
        client_secret=credentials["client_secret"],
        redirect_uri=args.redirect_uri,
        scope=scope
        )
      )

    offset = 0
    limit = 50
    uris = []
    if args.get_liked_tracks:
      return_function = sp.current_user_saved_tracks
    else:
      return_function = sp.current_user_saved_albums
    while len(return_function(limit=limit, offset=offset)["items"]) > 0:
      for record in return_function(limit=limit, offset=offset)["items"]:
        uris.append(record["album"]["external_urls"]["spotify"])
      offset += 50

    for uri in uris:
      print(uri)


if __name__ == '__main__':
  main()
