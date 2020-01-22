#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  promptbar.py
#  
#  Copyright 2020  <pi@raspberrypi>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
# This will be the prompt that will be used by the dx2googler script.
#
# Working on it in this seperate file, and will merge into the main
# script when done.

import shutil

dashcolor = '\033[00;01;38;5;51m'
COLS, LINES = shutil.get_terminal_size()
prevnext = ('\033[00;01;38;5;m[
dash = (dashcolor + '\u23BC')
promptbar = (dash * COLS + '\033[m\r\033[1C')


print(promptbar)


#print(COLS)
