import openpyxl
import pandas as pd


class WritingExcel:
    '''Класс записи в Excel.'''

    def __init__(self, filename: str) -> None:
        '''Инициализатор класса WritingExcel.'''

        self.sheet = 2
        self.filename = filename

    def write_to_excel(self, data: pd.DataFrame):
        '''Функция чтения записи в иксель файл.
        
        Args: 
            data: Данные, которые нужно занести в иксель файл.
        '''

        with pd.ExcelWriter(self.filename, mode='a', engine='openpyxl', if_sheet_exists='new') as writer:
            data.to_excel(writer, sheet_name=f'Sheet{self.sheet}', index=True)

        print(f'Данные размещены в файле {self.filename} на странице {self.sheet}')

        self.sheet +=1 
    