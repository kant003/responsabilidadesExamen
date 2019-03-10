
from odoo import models, fields, api, exceptions



class Responsabilidad(models.Model):
    _name = 'responsabilidades.responsabilidad'
    _description = "Responsabilidades del usuario"
    titulo = fields.Char(string="Titulo", required=True)
    descripcion = fields.Text()

    usuario_id = fields.Many2one('res.users',
        ondelete='set null', string="Asignado a", index=True)

    