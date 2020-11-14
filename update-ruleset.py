import io
import json
import os
import re

TLD = "globaleaks.tor.onion"
RULESET_DIR = "rulesets"

def write_custom_ruleset(entry):
    tld = "." + TLD if entry["slug"] else TLD

    ruleset = "<ruleset name=\"{org_name}\">\n" \
              "  <target host=\"{slug}{globaleaks_tld}\" />\n" \
              "  <rule from=\"^http[s]?:\/\/([a-z0-9\-]+[.])?{slug}{globaleaks_tld}\" to=\"http://$1{onion_address}\" />\n" \
              "</ruleset>\n".format(
        org_name=entry["title"],
        slug=entry["slug"],
        onion_address=entry["onion_address"],
        globaleaks_tld=tld
    )

    RULESET_OUTPUT = "globaleaks-ruleset.xml"
    with open(
        os.path.join(RULESET_DIR, entry["slug"] + tld + ".xml"),
        "w",
    ) as f:
        f.write(ruleset)


if __name__ == "__main__":
    with io.open("directory.json", "r", encoding="utf-8") as f:
        directory = json.loads(f.read().rstrip("\n"))

    for entry in directory:
        write_custom_ruleset(entry)
