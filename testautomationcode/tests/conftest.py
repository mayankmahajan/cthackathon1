import os
import logging.config

try:
    log_path = "target/artifacts/"
    os.makedirs(log_path)
except Exception:
    pass

# logging.config.fileConfig(log_path)
# _logger = logging.getLogger(__name__)
