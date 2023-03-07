# db = DAL('mysql://db_user:db_pass@localhost/taskdb', pool_size=1, check_reserved=['all'])
db = DAL("mysql://towhid:Gr0up#247@web2pydb1.mysql.database.azure.com:3306/taskdb", pool_size=10, migrate_enabled=True, migrate='runonly', check_reserved=['all'], fake_migrate=True)

db.define_table('tasks',
    Field('task_name', requires=IS_NOT_EMPTY()),
    Field('completed', 'boolean', default=False),
    Field('created_on', 'datetime', default=request.now),
)
