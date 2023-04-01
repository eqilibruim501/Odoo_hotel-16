{
    'name': 'Hotel booking Management',
    'author': 'surekhatech',
    'description': 'Management of Hotel Room Booking.',

    'website': 'mycompany@gmail.com',
    'summary': 'Hotel Room Booking System',

    'version': '16.0.1.0.0',

    'depends': ['base', 'website'],

    'data': [
        'security/ir.model.access.csv',
        'views/Register_users_views.xml',
        'views/index_template.xml',
        'views/login_template.xml',
        'views/Register_template.xml',
        'views/home_template.xml',
        'views/Hotel_Register_views.xml',
        'views/Room_views.xml',
        'views/hotel_register_template.xml',
        'views/hotel_rooms_template.xml',
        'views/Conformation_page_template.xml',
        'views/my_booking_template.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'Hotel_management_system/static/src/js/Submit_handle.js',
        ],
    },

}
