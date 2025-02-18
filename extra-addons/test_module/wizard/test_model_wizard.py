from odoo import models, fields, api
from odoo.exceptions import ValidationError


class TestModelWizard(models.TransientModel):
    _name = "test.model.wizard"
    _description = "Wizard for Creating Clients"

    name = fields.Char(string="Имя клиента", required=True)

    @api.constrains("name")
    def _check_name_unique(self):
        """Проверяем, существует ли уже контакт с таким именем"""
        for record in self:
            existing_partner = self.env["res.partner"].search(
                [("name", "=", record.name)], limit=1
            )
            if existing_partner:
                raise ValidationError("Клиент с таким именем уже существует!")

    def action_create_and_add(self):
        """Создаёт контакт и добавляет в clients"""
        partner = self.env["res.partner"].create({"name": self.name})
        active_id = self.env.context.get("active_id")
        test_model = self.env["test.model"].browse(active_id)
        self.env["test.model.line"].create(
            {
                "test_model_id": test_model.id,  # Связь с test.model
                "partner_id": partner.id,  # Связь с res.partner
            }
        )
        return {"type": "ir.actions.act_window_close"}

    def action_create_and_edit(self):
        """Создаёт контакт, добавляет его в clients и открывает форму"""
        partner = self.env["res.partner"].create({"name": self.name})
        active_id = self.env.context.get("active_id")
        test_model = self.env["test.model"].browse(active_id)
        self.env["test.model.line"].create(
            {
                "test_model_id": test_model.id,  # Связь с test.model
                "partner_id": partner.id,  # Связь с res.partner
            }
        )
        return {
            "type": "ir.actions.act_window",
            "res_model": "res.partner",
            "view_mode": "form",
            "res_id": partner.id,
            "target": "current",
        }
