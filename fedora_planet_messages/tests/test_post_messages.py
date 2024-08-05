# Copyright (C) 2020  Red Hat, Inc.
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
"""Unit tests for the project related message schema."""

import unittest

from fedora_planet_messages import PostNew


class TestPostNew(unittest.TestCase):
    """Tests for planet_messages.post_messages.PostNew class."""

    def setUp(self):
        """Set up the tests."""
        self.message = PostNew()

    def test_name(self):
        """Assert that name is returned."""
        self.message.body = {"name": "Best blog in the world"}

        self.assertEqual(self.message.name, "Best blog in the world")

    def test_name_missing(self):
        """Assert that None is returned when name is missing."""
        self.message.body = {}

        self.assertEqual(self.message.name, None)

    def test_username(self):
        """Assert that username is returned."""
        self.message.body = {"username": "Khorne"}

        self.assertEqual(self.message.agent_name, "Khorne")
        self.assertEqual(self.message.username, "Khorne")
        self.assertEqual(self.message.usernames, ["Khorne"])

    def test_username_missing(self):
        """Assert that None is returned when username is missing."""
        self.message.body = {}

        self.assertEqual(self.message.agent_name, None)
        self.assertEqual(self.message.username, None)
        self.assertEqual(self.message.usernames, [])

    def test_post_title(self):
        """Assert that post title is returned."""
        self.message.body = {"post": {"title": "Best blogpost in the world"}}

        self.assertEqual(self.message.post_title, "Best blogpost in the world")

    def test_post_title_missing(self):
        """Assert that None is returned when post title is missing."""
        self.message.body = {"post": {}}

        self.assertEqual(self.message.post_title, None)

    def test_face(self):
        """Assert that URL to avatar is returned."""
        self.message.body = {"face": "https://face.com"}

        self.assertEqual(self.message.face, "https://face.com")

    def test_face_missing(self):
        """Assert that None is returned when avatar URL is missing."""
        self.message.body = {}

        self.assertEqual(self.message.face, None)

    def test__str__(self):
        """Assert that correct string is returned."""
        self.message.body = {
            "username": "Khorne",
            "post": {"title": "Best blogpost in the world"},
        }

        exp = "A new post 'Best blogpost in the world' was published on planet by 'Khorne'."

        self.assertEqual(self.message.__str__(), exp)

    def test_summary(self):
        """Assert that correct summary string is returned."""
        self.message.body = {
            "username": "Khorne",
            "post": {"title": "Best blogpost in the world"},
        }

        exp = "A new post 'Best blogpost in the world' was published on planet by 'Khorne'."

        self.assertEqual(self.message.__str__(), exp)

    def test_summary_missing(self):
        """Assert that correct summary string is returned when the properties are missing."""
        self.message.body = {"post": {}}

        exp = "A new post 'None' was published on planet by 'None'."

        self.assertEqual(self.message.__str__(), exp)
