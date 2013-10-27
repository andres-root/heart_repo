#!/usr/bin/env python
# vim: ts=4 shiftwidth=4 expandtab

import webapp2
from google.appengine.ext import db


class User(db.Model):
    email = db.StringProperty()
    name = db.StringProperty()
    token = db.StringProperty()
    email_how_often = db.StringProperty()  # diario, mensual, semanal,
    birth_date = db.StringProperty()
    user_type = db.StringProperty()

    def __getitem__(self, x):
        return getattr(self, x)


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


def user_drop(e, r):
    email = r.get("email")
    a = db.GqlQuery("SELECT * FROM User WHERE email='" + email + "'")
    for i in a:
        i.delete()
    e("User Deleted.")


def read_template(a):
    c = open(a)
    data = c.read()
    c.close()
    return data


def add_user(e, r):
    e("<form method=POST action='?'>")
    e("<input type=hidden name=ac value=add_user2>")
    e("<h1> Add User</h1>")
    e("<p>Use this screen to create new users and assign roles to them</p>")
    e("<label>Email:</label><br/><input type=text name=email ><br/>")
    e("<label>Name:</label><br/><input type=text name=name ><br/>")
    e("<label>Email How Often:</label><br/><select name=email_how_often>")
    e("<option value='weekly'>Weekly</option>")
    e("<option value='monthly'>Monthly</option>")
    e("<option value='daily'>Daily</option>")
    e("</select><br/>")

    e("<label>Birth Date:</label><br/><input type=text name=birth_date ><br/>")
    e("<label>User Type:</label><br/><select name=user_type>")
    e("<option value='user'>User</option>")
    e("<option value='doctor'>Doctor</option>")
    e("<option value='admin'>admin</option>")
    e("</select><br/>")
    e("<input type=submit name=submit value='Create User'>")
    e("</form>")


def msg(title, message):
    m2 = "<img class=msg_icon src='/media/msg.png'>" + message
    return("<div class=msg>" + title +
           "<br><div class=msg_contents>" + m2 + "</div></div>")


def edit_profile2(e, r):
    pass


def show_dashboard(e, r):
    e("<h1>Heart Care Dashboard</h1>")

def edit_profile(e, r):
    #get current user email
    email = get_email()
    u = db.GqlQuery("SELECT * FROM User WHERE email='"+email+"'")
    c = 0
    for i in u:
        c += 1
        em = i["email"]
        na = i["name"]

    if c == 0:
        e("no user found.")
        return
    e("<form method=POST action='?'>")
    e("<input type=hidden name=ac value=edit_profile2>")
    e("<h1> Edit Profile</h1>")
    e("<label>Email:</label><br/><input type=text name=email value='"+em+"'>")
    e("<br/>")
    e("<label>Name:</label><br/><input type=text name=name value='"+na+"' >")
    e("<br/>")
    e("<label>Email How Often:</label><br/><select name=email_how_often>")
    e("<option value='weekly'>Weekly</option>")
    e("<option value='monthly'>Monthly</option>")
    e("<option value='daily'>Daily</option>")
    e("</select><br/>")

    e("<label>Birth Date:</label><br/><input type=text name=birth_date ><br/>")
    e("<label>User Type:</label><br/><select name=user_type>")
    e("<option value='user'>User</option>")
    e("<option value='doctor'>Doctor</option>")
    e("<option value='admin'>admin</option>")
    e("</select><br/>")
    e("<input type=submit name=submit value='Create User'>")
    e("</form>")


def add_user2(e, r):
    u = User()
    u.name = r.get("name")
    u.email = r.get("email")
    u.email_how_often = r.get("email_how_often")
    u.birth_date = r.get("birth_date")
    u.user_type = r.get("user_type")
    u.save()
    e("User Created.")


def show_users(e, r):
    u = User.all()
    e("<h1>Users</h1>")
    e("<table border=1>")
    e("<tr>")
    e("<th>Email</th>")
    e("<th>Name</th>")
    e("<th>Email How Often</th>")
    e("<th>Birth Date</th>")
    e("<th>User Type</th>")

    e("<th>&nbsp;</th>")
    e("</tr>")
    for i in u:
        e("<tr>")
        e("<td>"+str(i["email"])+"</td>")
        e("<td>"+str(i["name"])+"</td>")
        e("<td>"+str(i["email_how_often"])+"</td>")
        e("<td>"+str(i["birth_date"])+"</td>")
        e("<td>"+str(i["user_type"])+"</td>")
        e("<td><a href='?ac=user_drop&email="+i["email"]+"'>[x]</a></td>")
        e("</tr>")
    e("</table>")
    e("<a href='?ac=add_user'>Add User</a>")


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
    e(msg("Added", "measurement Added."))


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


def menu(e, r):
    a = "<div class=menu>"
    a += "<img onclick='location.href=\"/\";' width=150 valign=middle class=logo height=50 src='./media/logo.png' alt='HeartCare' /></a>"
    links = []
    #usertype
    links.append({"to": "?ac=show_users", 'label': 'Users'})
    links.append({"to": "?ac=show_dashboard", 'label': 'Dashboard'})
    links.append({"to": "?ac=show_measurements", 'label': 'Measurements'})
    links.append({"to": "?ac=show_add_measurement_form", 'label': 'New'})
    links.append({"to": "?ac=json_measurements", 'label': 'JSON'})
    links.append({"to": "?ac=my_profile", 'label': 'My Profile'})
    #
    links.append({"to": "?ac=my_patients", 'label': 'My Patients'})

    for i in links:
        a += "<a href='"+i["to"]+"'>"+i["label"]+"</a>&nbsp;"
    a += "</div>\n"
    a += "<div class=wrapper>"
    e(a)


def show_add_measurement_form(e, r):
    e("<form method=POST>")
    e("<input type=hidden name=ac value=add_measurement>")
    e("<h1> Add Measurement</h1>")
    #e("<label>Email:</label>")
    e("<input type=hidden name=email value='"+get_email()+"'><br/>")
    e("<label>BPM:</label><br/><input type=text name=bpm><br/>")
    d = "2013-01-01 00:00:00"
    e("<label>Date: (aaaa-mm-dd hh:ii:ss)</label><br/>")
    e("<input type=text name=when value='"+d+"'><br/>")
    e("<input type=submit name=submit value='Add Measurement'>")
    e("</form>")
    #e("<a href='?ac=show_measurements'>Show Measurements</a>")


def get_email():
    #todo: implement!
    return "dataf4l@gmail.com"


def show_measurements(e, r):
    email = get_email()
    m = db.GqlQuery("SELECT * FROM Measurement WHERE email='"+email+"'")
    e("<h1>Measurements</h1>")
    e("<table border=1>")
    e("<tr>")
    for a in ('Email', 'When', 'BPM'):
        e("<th>" + a + "</th>")
    e("</tr>")
    for i in m:
        e("<tr><td>" + i["email"] + "</td><td>" + i["when"] + "</td>")
        e("<td>" + i["bpm"] + "</td></tr>")
    e("</table>")
    e("<a href='?ac=show_add_measurement_form'>Add Measurement</a>")

class MainHandler(webapp2.RequestHandler):
    def post(self):
        self.get()

    def get(self):
        #name = self.request.get("name", "none")
        ac = self.request.get("ac", "default")
        r = self.request
        e = self.response.write

        if ac == "json_measurements":
            json_measurements(e, r)
        else:
            e(read_template("./template/header.html"))
            menu(e, r)
            if ac == "default":
                e(read_template("./template/start.html"))
            elif ac == "show_dashboard":
                show_dashboard(e, r)
            elif ac == "show_add_measurement_form":
                show_add_measurement_form(e, r)
            elif ac == "show_users":
                show_users(e, r)
            elif ac == "add_measurement":
                add_measurement(e, r)
            elif ac == "show_measurements":
                show_measurements(e, r)
            elif ac == "add_user":
                add_user(e, r)
            elif ac == "add_user2":
                add_user2(e, r)
            elif ac == "user_drop":
                user_drop(e, r)
            elif ac == "edit_profile":
                edit_profile(e, r)
            elif ac == "edit_profile2":
                edit_profile2(e, r)

            else:
                e(msg("ERROR", "Invalid Action:" + r.get("ac")))
            e(read_template("./template/footer.html"))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
