# -*- coding: utf-8 -*-
from odoo import models, fields, api


class User(models.Model):
    _inherit = 'res.users'
    
    responsabilidad_ids = fields.One2many('responsabilidades.responsabilidad','usuario_id', string="Responsabilidades asignadas")
    