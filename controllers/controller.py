from odoo import http
from odoo.http import request
from odoo import models,fields
import datetime
import json


class getClientData(http.Controller):

    @http.route('/api/loyaltyData', auth='public', website=False, crf=False, type='http', methods=['GET'])
    def getLoyalty(self, **kw):
        loyaltyList = []
        id_user = int(http.request.params.get('id'))
        loyaltyUsers = http.request.env['loyalty.card'].sudo().search([])

        for loyaltyUser in loyaltyUsers:
          partner_id = loyaltyUser.partner_id.id
          if id_user == partner_id:
            loyaltyList.append({
                'id':partner_id,
                'points': loyaltyUser.points,
            })
            return request.make_response(json.dumps(loyaltyList), headers=[('Content-Type', 'application/json')])
          else:
              return http.request.make_response(json.dumps({'message': 'User not found'}),
                                                headers=[('Content-Type', 'application/json')])



    @http.route('/api/clientData', auth='public', website=False, crf=False, type='http', methods=['GET'])
    def getUserData(self, **kw):
        user_id = int(http.request.params.get('id'))
        user = http.request.env['res.partner'].sudo().browse(user_id)
        if user.exists():
            user_data = {
                'id': user.id,
                'name': user.name,
                'email': user.email
            }
            return http.request.make_response(json.dumps(user_data), headers=[('Content-Type', 'application/json')])
        else:
            return http.request.make_response(json.dumps({'message': 'User not found'}),
                                              headers=[('Content-Type', 'application/json')])

    @http.route('/api/login', type='http',auth='public',methods=['GET'],csrf=False)
    def sendLogin(self,**kwargs):

        email=http.request.params.get('email')
        contact=http.request.env['res.partner'].sudo().search([('email','=',email)])
        if contact:
            return json.dumps({'partner_id': contact.id,'message':'ok'
                               })
        else:
            return json.dumps({'partner_id': 0,'message':'error'})

    @http.route('/api/listcupons', type='http', auth='public', methods=['GET'], csrf=False)
    def getCupons(self, **kwargs):
        rewards = []
        loyalty_rewards = http.request.env['loyalty.reward'].sudo().search([])
        program_id = 6

        for reward in loyalty_rewards.filtered(lambda r: r.program_id.id == program_id):
            rewards.append({
                'description': reward.description,
                'required_points': reward.required_points,
            })

        return http.request.make_response(json.dumps(rewards), headers=[('Content-Type', 'application/json')])

    # @http.route('/api/discountcupons', type='http',auth='public',methods=['GET'],crsf=False)
    # def getdiscount(self, **kwargs):
    #     cupondis = []
    #     id_user = int(http.request.params.get('id'))
    #     print(id_user)
    #     discounts= http.request.env['loyalty.card'].sudo().search([])
    #     for discount in discounts:
    #         partner_id = discounts.partner_id.id
    #
    #         if id_user == partner_id:
    #             print("entra")
    #             cupondis.append({
    #             'name': discount.program_id.name,
    #             'codigo':discount.code,
    #             'fecha caducidad':discount.expiration_date
    #             })
    #     return request.make_response(json.dumps(cupondis), headers=[('Content-Type', 'application/json')])



    @http.route('/api/coupons', type='http', auth='public', methods=['GET'], csrf=False)
    def getCoupons(self, **kw):
        id_user = int(http.request.params.get('id'))
        coupons = http.request.env['loyalty.card'].sudo().search([('partner_id', '=', id_user)])

        coupon_data = []


        for coupon in coupons:
            expiration_date = coupon.expiration_date
            if expiration_date:
                expiration_date = expiration_date.strftime('%Y-%m-%d')
                coupon_data.append({
                'code': coupon.code,
                'program_name': coupon.program_id.name,
                'fecha de expiracion':expiration_date

                })

        return http.request.make_response(json.dumps(coupon_data), headers=[('Content-Type', 'application/json')])
