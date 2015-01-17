mcpi_api="/opt/minecraft-pi/api/python/mcpi"
if [[ -z $PYTHONPATH ]]; then
  export PYTHONPATH="$mcpi_api"
elif [[ $PYTHONPATH != *"$mcpi_api"* ]]; then
  export PYTHONPATH="$PYTHONPATH:$mcpi_api"
fi
