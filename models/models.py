# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CaseHistoryGroup(models.Model):
    _name = 'case.group'
    _description = 'Case History Group'

    name = fields.Char('Group name', required=True, translate=True)
    title = fields.Char('Group title', translate=True)
    shortdesc = fields.Char('Short Description', translate=True)
    h_type = fields.Selection([('gallery', 'Picture Gallery'),('reference','Reference Tab')], default="gallery", string="Type of Group")
    icon_all = fields.Binary("Group Pics", attachment=True, help="Main image for Category")
    category_ids = fields.One2many('case.category','group_id')
    #ref_ids = fields.Many2one('case.history','Reference')

class CaseHistoryCategory(models.Model):
    _name = 'case.category'
    _description = 'Case History Categories (tags)'
    
    name = fields.Char('Category name', required=True, translate=True)
    icon = fields.Binary("Category Icon", attachment=True, help="Category icon to be used as selector")
    group_id = fields.Many2one('case.group', 'Group', help="Specify wich group the category belong to", required=True)


class CaseHistory(models.Model):
    _name = 'case.history'
    _description = 'Case History'
    _order = 'priority'
    
    name = fields.Char('Reference Title', required=True, translate=True)
    description = fields.Text('Reference Description', translate=True)
    active = fields.Boolean('Active?', default=True)
    priority = fields.Integer('Priority',default="100")
    orientation = fields.Selection([('vertical', 'vertical'),('horizontal','horizontal')],default="horizontal")
    
    group_id = fields.Many2one('case.group', string='Group of reference', help="Specify wich group the Reference belong to", required=True)

    tags_ids = fields.Many2many('case.category', string="References Tags", help="Insert a classification of the references")
    credits = fields.Text('Credits',
                              help="Partner who did the job")

    # image: all image fields are base64 encoded and PIL-supported
    image = fields.Binary(
        "Image", attachment=True,
        help="This field holds the image used as image for the reference.")
    
