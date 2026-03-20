import pandas as pd


class DataMerging:
    '''Класс слияния датафреймов.'''

    def merge_data(self, left_data: pd.DataFrame, right_data: pd.DataFrame) -> pd.DataFrame:
        '''Функция для слияния данных.
        
        Args:
            left_data: Левый датафрейм.
            right_data: Правый датафрейм.
            
        Returns:
            merged_data: Конкатенированный датафрейм.
        '''

        merged_data = pd.merge(left=left_data, right=right_data, how='left')

        return merged_data

    def concat_data(self, data1: pd.DataFrame, data2: pd.DataFrame) -> pd.DataFrame:
        '''Функция для конкатенации данных.
        
        Args:
            data1: Первый датафрейм.
            data2: Второй датафрейм.
            
        Returns:
            concat_data: Конкатенированный датафрейм.
        '''

        concat_data = pd.concat([data1, data2])

        return concat_data
    