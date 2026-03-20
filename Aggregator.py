import pandas as pd


class Aggregator:
    '''Класс аггрегатора данными.'''

    def sort_by_groups(self, df: pd.DataFrame) -> pd.DataFrame:
        '''Функция для сортировки по группам.

        Args:
            df: Pandas DataFrame, поступающий для сортировки.

        Returns:
            Сгруппировонный в нужном порядке df.
        '''

        df = df[['clinic_id', 'device_id', 'issues_reported_12mo', 'issues_text', 'failure_count_12mo']]

        df.sort_values(by='issues_reported_12mo', ascending=False)

        return df
    