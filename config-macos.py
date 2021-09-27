# -*- coding: utf-8 -*-
import string
import re
from xkeysnail.transform import *


define_keymap(lambda wm_class: wm_class not in ("Xfce4-terminal|Your-terminal-app-here"), {
    K("Ctrl-f"): K("RIGHT"),
    K("Ctrl-b"): K("LEFT"),
    K("Ctrl-p"): K("UP"),
    K("Ctrl-n"): K("DOWN"),
    
    K("Ctrl-a"): K("HOME"),
    K("Ctrl-e"): K("END"),

    K("C-d"): K("DELETE"),
    K("C-h"): K("BACKSPACE"),
    K("C-k"): [K("Shift-end"), K("BACKSPACE")]
}, "emacs-like keybind")


command_maps = dict()
for x in string.ascii_lowercase:
    command_maps[K(f"Super-{x}")] = K(f"Ctrl-{x}")

define_keymap(lambda wm_class: wm_class not in ("Xfce4-terminal|Your-terminal-app-here"), command_maps, "mac-like keybind super->command")


# [Conditional keybindings] Terminal
define_keymap(re.compile("Xfce4-terminal|Your-terminal-app-here"), {
    # Keep Ctrl terminal controls and add Cmd as Ctrl+Shift
    K("Super-q"): K("Ctrl-Shift-q"),
    K("Super-w"): K("Ctrl-Shift-w"),
    K("Super-e"): K("Ctrl-Shift-e"),
    K("Super-r"): K("Ctrl-Shift-r"),
    K("Super-t"): K("Ctrl-Shift-t"),
    K("Super-z"): K("Ctrl-Shift-z"),
    K("Super-u"): K("Ctrl-Shift-u"),
    K("Super-i"): K("Ctrl-Shift-i"),
    K("Super-o"): K("Ctrl-Shift-o"),
    K("Super-p"): K("Ctrl-Shift-p"),
    K("Super-a"): K("Ctrl-Shift-a"),
    K("Super-s"): K("Ctrl-Shift-s"),
    K("Super-d"): K("Ctrl-Shift-d"),
    K("Super-f"): K("Ctrl-Shift-f"),
    K("Super-g"): K("Ctrl-Shift-g"),
    K("Super-h"): K("Ctrl-Shift-h"),
    K("Super-j"): K("Ctrl-Shift-j"),
    K("Super-k"): K("Ctrl-Shift-k"),
    K("Super-l"): K("Ctrl-Shift-l"),
    K("Super-y"): K("Ctrl-Shift-y"),
    K("Super-x"): K("Ctrl-Shift-x"),
    K("Super-c"): K("Ctrl-Shift-c"),
    K("Super-v"): K("Ctrl-Shift-v"),
    K("Super-b"): K("Ctrl-Shift-b"),
    K("Super-n"): K("Ctrl-Shift-n"),
    K("Super-m"): K("Ctrl-Shift-m"),
    K("Super-minus"): K("Ctrl-minus"),	
    K("Super-key_0"): K("Ctrl-key_0"),
    K("Super-key_1"): K("Ctrl-key_1"),
    K("Super-key_2"): K("Ctrl-key_2"),
    K("Super-key_3"): K("Ctrl-key_3"),
    K("Super-key_4"): K("Ctrl-key_4"),
    K("Super-key_5"): K("Ctrl-key_5"),
    K("Super-key_6"): K("Ctrl-key_6"),
    K("Super-key_7"): K("Ctrl-key_7"),
    K("Super-key_8"): K("Ctrl-key_8"),
    K("Super-key_9"): K("Ctrl-key_9"),
    K("Super-Space"): K("Ctrl-Space")
}, "Terminal")
