from flask import Blueprint, render_template, request, redirect
from ..models.models import Tari

tari_bp = Blueprint('tari_bp', __name__)

@tari_bp.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        tari = Tari(nama=request.form["nama"], asal=request.form["asal"])
        tari.save()
        return redirect("/")
    tari_list = Tari.get_all()
    return render_template("index.html", tari_list=tari_list)

@tari_bp.route('/hapus/<id>')
def hapus(id):
    tari = Tari.get_by_id(id)
    if tari:
        tari.delete()
    return redirect("/")

@tari_bp.route('/update/<id>', methods=["GET", "POST"])
def update(id):
    tari = Tari.get_by_id(id)
    if request.method == "POST":
        tari.nama = request.form["nama"]
        tari.asal = request.form["asal"]
        tari.save()
        return redirect("/")
    return render_template("update.html", tari=tari)
