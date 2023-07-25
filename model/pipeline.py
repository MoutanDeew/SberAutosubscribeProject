import datetime

import dill
import numpy as np
import pandas as pd

from sklearn.model_selection import cross_val_score
#from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import OneHotEncoder, FunctionTransformer, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
#from sklearn.svm import SVC


#from sklearn.svm import SVC


# def new_feature(df_merged):
#     event_action_list = ['sub_car_claim_click'
#                          'sub_car_claim_submit_click',
#                          'sub_open_dialog_click',
#                          'sub_custom_question_submit_click',
#                          'sub_call_number_click',
#                          'sub_callback_submit_click',
#                          'sub_submit_success',
#                          'sub_car_request_submit_click']
#
#     df_merged['target'] = df_merged.apply(
#         lambda x: 1 if x.event_action in event_action_list else 0, axis=1)
#     df_merged['russia_or_not'] = df_merged.apply(
#         lambda x: 1 if x.geo_country == "Russia" else 0, axis=1)
#     df_merged['utm_keyword_0_1'] = df_merged.apply(
#         lambda x: 0 if x.utm_keyword == "puhZPIYqKXeFPaUviSjo" else 1, axis=1)
#     df_merged['utm_source_0_1'] = df_merged.apply(
#         lambda x: 1 if x.utm_source == "ZpYIoDJMcFzVoPFsHGJL" else 0, axis=1)
#     df_merged['utm_medium_0_1'] = df_merged.apply(
#         lambda x: 0 if x.utm_medium == "banner" else 1, axis=1)
#     df_merged['utm_campaign_0_1'] = df_merged.apply(
#         lambda x: 0 if x.utm_campaign == "LEoPHuyFvzoNfnzGgfcd" else 1, axis=1)
#     df_merged['utm_adcontent_0_1'] = df_merged.apply(
#         lambda x: 1 if x.utm_adcontent == "JNHcPlZPxEMWDnRiyoBf" else 0, axis=1)
#     df_merged['device_os_0_1'] = df_merged.apply(
#         lambda x: 1 if x.device_os == "Android" else 0, axis=1)
#     df_merged['device_brand_0_1'] = df_merged.apply(
#         lambda x: 1 if x.device_brand == "Samsung" else 0, axis=1)
#     df_merged['device_screen_resolution_0_1'] = df_merged.apply(
#         lambda x: 0 if x.device_screen_resolution == "393x851" else 1, axis=1)
#     df_merged['device_category_0_1'] = df_merged.apply(
#         lambda x: 1 if x.device_category == "mobile" else 0, axis=1)
#     df_merged['device_browser_0_1'] = df_merged.apply(
#         lambda x: 1 if x.device_browser == "Chrome" else 0, axis=1)
#
#     return df_merged


# def ohe_feature(df_merged):
#     city_list = ['geo_city', 'utm_medium', 'device_category', 'device_os', 'device_browser']
#     ohe = OneHotEncoder(sparse=False)
#     for i in city_list:
#         ohe.fit(df_merged[[i]])
#         ohe_column = ohe.transform(df_merged[[i]])
#         df_merged[ohe.get_feature_names()] = ohe_column
#
#     return  df_merged


def column_astype(df):

    df = df.astype(np.int32)

    return df


# def filter_data(df_merged):
#     df_merged_copy = df_merged.copy()
#     columns_to_drop = [
#         'session_id',
#         'hit_date',
#         'hit_time',
#         'hit_number',
#         'hit_type',
#         'hit_referer',
#         'hit_page_path',
#         'event_category',
#         'event_action',
#         'event_label',
#         'event_value',
#         'client_id',
#         'visit_date',
#         'visit_time',
#         'visit_number',
#         'device_model'
#     ]
#     df_merged_copy.drop(columns_to_drop, axis=1)

    # return df_merged_copy


# def ohe_feature(df_merged_copy):
#     ohe = OneHotEncoder(sparse=False)
#     ohe.fit(df_merged_copy[['geo_city']])
#     ohe_city = ohe.transform(df_merged_copy[['geo_city']])
#     df_merged_copy[ohe.get_feature_names()] = ohe_city
#
#     ohe.fit(df_merged_copy[['utm_medium']])
#     ohe_utm_medium = ohe.transform(df_merged_copy[['utm_medium']])
#     ohe.get_feature_names()
#     df_merged_copy[ohe.get_feature_names()] = ohe_utm_medium
#
#     ohe.fit(df_merged_copy[['device_category']])
#     ohe_device_category = ohe.transform(df_merged_copy[['device_category']])
#     ohe.get_feature_names()
#     df_merged_copy[ohe.get_feature_names()] = ohe_device_category
#
#     ohe.fit(df_merged_copy[['device_os']])
#     ohe_device_os = ohe.transform(df_merged_copy[['device_os']])
#     ohe.get_feature_names()
#     df_merged_copy[ohe.get_feature_names()] = ohe_device_os
#
#     ohe.fit(df_merged_copy[['device_browser']])
#     ohe_device_browser = ohe.transform(df_merged_copy[['device_browser']])
#     ohe.get_feature_names()
#     df_merged_copy[ohe.get_feature_names()] = ohe_device_browser


def main():
    df_merged = pd.read_csv('../data/df_1', low_memory=False)

    df_merged_1 = df_merged.iloc[0:522840]
    df_merged_2 = df_merged.iloc[522840:1045680]
    df_merged_3 = df_merged.iloc[1045680:1568520]
    df_merged_4 = df_merged.iloc[1568520:2091360]
    df_merged_5 = df_merged.iloc[2091360:2614200]
    df_merged_6 = df_merged.iloc[2614200:3137043]

    event_action_list = ['sub_car_claim_click'
                         'sub_car_claim_submit_click',
                         'sub_open_dialog_click',
                         'sub_custom_question_submit_click',
                         'sub_call_number_click',
                         'sub_callback_submit_click',
                         'sub_submit_success',
                         'sub_car_request_submit_click']

    df_merged_1['target'] = df_merged_1.apply(
        lambda x: 1 if x.event_action in event_action_list else 0, axis=1)

    columns_to_drop = [
        'session_id',
        'hit_date',
        'hit_time',
        'hit_number',
        'hit_type',
        'hit_referer',
        'hit_page_path',
        'event_category',
        'event_action',
        'event_label',
        'event_value',
        'client_id',
        'visit_date',
        'visit_time',
        'visit_number',
        'device_model',
        'target'
    ]

    X = df_merged_1.drop(columns_to_drop, axis=1)
    y = df_merged_1['target']

    numerical_features = X.select_dtypes(include=['int64', 'float64']).columns
    categorical_features = X.select_dtypes(include=['object']).columns

    numerical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='median')),
        ('column_astype', FunctionTransformer(column_astype)),
        ('scaler', StandardScaler())
    ])

    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('encoder', OneHotEncoder(handle_unknown='ignore'))
    ])

    # preprocessor = Pipeline(steps=[
    #     # ('new_feature', FunctionTransformer(new_feature)),
    #     ('filter_data', FunctionTransformer(filter_data))
    # ])

    column_transform = ColumnTransformer(transformers=[
        ('categorical', categorical_transformer, categorical_features),
        ('numerical', numerical_transformer, numerical_features) #поменять местами нум и кат
    ])

    models = (
        LogisticRegression(penalty='l1', solver='saga', random_state=42),
        RandomForestClassifier(random_state=42)
    )

    best_score = .0
    best_pipe = None
    for model in models:
        pipe = Pipeline(steps=[
            # ('preprocessor', preprocessor),
            ('transform', column_transform),
            ('classifier', model)
        ])

        score = cross_val_score(pipe, X, y, cv=4, error_score='raise', scoring='accuracy')

        print(f'model: {type(model).__name__}, acc_mean: {score.mean():.4f}, acc_std: {score.std():.4f}')

        if score.mean() > best_score:
            best_score = score.mean()
            best_pipe = pipe

    best_pipe.fit(X, y)
    print(f'best model: {type(best_pipe.named_steps["classifier"]).__name__}, accuracy: {best_score.mean():.4f}')
    with open('../model/sber_model.pickle', 'wb') as file:
        dill.dump({
            'model': best_pipe,
            'metadata': {
                'name': 'target action prediction pipeline',
                'author': 'Kataev German',
                'version': 1,
                'date': datetime.datetime.now(),
                'type': type(best_pipe.named_steps["classifier"]).__name__,
                'accuracy': best_score
            }
        }, file)


if __name__ == '__main__':
    main()

    # Почистить данные. Убрать NaN и выбросы. нужно поменять тип столбцов на инт32, иначе не хватает памяти для расчётов. Или ещё уменьшить датафрейм



