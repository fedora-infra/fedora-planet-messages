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
"""The schema for post-related messages sent by planet."""

import typing

from fedora_messaging import message


class PostNew(message.Message):
    """The message sent when a new post is published in planet."""

    topic = "planet.post.new"
    body_schema: typing.ClassVar = {
        "id": "https://fedoraproject.org/jsonschema/planet_post_new1.json",
        "$schema": "http://json-schema.org/draft-04/schema#",
        "description": "Message sent when a new post is published on planet",
        "type": "object",
        "required": ["post"],
        "properties": {
            "username": {"type": "string"},
            "face": {"type": "string"},
            "name": {"type": "string"},
            "post": {"type": "object", "properties": {"title": {"type": "string"}}},
        },
    }

    @property
    def name(self):
        """Name of the planet blog."""
        return self.body.get("name", None)

    @property
    def agent_name(self):
        """User that did the action."""
        return self.body.get("username", None)

    @property
    def username(self):
        return self.agent_name

    @property
    def usernames(self):
        return [self.agent_name] if self.agent_name is not None else []

    @property
    def post_title(self):
        """Title of the post."""
        return self.body["post"].get("title", None)

    @property
    def face(self):
        """URL to user avatar."""
        return self.body.get("face", None)

    @property
    def summary(self):
        """Return a summary of the message."""
        return f"A new post '{self.post_title}' was published on planet by '{self.username}'."

    def __str__(self):
        """
        Return a complete human-readable representation of the message, which
        in this case is equivalent to the summary.
        """
        return self.summary
