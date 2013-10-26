#!/usr/bin/env python
# vim: ts=4 shiftwidth=4 expandtab

import webapp2
from google.appengine.ext import db


class User(db.Model):
    email = db.StringProperty()
    name = db.StringProperty()
    token = db.StringProperty()


class Measurement(db.Model):
    email = db.StringProperty()
    dyear = db.StringProperty()
    dmonth = db.StringProperty()
    dday = db.StringProperty()
    dhour = db.StringProperty()
    dminute = db.StringProperty()
    when = db.StringProperty()
    bpm = db.StringProperty()

    def __getitem__(self, x):
        return getattr(self, x)


def add_measurement(e, r):
    mail = r.get("email", "")
    when = r.get("when", "")
    bpm = r.get("bpm", "")
    datepart = when.split(" ")[0]
    hourpart = when.split(" ")[1]

    m = Measurement()
    m.email = mail
    m.dyear = datepart.split("-")[0]
    m.dmonth = datepart.split("-")[1]
    m.dday = datepart.split("-")[2]

    m.dhour = hourpart.split(":")[0]
    m.dminute = hourpart.split(":")[1]

    m.when = when
    m.bpm = bpm
    m.save()
    e("measurement Added.")


def json_measurements(e, r):
    m = Measurement.all()
    e("[")
    a = []
    for i in m:
        json = "{email:'"+i["email"]+"', when:"
        json += "'"+i["when"]+"',bpm:'"+i["bpm"]+"'}"
        a.append(json)

    e(",".join(a))
    e("]")


def show_add_measurement_form(e, r):
    e("<form method=POST>")
    e("<input type=hidden name=ac value=add_measurement>")
    e("<h1> Add Measurement</h1>")
    e("Email:<br/><input type=text name=email value=test@test.com><br/>")
    e("BPM:<br/><input type=text name=bpm value=60><br/>")
    d = "2013-01-01 00:00:00"
    e("Date:<br/><input type=text name=when value='"+d+"'><br/>")
    e("<input type=submit name=submit value='Upload Measurement'>")
    e("</form>")
    e("<a href='?ac=show_measurements'>Show Measurements</a>")


def show_measurements(e, r):
    m = Measurement.all()
    e("<table border=1>")
    e("<table border=1>")
    e("<tr>")
    for a in ('Email', 'When', 'BPM'):
        e("<th>" + a + "</th>")
    e("</tr>")
    for i in m:
        e("<tr><td>" + i["email"] + "</td><td>" + i["when"] + "</td>")
        e("<td>" + i["bpm"] + "</td></tr>")
    e("</table>")


class MainHandler(webapp2.RequestHandler):
    def post(self):
        self.get()

    def get(self):
        #name = self.request.get("name", "none")
        ac = self.request.get("ac", "default")
        r = self.request
        e = self.response.write
        if ac == "default":
            show_add_measurement_form(e, r)
        if ac == "add_measurement":
            add_measurement(e, r)
        if ac == "show_measurements":
            show_measurements(e, r)
        if ac == "json_measurements":
            json_measurements(e, r)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
