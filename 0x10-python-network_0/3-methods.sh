#!/bin/bash
# display methods it accepts
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
