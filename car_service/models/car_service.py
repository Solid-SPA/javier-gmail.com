# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models




class CarService(models.Model):
    _name = 'carservice'
    _description = 'Servico de carros'

    name = fields.Char(
    	string='Nombre',
    	size=64,
    	required=True
    )
    precio = fields.Float(
        string='Tarifa',
    )