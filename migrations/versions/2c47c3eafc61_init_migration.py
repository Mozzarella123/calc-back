"""Init migration.

Revision ID: 2c47c3eafc61
Revises: 
Create Date: 2020-07-21 18:45:03.122341

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2c47c3eafc61'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Categories',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('Order', sa.Integer(), nullable=False),
    sa.Column('Name', sa.Unicode(), nullable=True),
    sa.Column('Parent_Id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['Parent_Id'], ['Categories.Id'], ),
    sa.PrimaryKeyConstraint('Id')
    )
    op.create_index(op.f('ix_Categories_Parent_Id'), 'Categories', ['Parent_Id'], unique=False)
    op.create_table('ElementTypes',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('Name', sa.Unicode(), nullable=True),
    sa.Column('Category', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('Id')
    )
    op.create_table('MultiProjects',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('Name', sa.Unicode(), nullable=True),
    sa.PrimaryKeyConstraint('Id')
    )
    op.create_table('Parameters',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('Name', sa.Unicode(), nullable=True),
    sa.Column('Type', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('Id')
    )
    op.create_table('RoomTypes',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('Name', sa.Unicode(), nullable=True),
    sa.Column('GUID', sa.Unicode(), nullable=True),
    sa.Column('Image', sa.Binary(), nullable=True),
    sa.PrimaryKeyConstraint('Id')
    )
    op.create_table('Tags',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('Name', sa.Unicode(), nullable=True),
    sa.PrimaryKeyConstraint('Id')
    )
    op.create_table('Templates',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('Name', sa.Unicode(), nullable=True),
    sa.Column('Content', sa.Unicode(), nullable=True),
    sa.PrimaryKeyConstraint('Id')
    )
    op.create_table('Documents',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('Name', sa.Unicode(), nullable=False),
    sa.Column('Json', sa.Unicode(), nullable=False),
    sa.Column('DocumentType', sa.Integer(), nullable=False),
    sa.Column('DateCreated', sa.DateTime(), nullable=False),
    sa.Column('DateModified', sa.DateTime(), nullable=False),
    sa.Column('MultiProject_Id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['MultiProject_Id'], ['MultiProjects.Id'], ),
    sa.PrimaryKeyConstraint('Id')
    )
    op.create_index(op.f('ix_Documents_MultiProject_Id'), 'Documents', ['MultiProject_Id'], unique=False)
    op.create_table('Formulae',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('Expression', sa.Unicode(), nullable=True),
    sa.Column('Type', sa.Integer(), nullable=False),
    sa.Column('ElementType_Id', sa.Integer(), nullable=True),
    sa.Column('RoomType_Id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['ElementType_Id'], ['ElementTypes.Id'], ),
    sa.ForeignKeyConstraint(['RoomType_Id'], ['RoomTypes.Id'], ),
    sa.PrimaryKeyConstraint('Id')
    )
    op.create_index(op.f('ix_Formulae_ElementType_Id'), 'Formulae', ['ElementType_Id'], unique=False)
    op.create_index(op.f('ix_Formulae_RoomType_Id'), 'Formulae', ['RoomType_Id'], unique=False)
    op.create_table('TemplateBlocks',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('Name', sa.Unicode(), nullable=True),
    sa.Column('Content', sa.Unicode(), nullable=True),
    sa.Column('Order', sa.Integer(), nullable=False),
    sa.Column('TemplateBlockType', sa.Integer(), nullable=False),
    sa.Column('Template_Id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['Template_Id'], ['Templates.Id'], ),
    sa.PrimaryKeyConstraint('Id')
    )
    op.create_index(op.f('ix_TemplateBlocks_Template_Id'), 'TemplateBlocks', ['Template_Id'], unique=False)
    op.create_table('ParameterFormulas',
    sa.Column('Parameter_Id', sa.Integer(), nullable=False),
    sa.Column('Formula_Id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['Formula_Id'], ['Formulae.Id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['Parameter_Id'], ['Parameters.Id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('Parameter_Id', 'Formula_Id')
    )
    op.create_index(op.f('ix_ParameterFormulas_Formula_Id'), 'ParameterFormulas', ['Formula_Id'], unique=False)
    op.create_index(op.f('ix_ParameterFormulas_Parameter_Id'), 'ParameterFormulas', ['Parameter_Id'], unique=False)
    op.create_table('WorkTypes',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('GUID', sa.Unicode(), nullable=True),
    sa.Column('Name', sa.Unicode(), nullable=True),
    sa.Column('PriceValue', sa.Float(), nullable=False),
    sa.Column('Salary', sa.Float(), nullable=False),
    sa.Column('Time', sa.Float(), nullable=False),
    sa.Column('Order', sa.Integer(), nullable=False),
    sa.Column('Description', sa.Unicode(), nullable=True),
    sa.Column('MaterialsCount', sa.Unicode(), nullable=True),
    sa.Column('Formula_Id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['Formula_Id'], ['Formulae.Id'], ),
    sa.PrimaryKeyConstraint('Id')
    )
    op.create_index(op.f('ix_WorkTypes_Formula_Id'), 'WorkTypes', ['Formula_Id'], unique=False)
    op.create_table('MaterialTypes',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('Name', sa.Unicode(), nullable=True),
    sa.Column('GUID', sa.Unicode(), nullable=True),
    sa.Column('Unit', sa.Unicode(), nullable=True),
    sa.Column('Formula_Id', sa.Integer(), nullable=True),
    sa.Column('WorkType_Id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['Formula_Id'], ['Formulae.Id'], ),
    sa.ForeignKeyConstraint(['WorkType_Id'], ['WorkTypes.Id'], ),
    sa.PrimaryKeyConstraint('Id')
    )
    op.create_index(op.f('ix_MaterialTypes_Formula_Id'), 'MaterialTypes', ['Formula_Id'], unique=False)
    op.create_index(op.f('ix_MaterialTypes_WorkType_Id'), 'MaterialTypes', ['WorkType_Id'], unique=False)
    op.create_table('TagWorkTypes',
    sa.Column('Tag_Id', sa.Integer(), nullable=False),
    sa.Column('WorkType_Id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['Tag_Id'], ['Tags.Id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['WorkType_Id'], ['WorkTypes.Id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('Tag_Id', 'WorkType_Id')
    )
    op.create_index(op.f('ix_TagWorkTypes_Tag_Id'), 'TagWorkTypes', ['Tag_Id'], unique=False)
    op.create_index(op.f('ix_TagWorkTypes_WorkType_Id'), 'TagWorkTypes', ['WorkType_Id'], unique=False)
    op.create_table('WorkTypeCategories',
    sa.Column('WorkType_Id', sa.Integer(), nullable=False),
    sa.Column('Category_Id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['Category_Id'], ['Categories.Id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['WorkType_Id'], ['WorkTypes.Id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('WorkType_Id', 'Category_Id')
    )
    op.create_index(op.f('ix_WorkTypeCategories_Category_Id'), 'WorkTypeCategories', ['Category_Id'], unique=False)
    op.create_index(op.f('ix_WorkTypeCategories_WorkType_Id'), 'WorkTypeCategories', ['WorkType_Id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_WorkTypeCategories_WorkType_Id'), table_name='WorkTypeCategories')
    op.drop_index(op.f('ix_WorkTypeCategories_Category_Id'), table_name='WorkTypeCategories')
    op.drop_table('WorkTypeCategories')
    op.drop_index(op.f('ix_TagWorkTypes_WorkType_Id'), table_name='TagWorkTypes')
    op.drop_index(op.f('ix_TagWorkTypes_Tag_Id'), table_name='TagWorkTypes')
    op.drop_table('TagWorkTypes')
    op.drop_index(op.f('ix_MaterialTypes_WorkType_Id'), table_name='MaterialTypes')
    op.drop_index(op.f('ix_MaterialTypes_Formula_Id'), table_name='MaterialTypes')
    op.drop_table('MaterialTypes')
    op.drop_index(op.f('ix_WorkTypes_Formula_Id'), table_name='WorkTypes')
    op.drop_table('WorkTypes')
    op.drop_index(op.f('ix_ParameterFormulas_Parameter_Id'), table_name='ParameterFormulas')
    op.drop_index(op.f('ix_ParameterFormulas_Formula_Id'), table_name='ParameterFormulas')
    op.drop_table('ParameterFormulas')
    op.drop_index(op.f('ix_TemplateBlocks_Template_Id'), table_name='TemplateBlocks')
    op.drop_table('TemplateBlocks')
    op.drop_index(op.f('ix_Formulae_RoomType_Id'), table_name='Formulae')
    op.drop_index(op.f('ix_Formulae_ElementType_Id'), table_name='Formulae')
    op.drop_table('Formulae')
    op.drop_index(op.f('ix_Documents_MultiProject_Id'), table_name='Documents')
    op.drop_table('Documents')
    op.drop_table('Templates')
    op.drop_table('Tags')
    op.drop_table('RoomTypes')
    op.drop_table('Parameters')
    op.drop_table('MultiProjects')
    op.drop_table('ElementTypes')
    op.drop_index(op.f('ix_Categories_Parent_Id'), table_name='Categories')
    op.drop_table('Categories')
    # ### end Alembic commands ###