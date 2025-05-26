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

model_access = models.execute_kw(db, uid, password, 'academy.session', 'check_access_rights', ['write'], {'raise_exception': False})
print(model_access)

courses = models.execute_kw(db, uid, password, 'academy.course', 'search_read', [[['level', 'in', ['intermediate', 'beginner'] ]]])
print(courses)
print('===================')
course = models.execute_kw(db, uid, password, 'academy.course', 'search_read', [[['name', '=', 'ERP 101']]])
print('Course:::: ',course)
print('===================')
session_fields = models.execute_kw(db, uid, password, 'academy.course', 'fields_get', [], {'attributes': ['string', 'type', 'required']})
print(session_fields)

print('====New Session ======')
new_session = models.execute(db, uid, password,
                             'academy.session', 'create',
                             [
                                 {'course_id': course[0]['id'],
                                  'duration': 5,
                                  'instructor_id': 1,
                                 }
                             ]
                             )
print(new_session)