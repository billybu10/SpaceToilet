#!/usr/bin/python

#  Copyright (c) Lightstreamer Srl.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import os
import signal

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
gi.require_version('AppIndicator3', '0.1')
from gi.repository import AppIndicator3

from lightstreamer.client import *
from subscription_listener import *

APPINDICATOR_ID = "example-pokemon-appindicator"


def main():
	loggerProvider = ConsoleLoggerProvider(ConsoleLogLevel.WARN)
	LightstreamerClient.setLoggerProvider(loggerProvider)
	global lightstreamer_client
	lightstreamer_client = LightstreamerClient("http://push.lightstreamer.com", "ISSLIVE")
	lightstreamer_client.connect()
	global subscription
	subscription = Subscription(
        mode="MERGE",
        items=["NODE3000005"],
        fields=["TimeStamp", "Value"])
	

	global indicator
	indicator = AppIndicator3.Indicator.new(
			APPINDICATOR_ID,
			os.path.abspath("space-toilet-icon.svg"),
			AppIndicator3.IndicatorCategory.SYSTEM_SERVICES)
	indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
	indicator.set_menu(menu_build())
	indicator.set_label("1%", "")
	subscription.addListener(SubListener())
	lightstreamer_client.subscribe(subscription)
	Gtk.main()
	


def menu_build():
	"""Return a Gtk+ menu."""
	menu = Gtk.Menu()

	item_quit = Gtk.MenuItem("Quit")
	item_quit.connect('activate', quit)
	menu.append(item_quit)

	menu.show_all()
	
	return menu

def quit(source):
	Gtk.main_quit()
	lightstreamer_client.unsubscribe(subscription)
	lightstreamer_client.disconnect()


if __name__ == "__main__":
	signal.signal(signal.SIGINT, signal.SIG_DFL)
	main()

