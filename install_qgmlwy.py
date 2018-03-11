# One first needs to copy the qgmlwy file into /usr/share/X11/xkb/symbols/
# Tested on Ubuntu 17.10
# WARNING: Don't blame me if this script causes any damage to your setup.

_XML_INSERTION = """<layoutList>
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

_LST_INSERTION = """! layout
  qgmlwy          QGMLWY (Icelandic)"""

def install():
    import re

    _X11_PATH = "/usr/share/X11/xkb/rules/"

    for file_name in ['evdev.xml', 'base.xml']:
        print('Opening {}...'.format(_X11_PATH+file_name))
        with open(_X11_PATH+file_name, 'r+') as f:
            text = f.read()
            assert len(re.findall(r"<layoutList>", text)) == 1
            assert len(re.findall(r"qgmlwy", text)) == 0
            f.seek(0)
            text = re.sub(r"<layoutList>", _XML_INSERTION, text)
            print('Writing {}...'.format(_X11_PATH+file_name))
            f.write(text)
            f.truncate()
            f.close()

    for file_name in ['evdev.lst', 'base.lst']:
        print('Opening {}...'.format(_X11_PATH+file_name))
        with open(_X11_PATH+file_name, 'r+') as f:
            text = f.read()
            assert len(re.findall(r"! layout", text)) == 1
            assert len(re.findall(r"qgmlwy", text)) == 0
            f.seek(0)
            text = re.sub(r"! layout", _LST_INSERTION, text)
            print('Writing {}...'.format(_X11_PATH+file_name))
            f.write(text)
            f.truncate()
            f.close()

if __name__ == '__main__':
    install()
