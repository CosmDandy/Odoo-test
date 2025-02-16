from odoo import api, fields, models


class TestModelLine(models.Model):
    _name = "test.model.line"
    _description = "Test Model Line"

    test_model_id = fields.Many2one(
        "test.model", string="Связанный документ", required=True, ondelete="cascade"
    )
    partner_id = fields.Many2one("res.partner", string="Клиент", required=True)
    email = fields.Char(
        string="Email", related="partner_id.email", store=True, readonly=True
    )
