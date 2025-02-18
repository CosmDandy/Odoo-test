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
        store=True,
    )

    responsible_editable = fields.Boolean(
        compute="_compute_responsible_editable", store=False
    )

    clients = fields.One2many("test.model.line", "test_model_id", string="Клиенты")

    option_one = fields.Boolean(string="Опция 1", store=False)
    option_two = fields.Boolean(string="Опция 2", store=False)
    select_all = fields.Boolean(string="Выбрать все", store=False)

    @api.depends("document_creator")
    def _compute_responsible_editable(self):
        for record in self:
            record.responsible_editable = bool(record.document_creator)

    @api.onchange("option_one", "option_two")
    def _onchange_option(self):
        if self._context.get("from_onchange", False):
            return

        # self = self.with_context(from_onchange=True)

        if self.option_one and self.option_two:
            self.select_all = True
        else:
            self.select_all = False

    @api.onchange("select_all")
    def _onchange_select_all(self):
        if self._context.get("from_onchange", False):
            return

        # self = self.with_context(from_onchange=True)

        if self.select_all:
            self.option_one = True
            self.option_two = True
        else:
            self.option_one = False
            self.option_two = False
