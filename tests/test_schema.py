# Copyright (C) 2018  Red Hat, Inc.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""Unit tests for the message schema."""
import json
import os
import unittest

from fedora_messaging import message

from . import FIXTURES_DIR


class ExistingMessagesTests(unittest.TestCase):
    """
    Assert schema successfully handle legacy fedmsg messages.

    The fixtures are generated by downloading messages from datagrepper.
    """

    def test_valid(self):
        message.load_message_classes()
        for message_class, name in message._class_to_schema_name.items():
            if not message_class.topic or not name.startswith("planet"):
                continue

            fixture = os.path.join(FIXTURES_DIR, message_class.topic + ".json")
            with self.subTest(msg=f"Validating {name} with {fixture} failed"):
                with open(fixture) as fp:
                    messages = json.load(fp)

                for m in messages:
                    message_class(body=m).validate()
