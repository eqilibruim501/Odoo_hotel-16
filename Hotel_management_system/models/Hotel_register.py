from odoo import api, fields, models


class HotelRegister(models.Model):
    _name = 'hotel.register'
    _description = "This model store the registration of hotels"

    name = fields.Char(string='name')
    number_of_rooms = fields.Integer(string="Rooms", required=True)
    image = fields.Binary(string="image", store="true")
    about = fields.Text(string="About",required=True)
    room_ids = fields.One2many('hotel.room', 'hotel_id', string="Room ids")
    address = fields.Char(string="Address", required=True)

    @api.model
    def create(self, vals_list):
        res = super(HotelRegister, self).create(vals_list)
        for i in range(int(vals_list['number_of_rooms'])):
            self.env['hotel.room'].create({
                "name": f"{vals_list['name']}/room-no:{i}",
                "hotel_id": res.id,
                "Status": "Available"
            })
        return res
