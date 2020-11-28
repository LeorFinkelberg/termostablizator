# -*- coding: utf-8 -*-
'''
25.11.2020 21:31:32
---------------------------------------------------------
Расчет коэффициента теплопередачи от грунта к СОУ
выполняется в соотвтествии с Приложением Б 
СТО Газпром 2-2.1-390-2009 "Руководство по проектированию
и применению сезонно-охлаждающих устройств для
термостабилизации грунтов оснований фундаментов"
'''

import streamlit as st
from streamlit.components import v1
import numpy as np
import math
from pandas import DataFrame, Series
#from scipy.special import (i1, i0, k0, k1)
from typing import NoReturn, Any
from css import header_css, subheader_css, annotation_css


def header() -> NoReturn:
    st.set_page_config(page_title='Приложение для расчета коэффициента теплопередачи от грунта к СОУ')
    header_css(
        'Приложение<br>для расчета коэффициента теплопередачи от грунта'
        '<br>к сезонно-охлаждающим устройствам')
    
    subheader_css(
        'Расчет выполняется в соответствии с <i>Приложением Б</i> '
        '"Алгоритм постановки граничных условий при прогнозе температурного '
        'режима грунтов численными методами" документа '
        '<i>СТО Газпром 2-2.1-390-2009</i> '
        '"Руководство по проектированию и применению сезонно-охлаждающих '
        'устройств для термостабилизаторов грунтов оснований фундаментов"')


def E_latex_dir_rib(res):
    st.latex(r'E = \dfrac{\tanh(x)}{x},\ x = h\sqrt{\dfrac{2 \alpha}{\lambda\, \delta}} \to E='
             + f'{res:10.3f}')


def alpha0_latex(alpha0):
    st.latex(r'\alpha_0 = 4.606\, \dfrac{w^{0.6}}{d^{0.4}} \to \alpha_0=' + f'{alpha0:5.3f}')
    
    
def Ki_latex(K_isp):
    st.latex(r'K_i = 4.606 \cdot \dfrac{w^{0.6}(E \cdot F_p + F_c)}{d^{0.4} \cdot F_i}=' + f'{K_isp:10.3f}')


def E_compute(
        item: int,
        rib_hight: float,
        alpha_v: float,
        lambda_rib: float,
        rib_wall_thickness: float,
        dp_rib: float,
        d_rib: float
        ) -> float:
    '''
    Вычисляет коэффициент оребрения
    '''
    inner_expr = rib_hight*np.sqrt(2*alpha_v/(lambda_rib*rib_wall_thickness))
    if item == 1:
        return np.tanh(inner_expr)/inner_expr
    else:
        return 0.98*np.tanh(inner_expr)/inner_expr
        # ub = inner_expr/(dp_rib/d_rib -1)
        # ue = ub*dp_rib/d_rib
        # beta = i1(ue)/k1(ue)    
        # return 2/( ub*(1 - ue/ub)**2* (i1(ub) - beta*k1(ub))/(i0(ub) + beta*k0(ub)) )


def items_for_E(items):
    Eflag = st.sidebar.radio('Коэффициент эффективности оребрения', items)

    if Eflag == items[0]:
        return 1
    else:
        return 2


def annotation_for_E(item):
    if item == 1:
        annotation_css('Расчет проводится для случая прямых ребер '
                       'постоянной толщины')
    else:
        annotation_css('Расчет проводится для случая круглых поперечных ребер '
                       'постоянной толщины')


def compute_heat_transfer_coef():
    '''
    Вычисляет коэффициент теплопередачи от грунта
    к СОУ, отнесенный к площади поверхности испарителя
    '''  
    st.sidebar.header('Входные параметры')
    st.sidebar.subheader('Геометрические параметры')
    Eitems = ('Прямые ребра постоянной толщины',
              'Круглые поперечные ребра постоянной толщины')
    Eitem = items_for_E(Eitems)  # вариант формы ребер
    # ------------------------------------------------------------------------
    rib_wall_thickness = st.sidebar.number_input(
        'Толщина стенки ребра, м', value=0.0005, min_value=0.0001,
        max_value=0.1, step=0.0001, format='%g')
    dp_rib = st.sidebar.number_input(
        'Наружный диаметр круглого ребера, м', value=0.070, min_value=0.050,
        max_value=2.0, step=0.001,format='%f')
    d_rib = st.sidebar.number_input(
        'Наружный диаметр трубы конденсатора, м', value=0.038, min_value=0.010,
        max_value=0.080, step=0.001, format='%f')
    L_isp = st.sidebar.number_input(
        'Длина испарительной части, м', value=16.2, min_value=6.0,
        max_value=30.0, step=0.001, format='%f')
    L_cond = st.sidebar.number_input(
        'Длина конденсаторной части, м', value=1.8, min_value=0.5,
        max_value=10.0, step=0.001, format='%f')
    L_spiral = st.sidebar.number_input(
        'Длина оребренной части, м', value=1.44, min_value=0.200,
        max_value=5.0, step=0.001, format='%f')
    step_spiral = st.sidebar.number_input(
        'Расстояние между ребрами, м', value=0.003, min_value=0.0005,
        max_value=5.0, step=0.001, format='%f')
    st.sidebar.subheader('Прочие параметры')
    lambda_rib = st.sidebar.number_input(
        'Теплопроводность матер-ла оребрения, Вт/(м К)', value=210.0,
        min_value=8.0, max_value=1000.0, step=0.01, format='%f')
    wind_speed = st.sidebar.selectbox('Скорость ветра, м', (1, 3))
    
    # Коэффициент теплоотдачи от гладкостенной трубы конденсатора
    # к окружающему воздуху, Вт/(м^2 K)
    alpha0 = 4.606*wind_speed**0.6/d_rib**0.4
    # Площаль поверхности неоребренной части конденсатора
    F_nonrib = math.pi*d_rib*L_cond
    # Площадь поверхности ребер
    F_rib = 2*( math.pi*dp_rib**2/4 - math.pi*d_rib**2/4 )*L_spiral/step_spiral
    # Площадь поверхности испарительной части
    F_isp = math.pi*d_rib*L_isp
    # Площадь наружной (оребрной) поверхности конденсатора
    Fpc = F_rib + F_nonrib
    # Высота ребер
    rib_hight = (dp_rib - d_rib)/2
    # Коэффициент эффективности оребрения
    E = E_compute(Eitem, rib_hight, alpha0,
                  lambda_rib, rib_wall_thickness, dp_rib, d_rib)
    # Приведнный коэффициент теплоотдачи от стенки конденсатора к окружающему воздуху
    alpha_pr = alpha0/Fpc*(E*F_rib + F_nonrib)
    # Коэффициент теплопередачи от грунта к СОУ, отнесенный к площади поверхности испарителя
    K_isp = alpha_pr*Fpc/F_isp
    
    if st.button('Расчитать...'):   
        annotation_for_E(Eitem)
        if ( (K_isp > 14.5 and wind_speed == 1) or (K_isp > 21 and wind_speed == 3) ):
            annotation_css('Коэффициент теплопередачи от грунта к СОУ, Вт/(м^2 К)', size=15)
            Ki_latex(K_isp)
        else:
            st.error('Согласно п. 1.2.3 ТУ Коэффициент теплоотдачи от грунта '
                     'к СОУ при скорости ветра 1 м/с должен быть '
                     'не менее 14,5 Вт/(м^2 К)')
        

if __name__ == '__main__':
    header()
    compute_heat_transfer_coef()
