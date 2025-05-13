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
"""The schema for build-related messages sent by planet."""

import typing

from fedora_messaging import message


class Build(message.Message):
    """The message sent when a new post is published in planet."""

    topic = "planet.build"
    body_schema: typing.ClassVar = {
        "id": "https://fedoraproject.org/jsonschema/planet_build.json",
        "$schema": "http://json-schema.org/draft-04/schema#",
        "description": "Message sent when the planet is built",
        "type": "object",
        "properties": {
            "title": {"type": "string"},
            "url": {"type": "string"},
            "Users": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "link": {"type": "string"},
                    "feed": {"type": "string"},
                    "avatar": {"type": "string"},
                    "author": {"type": "string"},
                },
            },
        },
    }

    @property
    def summary(self):
        """Return a summary of the message."""
        title = self.body.get("title", "The planet")
        return f"{title} has been rebuilt"

    def __str__(self):
        """
        Return a complete human-readable representation of the message, which
        in this case is equivalent to the summary.
        """
        return self.summary
