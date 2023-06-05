from odoo import http

class getClientData(http.Controller):

    @http.route('/api/clientData', auth='public', website=False, crf=False, type='http', methods=['GET', 'POST'])
    def get_data(self, **kw):
        costumerList = []
        costumers = http.request.env['res.partner'].sudo().search([])
        for costumer in costumers:
            costumerList.append({
                'id': costumer.id,
                'name': costumer.name,

            })

        return print(str(costumerList))
