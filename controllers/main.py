# -*- coding: utf-8 -*-
from odoo import http


class Main(http.Controller):
    @http.route("/tutorial/library/catalog", auth="public", website=True)
    def catalog(self, **kw):
        Book = http.request.env["tutorial.library.book"]
        books = Book.sudo().search([])
        return http.request.render("tutorial_portal.book_catalog", {"books": books})
