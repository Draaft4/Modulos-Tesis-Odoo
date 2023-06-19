from odoo import http
from odoo.http import request
import json

class getClientData(http.Controller):

    @http.route('/api/clientData', auth='public', website=False, crf=False, type='http', methods=['GET'])
    def get_data(self, **kw):
        costumerList = []
        costumers = http.request.env['loyalty.card'].sudo().search([])
        for costumer in costumers:
            costumerList.append({
                'partner_id': costumer.partner_id.name,
                'points': costumer.points,

            })

        #return (str(costumerList))
        return request.make_response(json.dumps(costumerList), headers=[('Content-Type', 'application/json')])
