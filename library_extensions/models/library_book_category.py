from odoo import models, fields

class LibraryBookCategory(models.Model):
    _name = 'library.book.category'
    _description = 'book category'

    name = fields.Char(string='Name', required=True, unique=True)

