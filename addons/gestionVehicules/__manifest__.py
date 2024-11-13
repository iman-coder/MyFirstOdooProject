{
    'name': 'Gestion de Projets de Construction',
    'version': '1.0.0',
    'sequence': -100,
    'author': '',
    'website': '',
    'category': 'Parc automobile',
    'summary': 'Gestion des vehicules de l entreprise INSEA ....',
    'description': 'Projet qui a pour but de digitaliser le proceessus d affectation des missions pour les chauffeurs et vehcules aussi pour l elaboration des contrat entre l entreprise INSEA et ses prestattaires qui geres tout ce qui est opérations de maintenances',
    'depends': ['base','hr','hr_contract','fleet','maintenance'],
    'data': [
        'views/employee_view.xml',
        'views/vehicule_view.xml',
        'views/project_view.xml',
        'views/product_view.xml',
        'security/ir.model.access.csv',
        
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
}