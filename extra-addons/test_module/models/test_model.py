from odoo import api, fields, models


class TestModel(models.Model):
    _name = "test.model"
    _description = "Test Model"

    char_field = fields.Char(string="Char Field")
    text_field = fields.Text(string="Text Field")
    int_field = fields.Integer(string="Integer Field")
    float_field = fields.Float(string="Float Field")
    bool_field = fields.Boolean(string="Boolean Field")
    date_field = fields.Date(string="Date Field")
    datetime_field = fields.Datetime(string="Datetime Field")
    select_field = fields.Selection(
        selection=[("option1", "Option 1"), ("option2", "Option 2")],
        string="Select Field",
    )
    binary_field = fields.Binary(string="Binary Field")

    document_creator = fields.Many2one(
        "res.users",
        string="Создатель документа",
        required=True,
        default=lambda self: self.env.user,
    )

    responsible_partner_id = fields.Many2one(
        "res.partner",
        string="Ответственный",
        compute="_compute_responsible_editable",
        store=True,
    )

    @api.depends("document_creator")
    def _compute_responsible_editable(self):
        for record in self:
            record.responsible_editable = bool(record.document_creator)
