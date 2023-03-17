from unittest import TestCase
from apps.loader.core.orchestrator import ServiceOrchestrator
from abc import abstractclassmethod
from os.path import dirname, join
from os import listdir
from werkzeug.datastructures import FileStorage
from pandas import read_csv
from apps.loader.core.rule_process import RuleProcess
import numpy as np


class BaseTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.print_test_info()
        cls.set_up_class()

    @classmethod
    def tearDownClass(cls):
        cls.close_input_files()

    def setUp(self) -> None:
        r = {
            "uuid": "a3b1e556-0044-4501-973f-3bebc730bdf2",
            "slug": "service",
            "version": 1,
            "steps": [
                    {
                        'component': 'formatter',
                        'alias': 'service.formatter',
                        'active': True,
                    },
                {
                        'component': 'reader',
                        'alias': 'service.reader',
                        'active': True
                        },
                {
                        'component': 'client',
                        'alias': 'service.client',
                        'active': True,
                        'steps': [
                            {
                                'service_name': 'items',
                                'method': 'get',
                                'uri': '${MELI_ITEMS_API}?ids=:[ids]&attributes=id,price,start_time,category_id,currency_id,seller_id',
                                'include_row': False,
                                'headers': [],
                                'placeholders': [
                                    {
                                        'name': 'id',
                                        'path': '$data.body.id'
                                    },
                                    {
                                        'name': 'price',
                                        'path': '$data.body.price'
                                    },
                                    {
                                        'name': 'start_time',
                                        'path': '$data.body.start_time'
                                    },
                                    {
                                        'name': 'category_id',
                                        'path': '$data.body.category_id'
                                    },
                                    {
                                        'name': 'currency_id',
                                        'path': '$data.body.currency_id'
                                    },
                                    {
                                        'name': 'seller_id',
                                        'path': '$data.body.seller_id'
                                    },
                                ],
                                'steps': [
                                    {
                                        'service_name': 'categories',
                                        'method': 'get',
                                        'uri': '${MELI_CATEGORIES_API}/:[category_id]?attributes=name',
                                        'headers': [],
                                        'placeholders': [
                                            {
                                                'name': 'name',
                                                'path': '$data.name'
                                            }
                                        ]
                                    },
                                    {
                                        'service_name': 'currencies',
                                        'method': 'get',
                                        'uri': '${MELI_CURRENCIES_API}/:[currency_id]?attributes=description',
                                        'headers': [],
                                        'placeholders': [
                                            {
                                                'name': 'description',
                                                'path': '$data.description'
                                            }
                                        ]
                                    },
                                    {
                                        'service_name': 'users',
                                        'method': 'get',
                                        'uri': '${MELI_USERS_API}/:[seller_id]?attributes=nickname',
                                        'headers': [],
                                        'placeholders': [
                                            {
                                                'name': 'nickname',
                                                'path': '$data.nickname'
                                            }
                                        ]
                                    },
                                ]
                            }
                        ]
                        },
            ]
        }

        self.rule = RuleProcess(r).rule

        self.component = [
            step
            for step in self.rule['steps']
            if step['component'] == self.component_name
        ][0]

        self.set_service()

    @property
    def component_name(self):
        """
        Property intended for set up a component of a test
        """
        pass

    @property
    def service_class(self):
        """
        Property intended for set up a service class of a test
        """
        pass

    def set_service(self):
        o = ServiceOrchestrator(
            rule=self.rule,
            base_data=None
        )
        self.service = self.service_class(
            alias=self.component['alias'],
            orchestrator=o
        )

    @abstractclassmethod
    def set_up_class(cls):
        """
        Method intended for specific setting up a test
        """
        pass

    @classmethod
    def print_test_info(cls):
        print('----------------------------------------------------------------------')
        print(cls.test_name)
        print('----------------------------------------------------------------------')

    @classmethod
    def read_input_files(cls):
        """Loads files in input folder
        ### Parameters
        `path: str`
        """

        path = join(dirname(__file__), 'input')
        files = [
            filename
            for filename in listdir(path)
        ]
        cls.files = {
            file.split('.')[0]: FileStorage(
                open(join(dirname(__file__), 'input', file), mode='rb'))
            for file in files
        }

    @classmethod
    def load_test_dataframe(cls):
        with open(join(dirname(__file__), 'input', 'test_txt.txt')) as f:
            cls.df = read_csv(f, dtype=np.str_)

        cls.df['ids'] = cls.df['id'] + cls.df['site']

    @classmethod
    def close_input_files(cls):
        for file in cls.files:
            cls.files[file].close()
