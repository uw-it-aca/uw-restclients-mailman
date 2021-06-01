# Copyright 2021 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from unittest import TestCase
from uw_mailman.basic_list import _get_url_path, exists, get_admin_url
from uw_mailman.util import fdao_mailman_override


@fdao_mailman_override
class TestMailmanBasicList(TestCase):

    def test_get_url_path(self):
        self.assertEqual(
            _get_url_path('aaa_au12'),
            "/__mock_key__/admin/v1.0/uwnetid/available/?uwnetid=aaa_au12")

    def test_exists(self):
        self.assertFalse(exists('bbio180a_au12'))
        self.assertTrue(exists('bbio180a_au13'))
        self.assertFalse(exists("tbus310a_au13"))
        self.assertTrue(exists("bill_au13"))

    def test_get_admin_url(self):
        self.assertEqual(
            get_admin_url("bbio180a_su13"),
            "https://mailman.u.washington.edu/mailman/admin/bbio180a_su13")
