# -*- coding: utf-8 -*-
#
# Copyright (c) 2019 by xt <xt@bash.no>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

#
# (this script requires WeeChat 0.3.0 or newer)
#

# The purpose of this script is to clear a buffer's hotlist when
# hotlist is set to never automatically clear in a pop-down terminal
# with hotlist2extern piping out hotlist data to an external
# desktop watcher widget, for example.

# History:
# 2021-12-03, silverd <alex.shershukov@gmail.com>
# version 0.1: shamelessly stolen from xt <xt@bash.no> and repurposed

import weechat as w
import re

SCRIPT_NAME    = "trigger_activity"
SCRIPT_AUTHOR  = "silverd <alex.shershukov@gmail.com>"
SCRIPT_VERSION = "0.1"
SCRIPT_LICENSE = "GPL3"
SCRIPT_DESC    = "Attempts to clear hotlist in a buffer when WeeChat detects any significant input."

if w.register(SCRIPT_NAME, SCRIPT_AUTHOR, SCRIPT_VERSION, SCRIPT_LICENSE,
                    SCRIPT_DESC, "", ""):

    # Hooks we want to hook
    hook_command_run = {
        "input" : ("/input *",   "command_run_input"),
        "buffer" : ("/buffer *",  "command_run_input"),
        "window" : ("/window *",  "command_run_input"),
        "bar" : ("/bar *",     "command_run_input"),
        "filter" : ("/filter *",  "command_run_input"),
        "cursor" : ("/cursor *",  "command_run_input"),
    }
    # Hook all hooks !
    for hook, value in hook_command_run.items():
        w.hook_command_run(value[0], value[1], "")


def command_run_input(data, buffer, command):

    if command != "/input hotlist_remove_buffer":
        w.command("", "/input hotlist_remove_buffer")

    return w.WEECHAT_RC_OK
