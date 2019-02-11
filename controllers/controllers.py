# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from odoo.addons.website.controllers.main import QueryURL

class WebsiteCaseHistory(http.Controller):
    @http.route([
        '/case-history',
        ], type='http', auth='public', website=True)
    def references(self, **kw):
        Ref = request.env['case.history']  
        Tags = request.env['case.category']
        references = Ref.search([('active','=','True')])
        references_limited = Ref.search([('active','=','True')], limit=3)
        tags_list = Tags.search([])
            
        attrib_list = request.httprequest.args.getlist('attrib')
        tag = request.httprequest.args.get('tag')
        tag_record = Tags.browse([('name','=',tag)])
        
        keep = QueryURL('case-history',attrib=attrib_list)
        
        values = {
            'reference_ids': references,
            'reference_lmtd': references_limited,
            'tag_ids': tags_list,
            'keep': keep,
            'tag': tag,
            'tag_record': tag_record,
        }
        return request.render("website_case_history.Reference_list", values)
    