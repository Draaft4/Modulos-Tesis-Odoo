from odoo import models, api

class CustomLoyalty(models.Model):
    _inherit="loyalty.card"

    @api.model
    def write(self, vals):
        res = super(CustomLoyalty, self).write(vals)
        if not self.env.context.get('loyalty_no_mail', False) and 'points' in vals:
            points_before = {coupon: coupon.points for coupon in self}
            print(points_before)
        if not self.env.context.get('loyalty_no_mail', False) and 'points' in vals:
            points_changes = {coupon: {'old': points_before[coupon], 'new': coupon.points} for coupon in self}
            print(points_changes)
        return res