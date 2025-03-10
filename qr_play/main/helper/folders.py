import os

from python_helpers.ph_util import PhUtil

from qr_play import PACKAGE_NAME


class Folders:
    top_folder_path = [os.pardir, os.pardir]

    DIR_DATA = 1

    DIR_USER_DATA = 2
    DIR_USER_DATA_GENERIC = 24

    DIR_SAMPLE_DATA = 3
    DIR_SAMPLE_DATA_GENERIC = 34

    DIR_TEST = 9
    DIR_TEST_LOGS = 91

    DIR_PJ_EXCLUSIVE = 999

    LOCATIONS_MAPPING = {
        #
        DIR_DATA: ['data'],
        #
        DIR_SAMPLE_DATA: ['data', 'sample_data'],
        DIR_SAMPLE_DATA_GENERIC: ['data', 'sample_data', 'Generic'],
        #
        DIR_USER_DATA: ['data', 'user_data'],
        DIR_USER_DATA_GENERIC: ['data', 'user_data', 'Generic'],
        #
        DIR_TEST: [PACKAGE_NAME, 'test'],
        DIR_TEST_LOGS: [PACKAGE_NAME, 'test', 'logs'],
        #
        DIR_PJ_EXCLUSIVE: ['data', 'pj_exclusive'],
    }

    @classmethod
    def in_test(cls, relative_path=''):
        return cls.__get_path(Folders.DIR_TEST, relative_path)

    @classmethod
    def in_test_logs(cls, relative_path=''):
        return cls.__get_path(Folders.DIR_TEST_LOGS, relative_path)

    @classmethod
    def in_sample(cls, relative_path=''):
        return cls.__get_path(Folders.DIR_SAMPLE_DATA, relative_path)

    @classmethod
    def in_sample_gen(cls, relative_path=''):
        return cls.__get_path(Folders.DIR_SAMPLE_DATA_GENERIC, relative_path)

    @classmethod
    def in_user(cls, relative_path=''):
        return cls.__get_path(Folders.DIR_USER_DATA, relative_path)

    @classmethod
    def in_user_gen(cls, relative_path=''):
        return cls.__get_path(Folders.DIR_USER_DATA_GENERIC, relative_path)

    @classmethod
    def in_pj_exclusive(cls, relative_path=''):
        return cls.__get_path(Folders.DIR_PJ_EXCLUSIVE, relative_path)

    @classmethod
    def __get_path(cls, folder_name, relative_path):
        """

        :param folder_name:
        :param relative_path: str or list
        :return:
        """
        if folder_name not in cls.LOCATIONS_MAPPING:
            raise ValueError('Unknown Folder name')
        return os.sep.join(
            filter(None, PhUtil.normalise_list(
                [Folders.top_folder_path, cls.LOCATIONS_MAPPING.get(folder_name), relative_path])))
