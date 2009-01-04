# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>). All Rights Reserved
#    $Id$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    "name" : "crm_profiling management",
    "version" : "1.3",
    "depends" : ["base", "crm"],
    "author" : "Tiny",
    "description": """
    This module allow users to perform segmentation within partners.
    It use the profiles criteria from the earlier segmentation module and improve it thanks to the new concept of questionnaire. You can now regroup questions into a questionnaire and directly use it on a partner.

    It also has been merged with the earlier CRM & SRM segmentation tool because they were overlapping.


    The menu items related are in "CRM & SRM\Configuration\Segmentations\"


    * Note: this module is not compatible with the module segmentation, since it's the same which has been renamed.
    """,
    "website" : "http://www.openerp.com",
    "category" : "Generic Modules/CRM & SRM",
    "init_xml" : [],
    "demo_xml" : ["crm_profiling_demo.xml"],
    "update_xml" : [
        "security/ir.model.access.csv",
        "crm_profiling_view.xml",
    ],
    "active": False,
    "installable": True
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

