"""
CONFIDENTIAL & PROPRIETARY
Copyright (c) 2025 Jerrold Neal. All Rights Reserved.

NOTICE: This software contains proprietary information and trade secrets of Jerrold Neal.
Use, disclosure, or reproduction is prohibited without the prior express written permission of Jerrold Neal.
PATENT PENDING
"""

import time
import os
import sys

def main():
    print("Starting minimal audio test app...")
    print("This app will play a test sound every 10 seconds.")

    while True:
        print("Playing test sound...")
        # Generate a sine wave using speaker-test (part of alsa-utils)
        # -t sine: Sine wave
        # -f 440: 440Hz
        # -l 1: Loop once
        os.system("speaker-test -t sine -f 440 -l 1 > /dev/null 2>&1")

        print("Waiting...")
        time.sleep(10)

if __name__ == "__main__":
    main()
