import atexit
import sys
import time

import pynvml
from prometheus_client import start_http_server

from .standard_metrics import register_standard_metrics

def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9200

    try:
        pynvml.nvmlInit()
        atexit.register(pynvml.nvmlShutdown)

        register_standard_metrics()

        print('Starting on port {}'.format(port))
        start_http_server(port)

        while True:
            time.sleep(10)
    except pynvml.NVMLError, err:
        print('NVML error: {}'.format(err))

if __name__ == '__main__':
    main()
