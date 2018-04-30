# One first needs to copy the qgmlwy file into /usr/share/X11/xkb/symbols/
# Tested on Ubuntu 17.10, Void Linux 4.15.12_1
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
    import os

    _X11_RULES_PATH = '/usr/share/X11/xkb/rules/'
    _X11_SYMBOLS_PATH = '/usr/share/X11/xkb/symbols/'

    if not os.path.isfile(_X11_SYMBOLS_PATH+'qgmlwy'):
        print('Error: Keyboard file not found\nOne first needs to copy the qgmlwy file into /usr/share/X11/xkb/symbols/ before running this script.')
        quit()

    for file_name in ['evdev.xml', 'base.xml']:
        try:
            print('Opening {}...'.format(_X11_RULES_PATH+file_name))
            with open(_X11_RULES_PATH+file_name, 'r+') as f:
                text = f.read()
                assert len(re.findall(r"<layoutList>", text)) == 1
                assert len(re.findall(r"qgmlwy", text)) == 0
                f.seek(0)
                text = re.sub(r"<layoutList>", _XML_INSERTION, text)
                print('Writing {}...'.format(_X11_RULES_PATH+file_name))
                f.write(text)
                f.truncate()
                f.close()
        except Exception as e:
            print('Error writing {}: {}'.format(file_name, e))

    for file_name in ['evdev.lst', 'base.lst']:
        try:
            print('Opening {}...'.format(_X11_RULES_PATH+file_name))
            with open(_X11_RULES_PATH+file_name, 'r+') as f:
                text = f.read()
                assert len(re.findall(r"! layout", text)) == 1
                assert len(re.findall(r"qgmlwy", text)) == 0
                f.seek(0)
                text = re.sub(r"! layout", _LST_INSERTION, text)
                print('Writing {}...'.format(_X11_RULES_PATH+file_name))
                f.write(text)
                f.truncate()
                f.close()
        except Exception as e:
            print('Error writing {}: {}'.format(file_name, e))

if __name__ == '__main__':
    install()
