from odoo import http
from odoo.http import request
from odoo import models,fields

import json

"""class resPartner(models.model):
    _inherit='res.partner'
    listTokkens= fields.One2many
    """
class getClientData(http.Controller):

    @http.route('/api/loyaltyData', auth='public', website=False, crf=False, type='http', methods=['GET'])
    def getLoyalty(self, **kw):
        loyaltyList = []
        loyaltyUsers = http.request.env['loyalty.card'].sudo().search([])
        for loyaltyUser in loyaltyUsers:
          if loyaltyUser.partner_id.name != False:
            loyaltyList.append({
                'name': loyaltyUser.partner_id.name,
                'points': loyaltyUser.points,
                'point_name':loyaltyUser.point_name
            })
        return request.make_response(json.dumps(loyaltyList), headers=[('Content-Type', 'application/json')])


    @http.route('/api/clientData', auth='public', website=False, crf=False, type='http', methods=['GET'])
    def getClientData(self, **kw):
        ClientList=[]
        clients= http.request.env['res.partner'].sudo().search([])
        for client in clients:
           if client.email!=False :
            ClientList.append({
                'id': client.id,
                'name': client.name,
                'mail': client.email

            })
        return request.make_response(json.dumps(ClientList), headers=[('Content-Type', 'application/json')])


    @http.route('/api/login', auth='public',website=False, crf=False, type='http', methods=['POST'])
    def sendLogin(self,**post_data):

        identific = post_data.get('vat')
        name=post_data.get('name')
        email=post_data.get('email')
        telefono=post_data.get('phone')
        tokken=post_data.get('tokken')
        nuevoUsuario=[identific,name,email,telefono,tokken]
        partner= request.env['res.partner'].create(nuevoUsuario)


        return True
