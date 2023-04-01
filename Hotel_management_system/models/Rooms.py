from odoo import api, fields, models


class HotelRooms(models.Model):
    _name = 'hotel.room'
    _description = "This models has the all the information of Rooms with the hotel name"

    name = fields.Char(string="Name")
    hotel_id = fields.Many2one('hotel.register', string="Hotel id", ondelete='cascade')
    Status = fields.Selection([('Available', 'Available'), ('Booked', 'Booked')])
    booking_date = fields.Date(string="date", help="booking date")
    contact = fields.Many2one('res.users', string='User id')
    about = fields.Text(related="hotel_id.about")
