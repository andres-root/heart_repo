#!/usr/bin/env python
# vim: ts=4 shiftwidth=4 expandtab

import webapp2
from google.appengine.ext import db
from collections import OrderedDict


class User(db.Model):
    email = db.StringProperty()
    name = db.StringProperty()
    token = db.StringProperty()
    email_how_often = db.StringProperty()  # diario, mensual, semanal,
    birth_date = db.StringProperty()
    user_type = db.StringProperty()
    smoker = db.StringProperty()
    drinker = db.StringProperty()
    heart_condition = db.StringProperty()

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
    lon = db.StringProperty()
    lat = db.StringProperty()

    def __getitem__(self, x):
        return getattr(self, x)


def view_measurements(e, r):
    email = r.get("email")
    m = db.GqlQuery("SELECT * FROM Measurement WHERE email='"+email+"'")
    show_m(e, r, m, email)
    show_info(e)


def show_info(e):
    e(read_template("./template/info-rates.html"))


def user_drop(e, r):
    email = r.get("email")
    a = db.GqlQuery("SELECT * FROM User WHERE email='" + email + "'")
    for i in a:
        i.delete()
    e(t("User Deleted."))


def read_template(a):
    c = open(a)
    data = c.read()
    c.close()
    return data

i18n = {}


def t(s):
    if not(s in i18n):
        return "["+s+"]"
    return i18n[s]


def add_user(e, r):
    e("<form method=POST action='?'>")
    e("<input type=hidden name=ac value=add_user2>")
    e("<h1>"+t("Add User")+"</h1>")
    e("<p>"+t("Use this screen to create new users and assign roles to them") +
      "</p>")
    e("<div class=l>")
    e("<label>"+t("Email")+":</label><br/><input type=text name=email ><br/>")
    e("<label>"+t("Name")+":</label><br/><input type=text name=name ><br/>")
    e("<label>"+t("Email How Often") +
      ":</label><br/><select name=email_how_often>")
    e("<option value='weekly'>"+t("Weekly")+"</option>")
    e("<option value='monthly'>"+t("Monthly")+"</option>")
    e("<option value='daily'>"+t("Daily")+"</option>")
    e("</select><br/>")

    e("<label>"+t("Birth Date")+":</label><br/>")
    e("<select name=birth_year>")
    for i in range(1900, 2100):
        e("<option value="+str(i)+">"+str(i)+"</option>")
    e("</select>")
    e("<select name=birth_month>")
    months = OrderedDict()
    months["01"] = t("Jan")
    months["02"] = t("Feb")
    months["03"] = t("Mar")
    months["04"] = t("Apr")
    months["05"] = t("May")
    months["06"] = t("Jun")
    months["07"] = t("Jul")
    months["08"] = t("Aug")
    months["09"] = t("Sep")
    months["10"] = t("Oct")
    months["11"] = t("Nov")
    months["12"] = t("Dec")
    for i in months:
        e("<option value="+i+">"+months[i]+"</option>")
    e("</select>")
    e("<select name=birth_date>")
    for i in range(1, 31):
        e("<option value="+str(i)+">"+str(i)+"</option>")
    e("</select><br/>")

    e("</div>")
    e("<div class=l>")

    e("<label>"+t("User Type")+":</label><br/>")
    e("<select name=user_type>")
    e("<option value='user'>"+t("User")+"</option>")
    e("<option value='doctor'>"+t("Doctor")+"</option>")
    e("<option value='admin'>"+t("Admin")+"</option>")
    e("</select><br/>")

    e("<label>"+t("Do you Smoke?")+":</label><br/><select name=smoker>")
    e("<option value='0'>"+t("No")+"</option>")
    e("<option value='1'>"+t("Yes")+"</option>")
    e("</select><br/>")

    e("<label>"+t("Do you Drink?")+":</label><br/><select name=drinker>")
    e("<option value='0'>"+t("No")+"</option>")
    e("<option value='1'>"+t("Yes")+"</option>")
    e("</select><br/>")

    e("<label>"+t("Do you Have a Heart Condition?")+":</label><br/>")
    e("<select name=heart_condition>")
    e("<option value='0'>"+t("No")+"</option>")
    e("<option value='1'>"+t("Yes")+"</option>")
    e("</select><br/>")

    e("<input type=submit name=submit value='"+t("Create User")+"'>")
    e("</div>")

    e("</form>")


def register(e, r):
    add_user(e, r)


def msg(title, message):
    m2 = "<img class=msg_icon src='/media/msg.png'>" + message
    return("<div class=msg>" + title +
           "<br><div class=msg_contents>" + m2 + "</div></div>")


def edit_profile2(e, r):
    pass


def show_dashboard(e, r):
    email = r.get("email", get_email())

    e("<h1>"+t("Heart Care Dashboard")+"</h1>")
    e("<script src='./template/reports/html_graphics/Chart.js'></script>")
    e("<script>;var jsonvar = " + get_json(email) + ";</script>")
    e(read_template("./template/reports/html_graphics/histogram.html"))


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
    e("<h1>"+t("Edit Profile")+"</h1>")
    e("<label>"+t("Email") +
      ":</label><br/><input type=text name=email value='"+em+"'>")
    e("<br/>")
    e("<label>"+t("Name") +
      ":</label><br/><input type=text name=name value='"+na+"' >")
    e("<br/>")
    e("<label>"+t("Email How Often") +
      ":</label><br/><select name=email_how_often>")
    e("<option value='weekly'>"+t("Weekly")+"</option>")
    e("<option value='monthly'>"+t("Monthly")+"</option>")
    e("<option value='daily'>"+t("Daily")+"</option>")
    e("</select><br/>")

    e("<label>"+t("Birth Date") +
      ":</label><br/><input type=text name=birth_date><br/>")
    e("<label>"+t("User Type")+":</label><br/><select name=user_type>")
    e("<option value='user'>"+t("User")+"</option>")
    e("<option value='doctor'>"+t("Doctor")+"</option>")
    e("<option value='admin'>"+t("admin")+"</option>")
    e("</select><br/>")
    e("<input type=submit name=submit value='"+t("Create User")+"'>")
    e("</form>")


def add_user2(e, r):
    u = User()
    u.name = r.get("name")
    u.email = r.get("email")
    u.email_how_often = r.get("email_how_often")
    u.birth_date = (r.get("birth_year") + "-" + r.get("birth_month") + "-" +
                    r.get("birth_date"))
    u.user_type = r.get("user_type")
    u.smoker = r.get("smoker")
    u.drinker = r.get("drinker")
    u.heart_condition = r.get("heart_condition")
    u.save()
    e(msg("User Created.", "User Created OK"))


def show_users(e, r):
    u = User.all()
    e("<h1>"+t("Users")+"</h1>")
    e("<table border=1 cellspacing=0 cellpadding=0 class=dataset>")
    e("<tr>")
    e("<th>"+t("Email")+"</th>")
    e("<th>"+t("Name")+"</th>")
    e("<th>"+t("Email How Often")+"</th>")
    e("<th>"+t("Birth Date")+"</th>")
    e("<th>"+t("User Type")+"</th>")
    e("<th>"+t("Smoker")+"</th>")
    e("<th>"+t("Drinker")+"</th>")
    e("<th>"+t("Heart Condition")+"</th>")

    e("<th>&nbsp;</th>")
    e("<th>&nbsp;</th>")
    e("<th>&nbsp;</th>")
    e("</tr>")
    for i in u:
        e("<tr>")
        e("<td>"+str(i["email"])+"</td>")
        e("<td>"+str(i["name"])+"</td>")
        e("<td>"+str(i["email_how_often"])+"</td>")
        e("<td>"+str(i["birth_date"])+"</td>")
        e("<td>"+str(i["user_type"])+"</td>")
        e("<td>"+str(i["smoker"])+"</td>")
        e("<td>"+str(i["drinker"])+"</td>")
        e("<td>"+str(i["heart_condition"])+"</td>")
        e("<td><a href='?ac=user_drop&email="+i["email"]+"'>[x]</a></td>")
        e("<td><a href='?ac=view_measurements&email="+i["email"]+"'>")
        e(t("Measurements")+"</a></td>")
        e("<td><a href='?ac=show_dashboard&email="+i["email"]+"'>")
        e(t("Dashboard")+"</a></td>")
        e("</tr>")
    e("</table>")
    e("<a href='?ac=add_user'>"+t("Add User")+"</a>")


def add_measurement(e, r):
    mail = r.get("email", "")
    when = r.get("when", "")
    bpm = r.get("bpm", "")
    lon = r.get("lon", "")
    lat = r.get("lat", "")
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

    m.lon = lon
    m.lat = lat
    m.save()
    e(msg("Added", "measurement Added."))


def json_measurements(e, r):
    email = get_email()
    e(get_json(email))


def get_json(email):
    m = db.GqlQuery("SELECT * FROM Measurement WHERE email='"+email+"'" +
                    " ORDER BY when DESC")
    ax = ""
    ax += "["
    a = []
    for i in m:
        json = "{email:'"+i["email"]+"', when:"
        json += "'"+i["when"]+"',bpm:'"+i["bpm"]+"'}"
        a.append(json)

    ax += ",".join(a)
    ax += "]"
    return ax


def menu(e, r):
    a = "<div class=menu>"
    a += """<img onclick='location.href=\"/\";'
                 valign=middle
                 class=logo
                 height=70
                 src='./media/logo.png'
                 alt='"""+t("MobileHeartCare")+"""' />"""
    links = []
    #usertype
    links.append({"to": "?ac=show_users", 'label': t('Users')})
    links.append({"to": "?ac=show_dashboard", 'label': t('Dashboard')})
    links.append({"to": "?ac=show_measurements", 'label': t('Measurements')})
    links.append({"to": "?ac=show_add_measurement_form", 'label': t('New')})
    links.append({"to": "?ac=json_measurements", 'label': 'JSON'})
    links.append({"to": "?ac=my_profile", 'label': t('My Profile')})
    #
    links.append({"to": "?ac=my_patients", 'label': t('My Patients')})
    links.append({"to": "?ac=register", 'label': t('Register')})

    for i in links:
        a += "<a href='"+i["to"]+"'>"+i["label"]+"</a>&nbsp;"
    a += "</div>\n"
    a += "<div class=wrapper>"
    e(a)


def show_add_measurement_form(e, r):
    e("<form method=POST action='?ac=add_measurement'>")
    e("<input type=hidden name=ac value=add_measurement>")
    e("<h1>"+t("Add Measurement")+"</h1>")
    #e("<label>Email:</label>")
    e("<input type=hidden name=email value='"+get_email()+"'><br/>")
    e("<label>"+t("BPM")+":</label><br/><input type=text name=bpm><br/>")
    d = "2013-01-01 00:00:00"
    e("<label>"+t("Date")+": (aaaa-mm-dd hh:ii:ss)</label><br/>")
    e("<input type=text name=when value='"+d+"'><br/>")
    e("<input type=submit name=submit value='"+t("Add Measurement")+"'>")
    e("</form>")
    #e("<a href='?ac=show_measurements'>Show Measurements</a>")


def get_email():
    #todo: implement!
    return "dataf4l@gmail.com"


def show_measurements(e, r):
    email = get_email()
    m = db.GqlQuery("SELECT * FROM Measurement WHERE email='"+email+"'")
    show_m(e, r, m, email)
    show_info(e)
    e("<a href='?ac=show_add_measurement_form'>Add Measurement</a>")


def show_m(e, r, m, email):
    e("<h1>"+t("Measurements of")+": "+email+"</h1>")
    e("<table border=1 cellspacing=0 cellpadding=0  class=dataset>")
    e("<tr>")
    for a in ('Email', 'Date', 'BPM', 'Lon', "Lat"):
        e("<th>" + t(a) + "</th>")
    e("</tr>")
    for i in m:
        e("<tr><td>" + i["email"] + "</td><td>" + i["when"] + "</td>")
        e("<td>" + str(i["bpm"]) + "</td>")
        e("<td>" + str(i["lon"]) + "</td>")
        e("<td>" + str(i["lat"]) + "</td>")
        e("</tr>")
    e("</table>")


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
            elif ac == "register":
                register(e, r)
            elif ac == "add_user":
                add_user(e, r)
            elif ac == "add_user2":
                add_user2(e, r)
            elif ac == "user_drop":
                user_drop(e, r)
            elif ac == "view_measurements":
                view_measurements(e, r)
            elif ac == "edit_profile":
                edit_profile(e, r)
            elif ac == "edit_profile2":
                edit_profile2(e, r)
            elif ac == "a":
                edit_profile2(e, r)

            else:
                e(msg("ERROR", "Invalid Action:" + r.get("ac")))
            e(read_template("./template/footer.html"))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
