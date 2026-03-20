import pandas as pd


class PivotTable:
    '''Класс сводной таблицы'''

    def make_pivot_table(self, data_for_pivot: pd.DataFrame, column_for_pivot: str)  -> pd.DataFrame:
        '''Функция для создания сводной таблицы

        Args:
            data_for_pivot: Датафрейм для создания сводной таблицы.
            column_for_pivot: Колонка по которой будут делаться столбцы сводной таблицы.

        Returns:
            pivot_table: Сводная таблица.
        '''

        categories = pd.cut(
            data_for_pivot[column_for_pivot],
            bins=[-float('inf'), -100, -30, 0, 30, 100, float('inf')],
            labels=['Уже была (>100 дн)', 'Уже была (30-100 дн)', 
                    'Уже была (<30 дн)', 'Сегодня-30 дн', '30-100 дн', '>100 дн']
        )

        pivot_table = pd.pivot_table(
            data_for_pivot,
            values='device_id',
            index='clinic_id',
            columns=categories,
            aggfunc=lambda x: ', '.join(map(str, x)),
            fill_value=''
        )
        
        issues_sum = data_for_pivot.groupby('clinic_id')['issues_reported_12mo'].sum()
        pivot_table['total_issues_12mo'] = issues_sum
        
        return pivot_table
    