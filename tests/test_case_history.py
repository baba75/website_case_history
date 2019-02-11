# -*- coding: utf-8 -*-
from odoo.tests.common import TransactionCase
from odoo.exceptions import AccessError

class TestCaseHistory(TransactionCase):
    
    def setUp(self, *args, **kwargs):
        result = super(TestCaseHistory, self).setUp(*args, **kwargs)
        user_demo = self.env.ref('base.user_demo')
        self.env = self.env(user=user_demo)
        return result

    def test_create(self):
        "Create a simple Reference"
        Case = self.env['case.history']
        ref = Case.create({'name': 'Test Reference'})
        
    def setUp(self, *args, **kwargs):
        result = super(TestCaseHistory, self).setUp(*args, **kwargs)
        user_demo = self.env.ref('base.user_demo')
        self.env= self.env(user=user_demo)
        return result
    
    def test_record_rule(self):
        "Test per user record rules"
        Case = self.env['case.history']
        ref = Case.sudo().create({'name': 'Admin Reference'})
        with self.assertRaises(AccessError):
            Case.browse([ref.id]).name
    
    
