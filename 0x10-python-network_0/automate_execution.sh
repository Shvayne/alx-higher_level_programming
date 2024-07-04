#!/usr/bin/bash

Directory="$(dirname "$0")"

find "$Directory" -type f ! -name '*.*' -exec chmod +x {} \;

