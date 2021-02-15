import unittest

from app import app, db
from app import DiagnosisCodeModel


class TestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///diagnosis"
        db.create_all()

    def tearDown(self):
        db.drop_all()

    def test_main_page(self):
        response = app.test_client().get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_get_diagnosis_codes(self):
        c = app.test_client().get('/dg_code', data={'cat_code': '001', 'dg_code': '4', 'full_code': '0014',
                                                    'abb_des': 'Malaria symptoms',
                                                    'full_des': 'malaria symptoms among others',
                                                    'title': 'Malaria'})
        self.assertTrue(c)

    def test_db_response(self):
        # create a Diagnosis record
        d = DiagnosisCodeModel(cat_code='', dg_code='', full_code='', abb_des='', full_des='', title='')
        # assert

    def test_db(self):
        db_ = db
        assert db_ is db


if __name__ == '__main__':
    unittest.main()
