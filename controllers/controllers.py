# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from odoo.addons.website.controllers.main import QueryURL

class WebsiteCaseHistory(http.Controller):
    @http.route([
        '/case-history',
        '/case-history/<group>',
        ], type='http', auth='public', website=True)
    def references(self, group=None, **kw):
        Ref = request.env['case.history']  
        Tags = request.env['case.category']
        Group = request.env['case.group']

        references = False
        references_limited = False
        ref_group = Group.search([('name','=',group)])
        # import pdb; pdb.set_trace()
        if ref_group:
            references = Ref.search([('active','=','True'),('group_id','=',ref_group.id)])
            references_limited = Ref.search([('active','=','True'),('group_id','=',ref_group.id)], limit=3)
        tags_list = Tags.search([('group_id','=',ref_group.id)])
        group_list = Group.search([])

        attrib_list = request.httprequest.args.getlist('attrib')
        tag = request.httprequest.args.get('tag')
        tag_record = Tags.browse([('name','=',tag),('group_id','=',ref_group.id)])
        
        keep = QueryURL('case-history',attrib=attrib_list)
        
        values = {
            'group': ref_group,
            'group_list': group_list,
            'reference_ids': references,
            'reference_lmtd': references_limited,
            'tag_ids': tags_list,
            'keep': keep,
            'tag': tag,
        }
        return request.render("website_case_history.Reference_list", values)
