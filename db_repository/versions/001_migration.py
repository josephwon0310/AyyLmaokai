from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('email', String(length=50)),
    Column('league_name', String(length=25)),
    Column('rank', Integer),
    Column('password', String(length=256)),
    Column('looking_for_lower', Boolean),
    Column('looking_for_equal', Boolean),
    Column('looking_for_greater', Boolean),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['user'].columns['looking_for_equal'].create()
    post_meta.tables['user'].columns['looking_for_greater'].create()
    post_meta.tables['user'].columns['looking_for_lower'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['user'].columns['looking_for_equal'].drop()
    post_meta.tables['user'].columns['looking_for_greater'].drop()
    post_meta.tables['user'].columns['looking_for_lower'].drop()
