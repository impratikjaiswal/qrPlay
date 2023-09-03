from collections import OrderedDict


class MetaData:
    def __init__(self, raw_data_org):
        self.raw_data_org = raw_data_org
        self.parsed_data = None
        self.file_based = None
        self.output_file = None
        self.output_dic = OrderedDict()
