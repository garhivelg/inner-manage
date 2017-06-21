from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required


from . import admin
from .forms import DepartmentForm, RoleForm, EmployeeAssignForm
from .. import db
from ..models import Department, Role, Employee


def check_admin():
    """
    Prevent non-admin from accessing the page
    """
    if not current_user.is_admin:
        abort(403)


@admin.route('/departments', methods=['GET', 'POST'])
@login_required
def list_departments():
    """
    List all departments
    """
    check_admin()

    departments = Department.query.all()

    return render_template(
        'admin/departments.html',
        departments=departments,
        title="Departments"
    )


@admin.route('/departments/add', methods=['GET', 'POST'])
@login_required
def add_department():
    """
    Add a department to the database
    """
    check_admin()

    add_department = True

    form = DepartmentForm()
    if form.validate_on_submit():
        department = Department(
            name=form.name.data,
            description=form.description.data
        )
        try:
            db.session.add(department)
            db.session.commit()
            flash('You have successfully added a new department.')
        except:
            flash('Error: department name already exists.')
        return redirect(url_for('admin.list_departments'))

    return render_template(
        'admin/department.html',
        action="Add",
        add_department=add_department,
        form=form,
        title="Add Department"
    )


@admin.route('/departments/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_department(id):
    """
    Edit a department
    """
    check_admin()

    add_department = False

    department = Department.query.get_or_404(id)
    form = DepartmentForm()
    if form.validate_on_submit():
        department.name = form.name.data
        department.description = form.description.data
        db.session.add(department)
        db.session.commit()
        flash('You have successfully edited the department.')

        return redirect(url_for('admin.list_departments'))

    form.name.data = department.name
    form.description.data = department.description

    return render_template(
        'admin/department.html',
        action="Edit",
        add_department=add_department,
        form=form,
        title="Edit Department"
    )


@admin.route('/departments/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_department(id):
    """
    Delete a department from database
    """
    check_admin()

    department = Department.query.get_or_404(id)
    db.session.delete(department)
    db.session.commit()
    flash('You have successfully deleted the department.')

    return redirect(url_for('admin.list_departments'))


@admin.route('/roles', methods=['GET', 'POST'])
@login_required
def list_roles():
    """
    List all roles
    """
    check_admin()

    roles = Role.query.all()

    return render_template(
        'admin/roles.html',
        roles=roles,
        title="Roles"
    )


@admin.route('/roles/add', methods=['GET', 'POST'])
@login_required
def add_role():
    """
    Add a role to the database
    """
    check_admin()

    add_role = True

    form = RoleForm()
    if form.validate_on_submit():
        role = Role(
            name=form.name.data,
            description=form.description.data
        )
        try:
            db.session.add(role)
            db.session.commit()
            flash('You have successfully added a new role.')
        except:
            flash('Error: role name already exists.')
        return redirect(url_for('admin.list_roles'))

    return render_template(
        'admin/role.html',
        action="Add",
        add_role=add_role,
        form=form,
        title="Add Role"
    )


@admin.route('/roles/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_role(id):
    """
    Edit a role
    """
    check_admin()

    add_role = False

    role = Role.query.get_or_404(id)
    form = RoleForm(obj=role)
    if form.validate_on_submit():
        role.name = form.name.data
        role.description = form.description.data
        db.session.add(role)
        db.session.commit()
        flash('You have successfully edited the role.')

        return redirect(url_for('admin.list_roles'))

    form.name.data = role.name
    form.description.data = role.description

    return render_template(
        'admin/role.html',
        action="Edit",
        add_role=add_role,
        form=form,
        title="Edit Role"
    )


@admin.route('/roles/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_role(id):
    """
    Delete a role from database
    """
    check_admin()

    role = Role.query.get_or_404(id)
    db.session.delete(role)
    db.session.commit()
    flash('You have successfully deleted the role.')

    return redirect(url_for('admin.list_roles'))


@admin.route('/employees', methods=['GET', 'POST'])
@login_required
def list_employees():
    """
    List all employees
    """
    check_admin()

    employees = Employee.query.all()

    return render_template(
        'admin/employees.html',
        employees=employees,
        title="Employees"
    )


@admin.route('/employees/assign/<int:id>', methods=['GET', 'POST'])
@login_required
def assign_employee(id):
    """
    Assign a department and a roleto an  employee
    """
    check_admin()

    employee = Employee.query.get_or_404(id)

    if employee.is_admin:
        abort(403)

    form = EmployeeAssignForm()
    if form.validate_on_submit():
        employee.department = form.department.data
        employee.role = form.role.data
        db.session.add(employee)
        db.session.commit()
        flash('You have successfully assigned a department and role.')

        return redirect(url_for('admin.list_employees'))

    return render_template(
        'admin/role.html',
        employee=employee,
        form=form,
        title="Assign Employee"
    )
