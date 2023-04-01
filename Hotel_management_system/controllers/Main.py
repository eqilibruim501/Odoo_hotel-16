from odoo import http
from odoo.http import request
from odoo.addons.web.controllers.main import home
from datetime import date


class Extension_Home(home.Home):

    @http.route()
    def web_login(self, redirect=None, **kw):
        res = super(Extension_Home, self).web_login()
        if 'login' in kw:
            login = kw.get('login')
            password = kw.get('password')
            print(f"{login}:{password}")
            uid = request.session.authenticate(request.env.cr.dbname, kw.get('login'), kw.get('password'))
            if uid:
                return request.redirect(f'/hotel_booking/home/{uid}')
            else:
                print("No data found")
            return request.redirect('/web/login')
        return res


class BookingSystem(http.Controller):

    @http.route('/hotel_booking/index', type="http", auth="public", website=True)
    def index(self, **kw):
        return request.render('Hotel_management_system.index')

    @http.route('/hotel_booking/login', type="http", auth="public", website=True)
    def login(self, **kw):
        return request.render('Hotel_management_system.bookingLogin')

    @http.route('/login/Authenticate/', type="http", auth="public")
    def authenticate_login(self, **kw):
        try:
            uid = request.session.authenticate(request.env.cr.dbname, kw.get('email'), kw.get('password'))
            return request.redirect(f'/hotel_booking/home/{uid}')
        except Exception as e:
            print("Authentication failed", e)
        return request.redirect('/hotel_booking/login')

    @http.route('/hotel_booking/home/<int:id>', type="http", auth="public", website=True)
    def home(self, id, **kw):
        user = request.env['res.users'].browse(id)
        rooms = request.env['hotel.room'].sudo().search([('Status', '=', 'Available')])
        hotels = request.env['hotel.register'].sudo().search(([]))
        context = {
            "user": user,
            "rooms": rooms,
            "hotels": hotels,
        }
        return request.render('Hotel_management_system.home', context)

    @http.route('/hotel_booking/register', type="http", auth="public", website=True)
    def register(self, **kw):
        if kw.get('name') and kw.get('login'):
            register_uid = request.env['res.users'].sudo().create(
                {
                    "name": kw['name'],
                    "login": kw['login'],
                    "password": kw['Password'],
                }
            )
            if register_uid:
                return request.redirect(f'/hotel_booking/home/{register_uid.id}')
            else:
                print("No registration")
        return request.render('Hotel_management_system.bookingRegister')

    @http.route('/hotel/Registration', type="http", auth="public", website=True)
    def hotel_register(self, **kw):
        hotels = request.env['hotel.register'].sudo().create(kw)
        return request.render('Hotel_management_system.HotelRegister')

    @http.route('/hotel/rooms/<int:userid>/<int:ids>', type="http", auth="public", website=True)
    def hotel_rooms(self, ids, userid, **kw):
        rooms = request.env['hotel.register'].sudo().browse(ids)
        today = date.today()
        print(today)
        context = {
            "rooms": rooms,
            "userid": userid,
            "today": today
        }
        return request.render('Hotel_management_system.rooms', context)

    @http.route('/room_booking', type="http", auth="public", website=True)
    def room_booking(self, **kw):
        user_id = kw.get('user')
        user=kw.get('userid')
        date = kw.get('date')
        print(date)
        room = request.env['hotel.room'].sudo().browse(int(kw.get('roomid')))
        room.Status = "Booked"
        room.contact = int(user)
        room.booking_date = date
        return request.redirect(f'/room_booking/Successfully/{room.id}')

    @http.route('/room_booking/my_booking', type="http", auth="user", website=True)
    def my_booking(self, **kw):
        booking = request.env['hotel.room'].search([('contact', '=', request.env.user.id)])
        return request.render('Hotel_management_system.MyBooking', {
            "booking": booking,
            "userid": request.env.user,
        })

    @http.route('/room_booking/Successfully/<int:id>', type="http", auth="user", website=True)
    def room_booking_successfully(self, id, **kw):
        room = request.env['hotel.room'].sudo().browse(int(id))
        print(room.booking_date)
        return request.render('Hotel_management_system.Conformation_page', {"room": room})
