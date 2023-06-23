from odoo import api, fields, models, _, tools

class tokkensToResPartner(models.Model):
   _inherit='res.partner'
   tokkens= fields.Many2one('res.partner',string='tokken de sesion')
