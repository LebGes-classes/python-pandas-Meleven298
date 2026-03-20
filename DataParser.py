import pandas as pd


class DateParser:
    '''Класс парсера дат.'''

    def sort_dates(self, df: pd.DataFrame) -> pd.DataFrame:
        '''Функция для сортировки дат.
        
        Args: 
            df: Pandas DataFrame, поступающий для сортировки.

        Returns:
            df_sorted: Pandas DataFrame, отсортированный df.
        '''

        date_columns = ['install_date', 'warranty_until', 'last_calibration_date', 'last_service_date']

        for col in date_columns:
            if col in df.columns:
                df[col] = pd.to_datetime(df[col], infer_datetime_format=True, format="mixed")

        df = df.sort_values('warranty_until', ascending=False)
        df = df.reset_index(drop=True)

        return df
    