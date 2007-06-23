from osv import fields,osv

class report_per_seller_customer(osv.osv):
        _name = "report.per.seller.customer"
        _description = "Customer per seller"
        _auto = False
        _columns = {
                    'name': fields.char('Depositer Inventory', size=64, required=True),
                    'partner_id': fields.many2one('res.partner', 'Seller',relate=True, required=True, change_default=True),
        }
        def init(self, cr):
            cr.execute("""
                create or replace view report_per_seller_customer as (
                    SELECT
                        l.id as id,
                        l.name as name,
                        l.partner_id as partner_id
                    from auction_deposit l
                  )""")
report_per_seller_customer()

class report_latest_doposit(osv.osv):
        _name = "report.latest.doposit"
        _description = "Latest 10 Deposits"
        _auto = False
        _columns = {
            'name': fields.char('Depositer Inventory', size=64, required=True),
            'partner_id': fields.many2one('res.partner', 'Seller', required=True, change_default=True),
            'date_dep': fields.date('Deposit date', required=True),
            'method': fields.selection((('keep','Keep until sold'),('decease','Decrease limit of 10%'),('contact','Contact the Seller')), 'Withdrawned method', required=True),
            'tax_id': fields.many2one('account.tax', 'Expenses'),
            'info': fields.char('Description', size=64),
            'lot_id': fields.one2many('auction.lots', 'bord_vnd_id', 'Objects'),
            'specific_cost_ids': fields.one2many('auction.deposit.cost', 'deposit_id', 'Specific Costs'),
            'total_neg': fields.boolean('Allow Negative Amount'),
            'user_id':fields.many2one('res.users', 'User', select=True),
        }
        def init(self, cr):
            cr.execute("""
                create or replace view report_latest_doposit as (
                    SELECT
                       l.id as id,
                       l.create_uid as user_id,
                       l.name as name,
                       l.partner_id as partner_id,
                       l.date_dep as date_dep,
                       l.method as method,
                       l.tax_id as tax_id,
                       l.info as info

                   from auction_deposit l
                   order by l.create_date desc
                   limit 3

                  )""")
report_latest_doposit()

class report_latest_objects(osv.osv):
        _name = "report.latest.objects"
        _description = "Latest 10 Objects"
        _auto = False
        _columns = {
                'partner_id': fields.many2one('res.partner', 'Seller', required=True, change_default=True),
                'auction_id': fields.many2one('auction.dates', 'Auction Date'),
                'bord_vnd_id': fields.many2one('auction.deposit', 'Depositer Inventory', required=True),
                'obj_desc': fields.text('Object Description'),
                'obj_num': fields.integer('Catalog Number'),
                'obj_ret': fields.float('Price retired'),
                'obj_comm': fields.boolean('Commission'),
                'obj_price': fields.float('Adjudication price'),
                'user_id':fields.many2one('res.users', 'User',  select=True),
        }
        def init(self, cr):
            cr.execute("""
                create or replace view report_latest_objects as (
                    SELECT
                       l.id as id,
                       l.bord_vnd_id as bord_vnd_id,
                       l.create_uid as user_id,
                       l.auction_id as auction_id,
                       l.obj_desc as obj_desc,
                       l.obj_num as obj_num,
                       l.obj_ret as obj_ret,
                       l.obj_comm as obj_comm,
                       l.obj_price as obj_price

                   from auction_lots l
                   order by l.create_date desc
                   limit 3

                  )""")
report_latest_objects()
def _type_get(self, cr, uid,ids):
    cr.execute('select name, name from auction_lot_category order by name')
    return cr.fetchall()
class report_auction_object_date(osv.osv):
    _name = "report.auction.object.date"
    _description = "Objects per day"
    _auto = False
    _columns = {
            'auction_id': fields.many2one('auction.dates', 'Auction Date'),
            'bord_vnd_id': fields.many2one('auction.deposit', 'Depositer Inventory', required=True),
            'name': fields.char('Short Description',size=64, required=True),
            'lot_type': fields.selection(_type_get, 'Object Type', size=64),
            'obj_desc': fields.text('Object Description'),
            'obj_num': fields.integer('Catalog Number'),
            'obj_ret': fields.float('Price retired'),
            'obj_comm': fields.boolean('Commission'),
            'obj_price': fields.float('Adjudication price'),
            'state': fields.selection((('draft','Draft'),('unsold','Unsold'),('paid','Paid'),('invoiced','Invoiced')),'State', required=True, readonly=True),
            'date':fields.date('Date', readonly=True),
            'lot_num': fields.integer('Quantity', required=True),
    }

    def init(self, cr):
        cr.execute("""
            create or replace view report_auction_object_date as (
                select
                    min(l.id) as id,
                    substring(l.create_date for 10) as date,
                    l.name as name,
                    sum(l.lot_num) as lot_num,
                    l.lot_type as lot_type,
                    l.state as state

                from
                    auction_lots l
                group by
                    l.create_date,l.name,l.obj_desc,lot_type,state
            )
        """)
report_auction_object_date()
