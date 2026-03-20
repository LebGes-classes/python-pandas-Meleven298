import pandas as pd


class ReadingExcel:
    '''Класс чтения.'''

    def reading_excel(self, data: str) -> pd.DataFrame:
        '''Функция чтения иксель файлов.
        
        Args:
            data: Файл, который нужно прочитать.
            
        Returns:
            df: pandas.DatFrame'''

        df = pd.read_excel(data, engine='openpyxl')

        return df
    