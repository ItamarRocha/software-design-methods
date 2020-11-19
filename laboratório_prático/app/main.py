import streamlit as st
from view.view import View


def main():

    interface =  View()
    interface.main_menu()

if __name__ == '__main__':
	main()