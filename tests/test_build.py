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

from fedora_planet_messages import Build


class TestBuild(unittest.TestCase):
    """Tests for planet_messages.build.Build class."""

    def setUp(self):
        """Set up the tests."""
        self.message = Build()

    def test_summary(self):
        """Assert that correct summary string is returned."""
        self.message.body = {
            "title": "Dummy Planet",
        }
        exp = "Dummy Planet has been rebuilt"
        self.assertEqual(self.message.summary, exp)

    def test_summary_no_title(self):
        """Assert that correct summary string is returned."""
        exp = "The planet has been rebuilt"
        self.assertEqual(self.message.summary, exp)

    def test__str__(self):
        """Assert that correct string is returned."""
        self.assertEqual(self.message.summary, str(self.message))
