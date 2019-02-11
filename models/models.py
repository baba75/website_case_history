# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CaseHistoryCategory(models.Model):
    _name = 'case.category'
    _description = 'Case History Categories (tags)'
    
    name = fields.Char('Category name', required=True, translate=True)
    icon = fields.Binary("Category Icon", attachment=True, help="Category icon to be used as selector")


class WebsiteCaseHistory(models.Model):
    _name = 'case.history'
    _description = 'Case History'
    _order = 'priority'
    
    name = fields.Char('Reference Title', required=True, translate=True)
    description = fields.Text('Reference Description', translate=True)
    active = fields.Boolean('Active?', default=True)
    priority = fields.Integer('Priority',default="100")
    orientation = fields.Selection([('vertical', 'vertical'),('horizontal','horizontal')],default="horizontal")
    
    tags_ids = fields.Many2many('case.category', string="References Tags", help="Insert a classification of the references")
    credits = fields.Text('Credits',
                              help="Partner who did the job")

    # image: all image fields are base64 encoded and PIL-supported
    image = fields.Binary(
        "Image", attachment=True,
        help="This field holds the image used as image for the reference.")
    
