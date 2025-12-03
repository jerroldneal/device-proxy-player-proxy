# Player Proxy

This is the audio-specific implementation of the audio driver proxy. It captures audio from ALSA and forwards it to the host.

## Usage

1. Build the base audio-driver-proxy image:

   ```bash
   cd ../audio-driver-proxy
   docker build -t audio-driver-proxy .
   ```

2. Start the player proxy:

   ```bash
   npm start
   ```

   Or manually:

   ```bash
   docker build -t player-proxy .
   docker run --name player-proxy-instance --rm player-proxy
   ```
