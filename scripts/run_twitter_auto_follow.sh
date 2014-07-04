#!/bin/bash

VIRTUALENV_DIR=/webapps/youtubeadl
SCRIPT_DIR=$VIRTUALENV_DIR/youtube-audio-dl/scripts/

# Activate the virtual environment
source $VIRTUALENV_DIR/bin/activate
source $VIRTUALENV_DIR/bin/postactivate

# Run the script
cd $SCRIPT_DIR
exec python twitter_auto_follow.py