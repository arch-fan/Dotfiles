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

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import psutil
import os

mod = "mod4"
terminal = guess_terminal()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    # Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], "space", lazy.widget["keyboardlayout"].next_keyboard(), desc="Next keyboard layout."),

    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),

    # ROFI
    Key([mod], "m", lazy.spawn("rofi -show run")),
    Key([mod, 'shift'], "m", lazy.spawn("rofi -show")),
]

groups = [Group(i) for i in [
    "  ", "  ", "  ", "  ", "  ", "  ", " ﭮ "
]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])


layout_conf = {
    'border_focus': '#00bfff',
    'border_width': 1,
    'margin': 5,
    'border_normal': '#000000'
}

layouts = [
    layout.Max(**layout_conf),
    layout.MonadTall(**layout_conf),
    layout.MonadWide(**layout_conf),
]


widget_defaults = dict(
    font="JetBrainsMonoNL Nerd Font Mono Bold",
    fontsize=14,
)

extension_defaults = widget_defaults.copy()

def widgetImage(img_filename, background_color):
    
    home_dir = os.environ['HOME']
    images_path = os.path.join(home_dir, '.config', 'img', img_filename)

    return widget.Image(
        filename=images_path,
        background=background_color,
        scale=True,
    )

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    foreground="#f1ffff",
                    background="#0f101a",
                    fontsize=25,
                    font='JetBrainsMonoNL Nerd Font Mono',
                    margin_y=3,
                    margin_x=0,
                    padding_y=8,
                    padding_x=9,
                    borderwidth=1,
                    active="#f1ffff",
                    rounded=False,
                    disable_drag=True,
                    highlight_method='block',
                    this_current_screen_border="#00bfff",
                    this_screen_border="#5c5c5c",
                    other_current_screen_border="#0f101a",
                    other_screen_border="#0f101a",
                ),

                widget.WindowName(
                    foreground="#00bfff",
                    background="#0f101a",
		            margin_x=3,
                ),

                widgetImage('arrow4.png', '#0f101a'),

                widget.CheckUpdates(
                    display_format='{updates}  ',
                    background='#FFD460',
                    no_update_string='0 ',
                    colour_have_updates='#000000',
                    colour_no_updates='#000000',
                    foreground='#000000',
                ),

                widgetImage('arrow3.png', '#ffd460'),

                widget.KeyboardLayout(
                    fmt=' {}',
                    background='#f38ba0',
                    foreground='#000000',
                    configured_keyboards=['es', 'cn']
                ),

                widgetImage('arrow2.png', '#f38ba0'),

                widget.Memory(
                    format=' RAM: {MemUsed:.0f}{mm}/{MemTotal:.0f}{mm}',
                    background='#ffbcbc',
                    foreground='#000000',
                ),
                
                widgetImage('arrow1.png', '#ffbcbc'),

                widget.CPU(
                    format=' {freq_current} GHz {load_percent}%',
                    background='#edf6e5',
                    foreground='#000000',
                ),

                widgetImage('arrow0.png', '#edf6e5'),

                widget.TextBox(
                    text='',
                    background="#b5eaea",
                    foreground="#0f101a",
                    fontsize=18,
                ),
                widget.Clock(
                    background="#b5eaea",
                    foreground="#0f101a",
                    margin_x=5,
                    format='%d/%m/%Y - %H:%M',
                ),
            ],
            25,
            opacity=1.0,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
