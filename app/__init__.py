from flask import Flask, render_template, redirect
from flask_migrate import Migrate
from .Config import Config, os
from .shipping_form import ShippingForm
from app.models import db, Package

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def root():
    packages = Package.query.all()
    return render_template("package_status.html", packages=packages)


@app.route('/new_package', methods=['GET', 'POST'])
def new_package():
    form = ShippingForm()
    if form.validate_on_submit():
        data = form.data
        new_package = Package(
            sender=data["sender"],
            recipient=data["recipient"],
            origin=data["origin"],
            destination=data["destination"],
            location=data["origin"]
        )
        new_package.advance_all_locations()
        db.session.add(new_package)
        db.session.commit()
        return redirect('/')
    return render_template("shipping_request.html", form=form)
