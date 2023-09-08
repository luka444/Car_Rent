{
    'name': 'Car Rent',
    'depends': ['base'],
    'category': 'Car Rent/Brokerage',
    'data':[
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/car_rent_car_data.xml',
        'views/car_rent_car_views.xml',
        'views/car_rent_driver_views.xml',
        'views/car_category_views.xml',
        'views/car_mark_views.xml',
        'views/car_rent_order_views.xml',
        'views/res_partner_views.xml',
        'views/car_rent_menus.xml',
        'reports/car_rent_car_report.xml',
        'reports/rent_cars_templates.xml',
        
    ],
    'icon': 'car_rent/static/icon_image.png',
    'installable': True,
    'application': True,
}