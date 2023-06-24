from odoo import fields, models

class tokensPartner(models.Model):

   _name = 'tokens.res.partner'

   partner_id = fields.One2many('res.partner','tokens_ids')

   tokens = fields.Char()



