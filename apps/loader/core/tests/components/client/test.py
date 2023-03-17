# from apps.loader.core.tests.base_test import BaseTest
# from apps.loader.core.components.client.service import Service
# from apps.common.models.records import Record
# from apps.api import db
# from apps.api import create_app

# app = create_app('testing')


# class TestClient(BaseTest):
#     test_name = 'Client tests'

#     @classmethod
#     def set_up_class(cls):
#         cls.load_test_dataframe()
#         # Clean database class method
#         with app.app_context():
#             db.create_all()

#     @classmethod
#     def tearDownClass(cls):
#         # with app.app_context():
#         #     db.session.query(Record).filter().delete()
#         pass


#     def setUp(self) -> None:
#         super().setUp()
#         self.service.orchestrator.payload['service.reader'] = {
#             'data': self.df
#         }
#         self.service.setup(
#             steps=self.component['steps']
#         )


#     @property
#     def component_name(self):
#         return 'client'

#     @property
#     def service_class(self):
#         return Service

#     def test_new_records(self):
#         with app.app_context():
#             self.service.run()
#             records = db.session.query(Record).all()
#         assert records
#         assert len(records) == 10
#         assert True

