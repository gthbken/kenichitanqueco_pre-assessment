from odoo import models, fields, api

class LibraryBook(models.Model):

    _name = "library.book"
    _description = "Book"
    _order = "name"


    name = fields.Char(string="Name",
                       required=True)
    isbn_13 = fields.Char(string="ISBN 13",
                          required=True)
    author_id = fields.Many2one('res.partner', string="Author", required=True)
    category_id = fields.Many2many(comodel_name="library.book.category", string="Categories")


