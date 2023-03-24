from odoo import api, fields, models

class School(models.Model):

    _name="schools.school"

    name=fields.Char(string="Name")
    type=fields.Selection([
        ('Private','Private'),
        ('Goverment','Goverment')
    ])





