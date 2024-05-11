#!/usr/bin/env python3

import argparse

import toml
import spotipy
from spotipy.oauth2 import SpotifyOAuth


def main():
  """The meat and potatoes"""
  parser = argparse.ArgumentParser(
    description="Generate your Spotify liked tracks or album urls"
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
  group = parser.add_mutually_exclusive_group(required=True)
  group.add_argument(
    "--tracks",
    action="store_true",
    default=False,
    help="Return user's liked tracks."
  )
  group.add_argument(
    "--albums",
    action="store_true",
    default=False,
    help="Return user's saved albums."
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
    if args.tracks:
      return_function = sp.current_user_saved_tracks
    else:
      return_function = sp.current_user_saved_albums
    while len(records := return_function(limit=limit, offset=offset)["items"]) > 0:
      for record in records:
        if args.tracks:
          uris.append(record["track"]["external_urls"]["spotify"])
        else:
          uris.append(record["album"]["external_urls"]["spotify"])

      offset += 50

    for uri in uris:
      print(uri)


if __name__ == '__main__':
  main()
