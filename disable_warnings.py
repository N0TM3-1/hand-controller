import os
import logging
def disable():
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # 0 = all logs, 3 = only fatal errors
    os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'  # optional: disables oneDNN
    logging.getLogger('tensorflow').setLevel(logging.FATAL)