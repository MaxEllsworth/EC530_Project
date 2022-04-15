#!/usr/bin/python3.8

from router import app


@app.route("/api/add_user/")
def add_user():
    True

@app.route("/api/delete_user")
def delete_user():
    True

@app.route("/api/update_user")
def update_user():
    True

@app.route("/api/assign_device_to_user")
def assign_device_to_user():
    True

@app.route("/api/remove_device_from_user")
def remove_device_from_user():
    True

@app.route("/api/list_available_devices")
def list_available_devices():
    True



