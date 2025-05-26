from xmlrpc import client

url = 'http://localhost:8069'
db = 'odoo_training'
username = 'admin'
password = 'admin'

common = client.ServerProxy('{}/xmlrpc/2/common'.format(url))
print(common.version())

uid = common.authenticate(db, username, password, {})
print(uid)

models = client.ServerProxy('{}/xmlrpc/2/object'.format(url))

model_access = models.execute_kw(db, uid, password, 'sale.order', 'check_access_rights', ['write'], {'raise_exception': False})
print(model_access)

draft_quotes = models.execute_kw(db, uid, password, 'sale.order', 'search', [[['state', '=', 'draft']]])
print(draft_quotes)

if_confirmed = models.execute_kw(db, uid, password, 'sale.order', 'action_confirm', [draft_quotes])
print(if_confirmed)

# Vamos a la carpeta donde está el script y lo corremos python3 sale_script.py
# Debe imprimir algo como esto: {'server_version': '16.0+e', 'server_version_info': [16, 0, 0, 'final', 0, 'e'], 'server_serie': '16.0', 'protocol_version': 1}