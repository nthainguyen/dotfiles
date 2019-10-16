# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile.config import Key, Screen, Group, Drag, Click, ScratchPad, DropDown
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from settings import MOD, COLS, FONT_PARAMS
from typing import List  # noqa: F401
import os
import subprocess
from libqtile.widget import spacer
import socket

mod = MOD
BORDER_NORMAL = COLS["dark_2"]
# BORDER_FOCUS = COLS["blue_2"]
BORDER_FOCUS = COLS["red_1"]
BORDER_WIDTH = 2
MARGIN = 12

# Define key bindin


@lazy.function
def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)


@lazy.function
def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)


def init_keys():
    keys = [
        # Switch between windows in current stack pane
        Key([mod], "e", lazy.layout.down()),
        Key([mod], "u", lazy.layout.up()),
        Key([mod], "n", lazy.layout.left()),
        Key([mod], "i", lazy.layout.right()),
        # Move windows up or down in current stack
        Key([mod, "shift"], "u", lazy.layout.shuffle_up()),
        Key([mod, "shift"], "e", lazy.layout.shuffle_down()),
        Key([mod, "shift"], "n", lazy.layout.swap_left()),
        Key([mod, "shift"], "i", lazy.layout.swap_right()),
        Key([mod], "o", lazy.layout.swap_main()),
        # Grow and shink the windows
        Key([mod, "mod1"], "u", lazy.layout.grow()),
        Key([mod, "mod1"], "e", lazy.layout.shrink()),
        Key([mod, "shift"], "Return", lazy.window.toggle_floating()),  # Toggle floating
        # Switch window focus to other pane(s) of stack
        Key([mod], "p", lazy.to_screen(0)),  # Keyboard focus screen(1)
        Key([mod], "f", lazy.to_screen(1)),  # Keyboard focus screen(2)
        Key([mod], "space", lazy.layout.next()),
        # Swap panes of split stack
        Key([mod, "shift"], "space", lazy.layout.rotate()),
        # multiple stack panes
        Key([mod, "shift"], "Return", lazy.layout.toggle_split()),
        # Toggle between different layouts as defined below
        Key([mod], "Tab", lazy.next_layout()),
        Key([mod], "q", lazy.window.kill()),
        Key([mod, "control"], "r", lazy.restart()),
        Key([mod, "control"], "q", lazy.shutdown()),
        Key([mod], "t", lazy.screen.toggle_group()),
        Key([mod, "mod1"], "t", lazy.screen.toscreen(1)),
        # Key([mod], "r", lazy.spawncmd()),
    ]
    return keys


def init_layouts():
    layouts = [
        layout.xmonad.MonadTall(
            border_normal=BORDER_NORMAL,
            border_focus=BORDER_FOCUS,
            border_width=BORDER_WIDTH,
            ratio=0.60,
            margin=MARGIN,
            single_border_width=2,
        ),
        layout.Max(
            border_normal=BORDER_NORMAL,
            border_focus=BORDER_FOCUS,
            border_width=BORDER_WIDTH,
            margin=MARGIN,
            single_border_width=2,
        ),
        layout.Stack(
            num_stacks=2,
            border_normal=BORDER_NORMAL,
            border_focus=BORDER_FOCUS,
            border_width=BORDER_WIDTH,
            margin=MARGIN,
            single_border_width=2,
        ),
    ]
    return layouts


widget_defaults = dict(font="sans", fontsize=12, padding=3)
extension_defaults = widget_defaults.copy()


def init_widgets():
    prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
    widgets_list = [
        widget.GroupBox(
            font="Ubuntu Bold",
            fontsize=9,
            margin_y=0,
            margin_x=0,
            padding_y=5,
            padding_x=5,
            borderwidth=1,
            active=COLS["color2"],
            inactive=COLS["color2"],
            rounded=False,
            highlight_method="block",
            this_current_screen_border=COLS["color1"],
            this_screen_border=COLS["color4"],
            other_current_screen_border=COLS["color0"],
            other_screen_border=COLS["color0"],
            foreground=COLS["color2"],
            background=COLS["color0"],
        ),
        widget.Prompt(
            prompt=prompt,
            font="Ubuntu Mono",
            padding=10,
            foreground=COLS["color3"],
            background=COLS["color1"],
        ),
        widget.Sep(
            linewidth=0,
            padding=10,
            foreground=COLS["color2"],
            background=COLS["color2"],
        ),
        widget.WindowName(
            font="Ubuntu",
            fontsize=11,
            foreground=COLS["color5"],
            background=COLS["color0"],
            padding=5,
        ),
        widget.Image(
            scale=True, filename="~/.config/qtile/bar06.png", background=COLS["color6"]
        ),
        widget.Systray(background=COLS["color10"], padding=5),
        widget.Image(
            scale=True,
            filename="~/.config/qtile/bar02-b.png",
            background=COLS["color6"],
        ),
        widget.TextBox(
            text=" ↯",
            foreground=COLS["color0"],
            background=COLS["color6"],
            padding=0,
            fontsize=14,
        ),
        widget.Net(
            interface="wlp5s0",
            foreground=COLS["color0"],
            background=COLS["color6"],
            padding=5,
        ),
        widget.Image(
            scale=True, filename="~/.config/qtile/bar03.png", background=COLS["color3"]
        ),
        widget.TextBox(
            font="Ubuntu Bold",
            text=" ☵",
            padding=5,
            foreground=COLS["color0"],
            background=COLS["color3"],
            fontsize=14,
        ),
        widget.CurrentLayout(
            foreground=COLS["color0"], background=COLS["color3"], padding=5
        ),
        widget.Image(
            scale=True, filename="~/.config/qtile/bar04.png", background=COLS["color7"]
        ),
        widget.TextBox(
            font="Ubuntu Bold",
            text=" ⟳",
            padding=5,
            foreground=COLS["color0"],
            background=COLS["color7"],
            fontsize=14,
        ),
        widget.Pacman(
            execute="urxvtc",
            update_interval=1800,
            foreground=COLS["color0"],
            background=COLS["color7"],
        ),
        widget.TextBox(
            text="Updates",
            padding=5,
            foreground=COLS["color0"],
            background=COLS["color7"],
        ),
        widget.Image(
            scale=True, filename="~/.config/qtile/bar05.png", background=COLS["color8"]
        ),
        widget.TextBox(
            font="Ubuntu Bold",
            text=" ♫",
            padding=5,
            foreground=COLS["color0"],
            background=COLS["color8"],
            fontsize=14,
        ),
        widget.Volume(
            max_chars=40,
            update_interval=0.5,
            foreground=COLS["color0"],
            background=COLS["color8"],
        ),
        widget.Image(
            scale=True, filename="~/.config/qtile/bar07.png", background=COLS["color9"]
        ),
        widget.TextBox(
            font="Ubuntu Bold",
            text=" 🕒",
            foreground=COLS["color2"],
            background=COLS["color9"],
            padding=5,
            fontsize=14,
        ),
        widget.Clock(
            foreground=COLS["color2"],
            background=COLS["color9"],
            format="%A, %B %d - %H:%M",
        ),
        widget.Sep(
            linewidth=0, padding=5, foreground=COLS["color0"], background=COLS["color9"]
        ),
    ]
    return widgets_list


def init_group_names():
    return [
        ("DEV", {"layout": "monadtall"}),
        ("WWW", {"layout": "monadtall"}),
        ("SYS", {"layout": "monadtall"}),
        ("VBOX", {"layout": "monadtall"}),
        ("MEDIA", {"layout": "monadtall"}),
        ("GFX", {"layout": "monadtall"}),
    ]


# DWSVMG is out of the picture for key binding
def init_groups():
    return [Group(name, **kwargs) for name, kwargs in group_names]


# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        {"wmclass": "confirm"},
        {"wmclass": "dialog"},
        {"wmclass": "download"},
        {"wmclass": "error"},
        {"wmclass": "file_progress"},
        {"wmclass": "notification"},
        {"wmclass": "splash"},
        {"wmclass": "toolbar"},
        {"wmclass": "confirmreset"},  # gitk
        {"wmclass": "makebranch"},  # gitk
        {"wmclass": "maketag"},  # gitk
        {"wname": "branchdialog"},  # gitk
        {"wname": "pinentry"},  # GPG key password entry
        {"wmclass": "ssh-askpass"},  # ssh-askpass
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.call([home])


keys = init_keys()
screens = [
    Screen(top=bar.Bar(widgets=init_widgets(), opacity=0.95, size=20)),
    Screen(top=bar.Bar(widgets=init_widgets(), opacity=0.95, size=20)),
]
layouts = init_layouts()
group_names = init_group_names()
groups = init_groups()

groups.extend(
    [
        ScratchPad(
            "scratchpad",
            [
                DropDown("terminal", "gnome-terminal", opacity=0.8),
                DropDown("spotify", "spotify", opacity=0.9, x=0.05, y=0.2, height=0.7),
            ],
        ),
        Group("DEV"),
    ]
)

keys.extend(
    [
        # toggle visibiliy of above defined DropDown named "term"
        Key([], "F10", lazy.group["scratchpad"].dropdown_toggle("terminal")),
        Key([], "F12", lazy.group["scratchpad"].dropdown_toggle("spotify")),
    ]
)

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key([mod], i.name[0].lower(), lazy.group[i.name].toscreen()),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key([mod, "shift"], i.name[0].lower(), lazy.window.togroup(i.name)),
        ]
    )


#   groups = [Group(i) for i in "123456789"]
#
#
#   for i in groups:
#       keys.extend(
#           [
#               # mod1 + letter of group = switch to group
#               Key([mod], i.name, lazy.group[i.name].toscreen()),
#               # mod1 + shift + letter of group = switch to & move focused window to group
#               Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
#           ]
#       )
