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

1. Clone this repository: `git clone https://github.com/ArniDagur/qgmlwy-icelandic.git`

2. Enter it: `cd qgmlwy-icelandic`

3. Run: `sudo python install_qgmlwy.py`

---
### Troubleshooting:
**Right-alt does not produce Icelandic keys:** If you use GNOME, make sure that you have the 'compose key' disabled in Tweaks Tool -> Keyboard & Mouse.

### Making MacOS keyboard usable

Set the following settings:

```
echo "1" | sudo tee /sys/module/hid_apple/parameters/swap_opt_cmd
echo "1" | sudo tee /sys/module/hid_apple/parameters/swap_fn_leftctrl
```

These changes can be made permanent. See https://wiki.archlinux.org/title/Apple_Keyboard
