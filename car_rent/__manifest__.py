{
    'name': 'Car Rent',
    'depends': ['base'],
    'category': 'Car Rent/Brokerage',
    'data':[
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/car_rent_car_tag_data.xml',
        'data/car_rent_car_data.xml',
        'views/car_rent_car_views.xml',
        'views/car_rent_driver_views.xml',
        'views/car_rent_tag_views.xml',
        'views/res_partner_views.xml',
        'views/car_rent_menus.xml',
        
    ],
    'icon': 'static/description/icon_image.png',
    'installable': True,
    'application': True,
}