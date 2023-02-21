from odoo import http
from odoo.addons.portal.controllers import portal
import logging

_logger = logging.getLogger(__name__)


class CustomerPortal(portal.CustomerPortal):
    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        if "book_checkout_count" in counters:
            count = http.request.env["tutorial.library.checkout"].search_count([])
            values["book_checkout_count"] = count

        return values

    @http.route(
        "/my/book-checkout/<model('tutorial.library.checkout'):doc>",
        auth="user",
        website=True,
    )
    def book_detail(self, doc="", **kwargs):
        _logger.info(f"Hello: {doc}")
        return http.request.render("tutorial_portal.book_checkout", {"doc": doc})

    @http.route(
        ["/my/book-checkouts", "/my/book-checkouts/page/<int:page>"],
        auth="user",
        website=True,
    )
    def book_checkout(self, page=1, **kwargs):
        Checkout = http.request.env["tutorial.library.checkout"]
        domain = []
        checkout_count = Checkout.search_count(domain)
        pager_data = portal.pager(
            url="/my/book-checkouts",
            total=checkout_count,
            page=page,
            step=self._items_per_page,
        )
        # Recordset according to pager and domain filter
        checkouts = Checkout.search(
            domain, limit=self._items_per_page, offset=pager_data["offset"]
        )
        _logger.info(checkouts)
        # Prepare template values
        values = self._prepare_portal_layout_values()
        values.update(
            {
                "checkouts": checkouts,
                "page_name": "book-checkouts",
                "default_url": "/my/book-checkouts",
                "pager": pager_data,
            }
        )
        return http.request.render("tutorial_portal.my_book_checkouts", values)
