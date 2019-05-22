#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# Copyright (c) 2019 Pekka Wallendahl
# 
# LICENSE: MIT

__module_name__ = "daychanged"
__module_version__ = "0.42"
__module_description__ = "Print the new date on midnight"

import hexchat   
import schedule
from datetime import datetime

MODULE_DEBUG = False

def print_day_changed():
    date_fmt = '%a %d %b %Y (%Y-%m-%d)'
    date = datetime.now().strftime(date_fmt)
    channel_list = hexchat.get_list("channels")
    for item in channel_list:
        context = hexchat.find_context(channel=item.channel)  
        context.prnt('\002\00315Day changed to {}'.format(date))

def schedule_callback(userdata):
    schedule.run_pending()
    return True

def main():
    if MODULE_DEBUG:
        hexchat.prnt("daychanged.py: DEBUG MODE")
        schedule.every(5).seconds.do(print_day_changed)
    schedule.every().day.at("00:00").do(print_day_changed)
    
    hexchat.hook_timer(1000, schedule_callback)
    
if __name__ == '__main__':
    main()
