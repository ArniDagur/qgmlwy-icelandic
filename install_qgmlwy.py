# One first needs to copy the qgmlwy file into /usr/share/X11/xkb/symbols/
# Tested on Ubuntu 17.10, Void Linux 4.15.12_1
# WARNING: Don't blame me if this script causes any damage to your setup.

import urllib.request
import re

X11_RULES_PATH = "/usr/share/X11/xkb/rules/"
X11_SYMBOLS_PATH = "/usr/share/X11/xkb/symbols/"
LAYOUT_PATH = X11_SYMBOLS_PATH + "qgmlwy"
XML_INSERTION = """<layoutList>
    <layout>
      <configItem>
        <name>qgmlwy</name>

        <shortDescription>qgmlwy</shortDescription>
        <description>QGMLWY (Icelandic)</description>
        <languageList>
          <iso639Id>ice</iso639Id>
        </languageList>
      </configItem>
      <variantList>
      </variantList>
    </layout>"""


def download_newest_layout():
    url = "https://raw.githubusercontent.com/ArniDagur/qgmlwy-icelandic/master/qgmlwy"
    with urllib.request.urlopen(url) as f:
        return f.read().decode("utf-8")


def get_current_layout():
    try:
        with open(LAYOUT_PATH, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return None


def ensure_layout_up_to_date():
    newest_layout = download_newest_layout()
    current_layout = get_current_layout()
    if newest_layout == current_layout:
        print(f"Layout {LAYOUT_PATH} is up to date")
        return

    print(f"Writing layout to {LAYOUT_PATH} ...")
    with open(LAYOUT_PATH, "w", encoding="utf-8") as f:
        f.write(newest_layout)


def patch_xml_file(xml_path):
    print(f"Opening {xml_path}...")
    with open(xml_path, "r+") as f:
        text = f.read()
        assert len(re.findall(r"<layoutList>", text)) == 1
        assert len(re.findall(r"qgmlwy", text)) == 0
        f.seek(0)
        text = re.sub(r"<layoutList>", XML_INSERTION, text)
        print(f"Writing {xml_path}...")
        f.write(text)
        f.truncate()
        f.close()


LST_INSERTION = """! layout
  qgmlwy          QGMLWY (Icelandic)"""


def patch_lst_file(lst_path):
    print("Opening {}...".format(lst_path))
    with open(lst_path, "r+") as f:
        text = f.read()
        assert len(re.findall(r"! layout", text)) == 1
        assert len(re.findall(r"qgmlwy", text)) == 0
        f.seek(0)
        text = re.sub(r"! layout", LST_INSERTION, text)
        print("Writing {}...".format(lst_path))
        f.write(text)
        f.truncate()
        f.close()


def main():
    ensure_layout_up_to_date()

    for file_name in ["evdev.xml", "base.xml"]:
        try:
            patch_xml_file(X11_RULES_PATH + file_name)
        except Exception as e:
            print("Error writing {}: {}".format(file_name, e))

    for file_name in ["evdev.lst", "base.lst"]:
        try:
            patch_lst_file(X11_RULES_PATH + file_name)
        except Exception as e:
            print("Error writing {}: {}".format(file_name, e))

    return 0


if __name__ == "__main__":
    exit(main())
