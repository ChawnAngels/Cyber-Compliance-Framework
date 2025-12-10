# -----------------------------------------
# signal_extractor.py
# -----------------------------------------
# Purpose:
#   Convert raw device configuration text into
#   simple "signals" that the compliance engine
#   can understand.
#
# Why this matters:
#   Compliance rules don't read switch configs.
#   They read *facts*. This file extracts those facts.
# -----------------------------------------

def extract_signals(config_text):
    """
    Reads configuration text and produces
    a dictionary of simple True/False signals.

    Example signals:
      - ssh_enabled
      - telnet_enabled
      - logging_present
    """

    # Start with all signals as False
    signals = {
        "ssh_enabled": False,
        "telnet_enabled": False,
        "logging_present": False,
        "password_minimum_length": None
    }

    lines = config_text.lower().splitlines()

    for line in lines:

        # Detect SSH usage
        if "transport input ssh" in line:
            signals["ssh_enabled"] = True

        # Detect Telnet usage
        if "transport input telnet" in line:
            signals["telnet_enabled"] = True

        # Detect logging
        if "logging" in line and "buffered" in line:
            signals["logging_present"] = True

        # Detect password minimum length
        if "password minimum-length" in line:
            parts = line.split()
            try:
                signals["password_minimum_length"] = int(parts[-1])
            except:
                pass  # ignore errors for now

    return signals
