# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 15:31:33 2020

@author: ADM
"""

import streamlit as st


def header_css(text: str = "", clr: str = "black"):
    st.markdown(
        f"<h1 style='font-family: Helvetica, sans-serif;"
        "line-height: 1.2; margin-top: 5px; font-size: 25px;"
        "text-align: center;"
        f"color: {clr}'>{text}",
        unsafe_allow_html=True,
    )


def subheader_css(text: str = "", clr: str = "black"):
    st.markdown(
        f"<h2 style='font-family: Helvetica, sans-serif;"
        "line-height: 1.2; text-align: justify; font-size: 20px;"
        f"color: {clr}'>{text}",
        unsafe_allow_html=True,
    )


def annotation_css(text: str = "", clr: str = "black", size: int = 15):
    st.markdown(
        f"<h2 style='font-family: Helvetica, sans-serif;"
        f"line-height: 1.2; text-align: justify; font-size: {size}px;"
        f"color: {clr}'><i>{text}</i>",
        unsafe_allow_html=True,
    )


def annotation_normal_css(text: str = "", clr: str = "black", size: int = 15):
    st.markdown(
        f"<h2 style='font-family: Helvetica, sans-serif;"
        f"line-height: 1.2; text-align: justify; font-size: {size}px;"
        f"color: {clr}'>{text}",
        unsafe_allow_html=True,
    )
