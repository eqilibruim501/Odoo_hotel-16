from odoo import api, fields, models


class RegisterUser(models.Model):
    _name = 'booking.register'
    _description = "this model holds the data of Customers for the website"

    name_id = fields.Many2one('res.users', string='User', required=True, ondelete='cascade')
    phone = fields.Char(string='Phone')
    Email = fields.Char(string='Email', required=True)
    Password = fields.Char(string='Password', required=True)
    Gender = fields.Selection([('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
