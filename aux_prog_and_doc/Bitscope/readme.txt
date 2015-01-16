Running the Bitscope Oscilloscope



Open Sonic Pi from Menu | Programming


Run bitscope & from the terminal


Press the power button on the bitscope UI to start the scope


Choose 5ms/Div, and 1V/Div for Channel A, and Wave Spectrum for the display (purple section)


Play the sound from Sonic Pi, Play 60 is the simplest and see the spectrum and the oscilloscope trace



Initial Setup



Set audio out to the jack, not HDMI, using 

sudo raspi_config


Install sudo dpkg -i bitscope-dso_2.6.EA17H_armhf.deb


Run bitscope &

 choose /dev/ttyUSB0 for the scope source in the setup


