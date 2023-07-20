from odoo import models, api
import firebase_admin
from firebase_admin import credentials, messaging

class CustomLoyalty(models.Model):
    _inherit="loyalty.card"

    @api.model
    def write(self, vals):
        res = super(CustomLoyalty, self).write(vals)
        if not self.env.context.get('loyalty_no_mail', False) and 'points' in vals:
            points_before = {coupon: coupon.points for coupon in self}
        if not self.env.context.get('loyalty_no_mail', False) and 'points' in vals:
            points_changes = {coupon: {'old': points_before[coupon], 'new': coupon.points} for coupon in self}
        if not self.env.context.get('loyalty_no_mail', False) and 'points' in vals:
            partner = self.partner_id
            points = self.points
            if(partner.token_ids):
                for token in partner.token_ids:
                    message = messaging.Message(
                    notification=messaging.Notification(
                        title="Has Ganado Puntos!",
                        body=f"Usted ha acumulado ${points}, gracias por su compra.",
                    ),
                    token=token.token,
                )
                response = messaging.send(message)
                print('Successfully sent message:', response)
        return res