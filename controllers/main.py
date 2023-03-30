from odoo import http
from odoo.http import request


class School(http.Controller):
    @http.route('/school', type='http', auth='public', website=True)
    def school_student(self, **kw):
        students = request.env['school.student'].sudo().search([])
        return request.render('aaa_school.student_page', {
            'Students': students
        })

class WebView2(http.Controller):
    # Render Form View
    @http.route('/add_new_student', auth='public', website=True)
    def hospital_patient_new(self, **kw):
        return request.render('aaa_school.add_new_student', {
        })

    # Redirect To  Patient Page
    @http.route('/my_form', auth='public', website=True)
    def hospital_patient_redirect(self, **kw):
        name = kw.get('name')
        email = kw.get('email')
        # age = kw.get('age')
        request.env['school.student'].create({
            'name': name,
            'email': email,
            # 'age': age,
        })
        redirect = '/school'
        return request.redirect(redirect)




