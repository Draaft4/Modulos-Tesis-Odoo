from odoo import api, fields, models, _, tools

class user_odoo_to_flutter(models.Model):
    _name = "user_variables_to_flutter"

    id_client= fields.Many2one(comodel_name='res.partner', string='Cliente')
