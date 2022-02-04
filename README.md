This is the [QGMLWY keyboard layout](http://mkweb.bcgsc.ca/carpalx/) modified for Icelandic language use.

The Icelandic characters were not placed in a scientific manner, but like in the original layout, all vowels are positioned on the right half of the keyboard, and all consonants on the left.

---
### For Icelandic Characters:
| Key Combination | Character |
| --- | --- |
| alt-gr + a | á |
| alt-gr + e | é |
| alt-gr + o | ó |
| alt-gr + h | æ |
| alt-gr + u | ú |
| alt-gr + y | ý |
| alt-gr + b | ö |
| alt-gr + t | ð |
| alt-gr + n | þ |
| alt-gr + i | í |

---
### Installation:

1. Clone this repository and enter it: `git clone https://github.com/ArniDagur/qgmlwy-icelandic.git`

2. Enter it: `cd qgmlwy-icelandic`

3. Copy 'qgmlwy' file to X11 symbols directory: `sudo cp qgmlwy /usr/share/X11/xkb/symbols/`

4. Run: `sudo python install_qgmlwy.py`

---
### Troubleshooting:
**Right-alt does not produce Icelandic keys:** If you use GNOME, make sure that you have the 'compose key' disabled in Tweaks Tool -> Keyboard & Mouse.
