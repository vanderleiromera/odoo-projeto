{ 
    'name': "My library",
    'summary': "Manage books easily",
    'description': """Odoo development - My first App""", 
    'author': "Vanderlei", 
    'website': "http://www.paranstillus.com", 
    'category': 'Uncategorized', 
    'version': '12.0.1',
    'depends': ['base'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/library_book.xml'
    ],
}
