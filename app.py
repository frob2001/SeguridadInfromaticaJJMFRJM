from flask import Flask, render_template, request, redirect, url_for, flash, session
from functools import wraps
from config import auth, fdb

app = Flask(__name__)
app.secret_key = "seginf"

""""
⡍⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣷⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣽⣿⣿⣿⣿⠿⠛⠛⠛⠋⠛⠛⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠘⣧⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢼⣿⢿⣿⠋⠀⠀⣀⣄⡀⠀⠀⠀⠀⣗⡯⣗⡦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡗⣿⣆⠀⠙⣵⣿⣯⠗⢀⣴⣾⡏⠛⢮⣿⣦⡑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⠹⡆⠀⠈⠉⠉⠘⢸⠛⢻⣏⡙⠦⡿⠛⣷⠈⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣻⢾⢘⣿⣿⡀⠳⠀⠙⠂⠺⢥⣺⢆⠞⠙⠛⠶⣧⡀⠹⡇⠀⠱⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣸⣿⣧⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢾⣷⡿⣾⣿⠃⢷⣄⠀⠐⢶⡶⢦⣦⠏⠀⠀⠀⠀⠈⠙⠶⢫⣳⢀⣬⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣹⣿⣿⣿⣅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡿⠟⠉⠀⠀⠉⠳⢄⣀⣉⣽⣅⣀⣀⣀⣀⠀⠀⠀⠀⠀⠹⣏⠀⠘⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢿⣿⣿⣿⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⢶⣾⣿⡥⡄⠀⢀⣀⠀⠀⠀⠀⠈⠁⠀⢻⣿⣇⠀⠀⠙⠢⣄⠀⠀⠀⢹⡄⠀⠈⢣⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⣿⣿⣿⣧⣦⡀⠀⠀⠀⠀⠀⠀⢀⡞⠁⠀⠀⠻⣿⣿⣆⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⢿⣿⡆⠀⠀⠀⠈⠳⣄⠀⠀⢿⡄⠀⠀⠳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⣿⣿⣿⣿⣿⣿⣿⣶⣤⣤⣀⣀⣼⠁⠀⠀⠀⠀⢹⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣷⢠⡖⠀⠀⠀⠈⠓⢦⣄⣧⠀⠀⠀⠹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣝⣦⡀⠀⠀⠀⠀⠈⢻⡀⠀⠀⠀⠹⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⣟⢀⣿⣿⣿⣿⣿⣷⣦⣄⣀⣂⣀⣀⣀⣤⣿⣿⣧⣀⣙⡿⣀⠀⠀⠀⠀⠈⢷⡀⠀⠀⠀⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⡈⠉⠉⠻⠷⢦⣄⡀⠀⠑⠆⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡇⣿⣿⣿⣿⣿⣿⣿⣿⡟⣻⣿⣿⠇⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠉⡳⠲⠤⠤⣖⠛⠋⠉⠑⠒⠒⠲⠤⠤⠤⢄⣀⠀⠀
⡇⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣻⣿⠁⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠐⠉⠙⠖
⠃⠉⠁⠀⠈⠙⠿⣿⣿⣿⣿⣿⢻⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠀⠀⠀⠀⠀
⠁⠀⠀⠀⠀⠀⠀⠀⢻⣱⣷⡫⡿⠀⠀⠀⠀⣿⠟⠻⡿⠿⢿⣿⣿⣿⡿⠿⠿⠿⠿⠿⠿⠿⢿⣇⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⡘⠀⠀⠀⠀⢀⠀
⡄⠀⠀⠀⠀⠀⠀⢀⡷⣵⠿⣫⡇⠀⠀⠀⢠⣟⠀⡠⢹⡄⠑⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣞⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⢘
⡂⠀⠀⠀⠀⢀⣾⡽⢹⠙⠊⡾⠀⠀⠀⠀⢸⡷⠀⣡⠿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣇⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⢀⢀⠀⠀⠀⠀⡠⠀⠀⠈
⠁⠀⠀⡠⢞⠟⢋⣷⣼⠇⢸⠃⠀⠀⠀⠀⣼⣧⣴⣇⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡞⡏⡳⠟⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⠀⢀⠀⠀⠀⠀⠀⠀⢰
⢃⢦⢞⣴⣅⡔⠟⣏⡉⠀⡟⠀⠀⠀⠀⢰⡿⠛⢿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⡄⠀⡸⣰⡁⠘⣆⢱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⡠⠄⠀⠀⠀⠀⠀⠀⢠
⠘⣌⣿⢟⠿⣧⠶⠟⠁⠂⣇⠀⠀⠀⠀⡼⠀⠀⠈⣿⣿⣷⡀⠀⠀⠀⠀⠀⣸⠃⠀⢠⡏⠁⠀⢿⠄⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⢸
⠀⠹⡸⡏⡼⠛⠀⠀⠀⢰⡏⠀⠀⠀⢰⠃⠘⢣⠀⠸⣿⣿⣿⡄⠀⠀⠀⠀⠀⢀⣰⣿⡟⡶⡶⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⢀⠀⠀⠀⠀⠀⠀⠀⢈
⠀⠀⢳⠘⡇⠀⠀⠀⠀⢸⡏⠀⠀⢀⡧⠥⣄⡀⠁⡀⢹⣿⣿⣿⣦⣀⣀⣀⣴⣾⣿⡟⠀⡿⠁⠀⢦⢸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰
⠀⠀⠀⢣⠸⡄⠀⠀⠀⢸⠃⠀⠀⡼⠀⠀⠀⠉⢲⢅⢘⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁⠀⠀⡇⠀⠀⠈⠘⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸
⠀⠠⡄⠀⢣⢱⠀⠀⠀⣿⠀⠀⣰⠃⠀⠀⠀⠀⠈⠃⢫⣿⣿⣿⣿⡿⠟⠉⠀⠀⠀⠀⠀⢻⣤⠀⠀⢀⡇⡀⠀⠀⠀⠀⠐⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠀⠀⠀
⠀⠀⢜⣄⡈⢇⣧⢄⣰⡏⢀⠀⡏⠀⠀⠀⠀⠀⠀⠘⢼⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⢸⣞⠀⢄⢸⡆⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⢸⠀⠀⡄
⡀⠀⠈⠓⢙⡿⣾⣤⣿⠃⠠⠀⢧⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡏⠙⣺⡸⡥⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⡈⠀⠀⠃
⠀⠀⠀⠀⠈⠂⠁⣽⣿⠀⠈⠄⢸⠀⠀⠀⠀⠀⠀⠀⢸⠙⠻⣆⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢶⣉⠤⢷⠤⠤⣀⠀⠀⠀⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⢰⠀
⠀⠀⠀⠀⠀⢀⣾⡿⠁⡠⣣⢁⢸⠀⠀⠀⠀⠀⠀⠀⡜⠀⠀⠙⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡏⠱⠊⢁⣀⣠⡎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠇⠀⠸⠀
⠀⠠⣄⠀⠀⣼⣹⠀⣼⠏⢹⡎⢺⡀⠀⠀⠀⠀⠀⡄⣿⠂⠀⠀⠈⢿⡆⠀⠀⠀⠀⠀⠀⠀⠀⢸⠊⣩⠛⠣⢟⠪⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⢰⢸⠀⢀⡇⢰
⠀⠀⠀⠉⢺⣟⡇⢰⠋⠀⠘⢷⡛⡇⠀⠀⠀⠀⠀⢸⢿⣇⠀⠀⠀⢸⡞⠀⠀⠀⠀⠀⠀⠀⠀⠸⡆⠎⠀⠀⠀⠉⠚⠷⣄⠀⠀⡠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢸⠀⣿⡇⢸
⠀⠘⢶⡠⡞⣿⠀⡏⠀⠀⠠⠂⠉⠁⠀⠀⠀⠀⠀⡘⠀⠈⠳⢦⡀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⣟⡴⠊⠀⠀⠀⠀⠐⠩⢻⡼⡀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡌⠀⣿⠀⠈
⣀⣀⣠⢙⣾⣽⣄⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡗⠀⠀⠀⠀⠉⠺⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢱⠤⠂⠀⠀⠀⠀⠀⠀⢸⠹⡧⡠⠀⠀⡑⠀⠀⠀⠀⠀⠀⠀⢸⡇⢰⣿⠀⡀
⠀⢈⠙⠳⣿⣻⡿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠁⠀⠀⠀⠀⠀⠀⠀⠑⠦⡀⠀⠀⠀⠀⠀⠀⢸⠄⠀⠀⠀⠀⠀⠀⡠⠃⠀⣧⣽⢤⠀⠀⠀⠐⠀⠀⠀⠀⠀⢸⠁⢸⡏⠀⡇
⠂⠀⠫⣖⣷⠿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⢬⠓⢤⡀⠀⠀⠀⣸⠥⠀⠀⠀⠀⠀⠀⠀⠀⡜⣹⢉⡀⠁⠀⠀⠠⠐⠀⣀⠆⣀⢸⣀⣿⡇⢰⠀


"""

def login_required(f):
  @wraps(f)
  def decorated_function(*args, **kwargs):
    if not session.get("user"):
      return redirect(url_for("login"))
    return f(*args, **kwargs)
  return decorated_function

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            account_info = auth.get_account_info(user['idToken'])
            print("logged")
            if account_info['users'][0]['emailVerified']:
                # Email is verified, allow user to log in
                print("Email is verified")
                session['user'] = user['localId']
                return redirect(url_for('dashboard'))
            else:
                # Email is not verified, redirect user to a page informing them to verify their email
                return render_template('login.html', message='El correo no ha sido verificado')
        except Exception as e:
            return render_template('login.html', message='El correo o la contraseña son incorrectos')
    else:
        return render_template('login.html')

#Logout
@app.route('/logout')
def logout():
  session.clear()
  return redirect(url_for("login"))


#Registro de usuarios
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        phone_number = request.form['phone_number']

        if password == confirm_password:
            try:
                user = auth.create_user_with_email_and_password(email, password)
                fdb.child("users").child(user['localId']).set({
                    "email": email,
                    "phone_number": phone_number
                })

                auth.send_email_verification(user['idToken'])

                return redirect('/')
            except Exception as e:
                return render_template('register.html', error=str(e))
        else:
            return render_template('register.html', message="Passwords do not match.")
    else:
        return render_template('register.html')

#Reseteo de contraseña
@app.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    if request.method == 'POST':
        email = request.form['email']
        try:
            auth.send_password_reset_email(email)
            return render_template('reset_password.html', message='Email de reseteo de contrasena enviado con exito')
        except:
            return render_template('reset_password.html', error='El correo no esta registrado')

    return render_template('reset_password.html')

#Pagina principal (tabla)
@app.route('/dashboard')
@login_required
def dashboard():
    datos = fdb.child("Activos").get().val()
    return render_template('dashboard.html', datos=datos)

#Crear activo
@app.route('/crear_activo', methods=['GET', 'POST'])
@login_required
def crear_activo():
  if request.method == 'POST':
      id = request.form['id']
      area = request.form['area']
      propietario = request.form['propietario']
      funcion = request.form['funcion']
      conexion = request.form.get('conexion')
      print(conexion)
      if conexion:
          conexion_value = 'Sí'
      else:
          conexion_value = 'No'
      criticidad = float(request.form['criticidad'])
      ubicacion = request.form['ubicacion']
      categoria = request.form.get('categoria_text')
      clasificacion = request.form.get('clasificacion_text')
      valor = float(request.form['valor'])
      utilidad = request.form.get('utilidad_text')

      nuevo_activo = {"id": id, "area": area, "propietario": propietario, "funcion": funcion, "conexion": conexion_value, "criticidad" : criticidad, "ubicacion":ubicacion, "categoria": categoria, "clasificacion": clasificacion, "valor": valor, "utilidad": utilidad, "riesgo": ""}
      print(nuevo_activo)
      fdb.child("Activos").push(nuevo_activo)

      return redirect(url_for('dashboard'))

  return render_template('crear_activo.html')

#Detalles activo
@app.route('/detallesactivo/<string:key>', methods=["GET", "POST"])
@login_required
def detalles_activo(key):
    campo = fdb.child('Activos').child(key).get().val()
    return render_template('detalles_activo.html', key=key, campo=campo)

#Actualizar activo
@app.route('/actualizaractivo/<string:key>', methods=["GET", "POST"])
@login_required
def actualizar_activo(key):
  campo = fdb.child("Activos").child(key).get().val()
  if request.method == "POST":
    id = request.form['id']
    area = request.form['area']
    propietario = request.form['propietario']
    funcion = request.form['funcion']
    conexion = request.form.get('conexion')
    if conexion:
        conexion_value = 'Sí'
    else:
        conexion_value = 'No'
    criticidad = float(request.form['criticidad'])
    ubicacion = request.form['ubicacion']
    categoria = request.form.get('categoria_text')
    clasificacion = request.form.get('clasificacion_text')
    valor = float(request.form['valor'])
    utilidad = request.form.get('utilidad_text')

    fdb.child("Activos").child(key).update({"id": id, "area": area, "propietario": propietario, "funcion": funcion, "conexion": conexion_value, "criticidad" : criticidad, "ubicacion":ubicacion, "categoria": categoria, "clasificacion": clasificacion, "valor": valor, "utilidad": utilidad, "riesgo": ""})
    return redirect(url_for('dashboard'))
  else:
    return render_template('detalles_activo.html', key=key, campo=campo)

#eliminar activo
@app.route('/eliminaractivo/<string:key>')
@login_required
def eliminar_activo(key):
    fdb.child("Activos").child(key).remove()
    return redirect(url_for('dashboard'))


#Crear activo
@app.route('/calcular_riesgo/<string:key>', methods=['GET', 'POST'])
@login_required
def calcular_riesgo(key):
    activos = fdb.child("Activos").child(key).get().val()
    categoria_activo = activos["categoria"]
    if categoria_activo == "DC":
        promedio = 4
    elif categoria_activo == "SW":
        promedio = 3.636
    elif categoria_activo == "HW":
        promedio = 3.444
    elif categoria_activo == "R":
        promedio = 3.875
    elif categoria_activo == "P":
        promedio = 4
    elif categoria_activo == "IF":
        promedio = 4
    elif categoria_activo == "DT":
        promedio = 3.667
    elif categoria_activo == "DM":
        promedio = 4.5

    amenazas = fdb.child("Amenazas").get().val()
    datos_filtrados = []
    codigos = []

    # Filtrar los datos según la categoría del activo
    for codigo, amenaza in amenazas.items():
        if amenaza.get(categoria_activo) == True:
            datos_filtrados.append({
                'codigo': codigo,
                'amenaza': amenaza['Amenaza'],
                'vulnerabilidad': amenaza['Vulnerabilidad'],
                'calificacion': amenaza['Calificación']
            })
            codigos.append(codigo)
    
    print(codigos)

    medidas = fdb.child("Medidas").get().val()

    medidas_filtradas = {codigo: medidas[codigo] for codigo in codigos if codigo in medidas}

    print(medidas_filtradas)




    if request.method == "POST":
        

        probabilidad = float(request.form['probabilidad'])/100
        
        preventivos = float(request.form['preventivos'])/100
        deteccion = float(request.form['deteccion'])/100
        correctivos = float(request.form['correctivos'])/100
        compensacion = float(request.form['compensacion'])/100
        fisicos = float(request.form['fisicos'])/100

        print(probabilidad, preventivos, deteccion, correctivos, compensacion, fisicos, promedio)

        fe = preventivos + deteccion + correctivos + compensacion + fisicos

        riesgo = ((probabilidad * promedio) + promedio) * (1-fe)

        print(riesgo)

        if riesgo <= 4.00:
            nivel = "Bajo"
        elif riesgo >= 4.01 and riesgo <= 7.00:
            nivel = "Medio"
        elif riesgo >= 7.01 and riesgo <= 9.00:
            nivel = "Alto"
        elif riesgo >= 9.01:
            nivel = "Crítico"

        print(nivel)

        riesgo = round(riesgo, 2)

        
        fdb.child("Activos").child(key).update({"id": activos["id"], "area": activos["area"], "propietario": activos["propietario"], "funcion": activos["funcion"], "conexion": activos["conexion"], "criticidad" : activos["criticidad"], "ubicacion": activos["ubicacion"], "categoria": categoria_activo, "clasificacion": activos["clasificacion"], "valor": activos["valor"], "utilidad": activos["utilidad"], "riesgo": nivel})
        return render_template('calificacion.html', nivel=nivel, riesgo=riesgo, medidas=medidas_filtradas)


    else:
        return render_template('riesgo.html', key=key, datos=datos_filtrados)


if __name__ == "__main__":
    app.run(debug=True)