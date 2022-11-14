# import re
import re

r = re.compile(r"([0-9]+)' ([0-9]*\.?[0-9]+)\"")

def get_inches(height):
    """Calculates the number of inches in a given impirical height.

    Args:
        height (string): hieght consisting of feet and inches as string

    Returns:
        float: Number of inches
    """
    m = r.match(height)
    return float('NaN') if m is None else int(m.group(1))*12 + float(m.group(2))



