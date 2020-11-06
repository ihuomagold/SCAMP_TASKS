import re

emails = """
IhuomaOgbuji@futo.edu
angelafube23@gmail.com
alexx-31-lazzo@cisco.net
"""

pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(edu|com|net)')

matches = pattern.finditer(emails)

for match in matches:
    print(match)
