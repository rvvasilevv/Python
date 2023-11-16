import gspread
from module.modules.file_handler import FileHandler
from oauth2client.service_account import ServiceAccountCredentials


class UpdateGSheet:
    """
    Writes JSON data into Google Sheets
    """

    MAIN_SPREADSHEET_TITLE = "Hub"
    MAX_NUMBER_OF_COLUMNS = 15
    SCOPE = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    RANGE_TO_CLEAR = 'A7:H35'
    FIRST_AVAILABLE_ROW = 7

    def __init__(self, spreadsheet_title, credentials_file, sorted_book_data_json, args, num_of_rows):
        """
        Takes in the title for the spreadsheet and the
        credentials file needed for authentication
        :param spreadsheet_title: Title of the Google Sheets spreadsheet used for the project
        :param credentials_file: File path to credentials JSON file
        :param sorted_book_data_json: List of tuples containing a json file string, predicate and order
        :param args: arguments used for the json results
        :param num_of_rows: number of rows needed for the file
        """
        self._gc = self._authorize_gspread(credentials_file)
        self._spreadsheet = self._open_spreadsheet(spreadsheet_title)
        self._clear_previous_data()
        self.__current_worksheet_counter = 0
        self.__first_row_to_insert_data_to = self.FIRST_AVAILABLE_ROW
        self._upload_json_to_google_sheets(sorted_book_data_json, args, num_of_rows)

    def _upload_json_to_google_sheets(self, sorted_book_data_json, args, num_of_rows):
        """
        Uploads the JSON data to Google Sheets in the
        expected spreadsheet format
        :param sorted_book_data_json: list of tuples
        :param args: dictionary
        :param num_of_rows: int
        :return:
        """
        for json_data, sort_predicate, sort_order in sorted_book_data_json:
            sheet_title = self._add_result_to_main_worksheet(args, sort_predicate, sort_order)
            json_data = FileHandler.json_load(json_data)

            data_to_insert = self._create_data_to_insert_in_the_sheet(json_data)
            worksheet = self._spreadsheet.add_worksheet(title=sheet_title, rows=num_of_rows,
                                                         cols=self.MAX_NUMBER_OF_COLUMNS)

            worksheet.update(data_to_insert)
            print(f"Data successfully uploaded to {sheet_title} sheet.")
        return None

    def _add_result_to_main_worksheet(self, args, sort_predicate, sort_order):
        """
        Updates the main worksheet with the name of the new created sheet
        and the filters used in order to obtain those results.
        :param args: dictionary
        :param sort_predicate: str
        :param sort_order: str
        :return: str
        """
        hub_worksheet = self._spreadsheet.worksheet(self.MAIN_SPREADSHEET_TITLE)
        sort_predicate = sort_predicate or "default"
        sort_order = sort_order or "ascending"
        args['sorting_criteria'] = f"{sort_predicate} {sort_order}"

        used_arguments_string = ', '.join([f"{key}:{value}" for key, value in args.items() if value is not None])
        worksheet_title_string = f"Results{self.__current_worksheet_counter}"
        hub_worksheet.update(f'A{self.__first_row_to_insert_data_to}', worksheet_title_string)
        hub_worksheet.update(f'B{self.__first_row_to_insert_data_to}', used_arguments_string)
        self.__current_worksheet_counter += 1
        self.__first_row_to_insert_data_to += 1
        return worksheet_title_string

    def _clear_previous_data(self):
        """
        Deletes all the spreadsheets holding
        data from previous usages of the class.
        Does not delete the main sheet but clears the data inside of it.
        :return:
        """
        worksheet_list = self._spreadsheet.worksheets()
        for worksheet in worksheet_list:
            if worksheet.title != self.MAIN_SPREADSHEET_TITLE:
                self._spreadsheet.del_worksheet(worksheet)

        self._spreadsheet.values_clear(range=self.RANGE_TO_CLEAR)
        return None

    def _authorize_gspread(self, credentials_file):
        """
        Responsible for going through the authorization
        process necessary in to upload the data to
        Google Sheets.
        :param credentials_file: dictionary
        :return: gspread.client.Client
        """
        credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, self.SCOPE)
        return gspread.authorize(credentials)

    @staticmethod
    def _create_data_to_insert_in_the_sheet(json_data):
        """
        Takes the book data as JSON and
        creates a spreadsheet from it
        :param json_data: str
        :return: list
        """
        headers = list(json_data[0].keys())

        product_info_keys = set()
        for data_row in json_data:
            product_info = data_row.get("product_info")
            if product_info:
                product_info_keys.update(product_info.keys())

        headers_without_product_info = [header for header in headers if header != "product_info"]
        headers_to_insert = [header.title() for header in headers_without_product_info] + sorted(product_info_keys)
        data_to_insert = [headers_to_insert]

        for data_row in json_data:
            row_values = [str(data_row.get(header, "")).strip() for header in headers_without_product_info]

            product_info = data_row.get("product_info")
            if product_info:
                for key in sorted(product_info_keys):
                    row_values.append(str(product_info.get(key, "")).strip())
            data_to_insert.append(row_values)

        return data_to_insert

    def _open_spreadsheet(self, spreadsheet_title):
        """
        Attempts to open a spreadsheet for writing
        :param spreadsheet_title: str
        :return:
        """
        try:
            return self._gc.open(spreadsheet_title)
        except gspread.exceptions.SpreadsheetNotFound as e:
            print(f"Spreadsheet '{spreadsheet_title} not found {str(e)}")
            return None
