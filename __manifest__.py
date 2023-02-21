# -*- coding: utf-8 -*-
{
    "name": "Tutorial Portal",
    "summary": """Portal""",
    "description": """
        Study material
    """,
    "author": "vyngt",
    "website": "https://github.com/vyngt/odoo-tutorial-portal",
    "category": "Services/Library",
    "version": "16.0.1.0.0",
    "depends": ["tutorial_checkout", "portal"],
    "data": [
        "security/ir.model.access.csv",
        "security/tutorial_security.xml",
        "views/main_templates.xml",
        "views/portal_templates.xml",
    ],
    "assets": {
        "web.assets_frontend": {
            "tutorial_portal/static/src/css/library.css",
        }
    },
    "demo": [],
}
