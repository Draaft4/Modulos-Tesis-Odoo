from odoo import api, fields, models, _, tools

class UserOdooToFlutter(models.Model):
    _name = "user.variables"
    _description = 'Usuarios'

    name = fields.Char(string='Nombre')
    id_client = fields.Many2one('res.partner', string='Cliente')