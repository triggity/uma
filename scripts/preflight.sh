#!/bin/bash -e

if [[ -z "$(which docker)" ]] ; then

  echo "Error, missing tool: docker" >&2
  echo "  sudo apt-get install docker" >&2
  exit 1
fi
