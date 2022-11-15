from flask import Blueprint, render_template

from models.financial_report import FinancialReport
import repositories.product_repository as product_repository

reports_blueprint = Blueprint("reports", __name__)

@reports_blueprint.route("/reports/")
def reports():
    return render_template('reports/index.html.j2')

@reports_blueprint.route("/reports/discontinued")
def discontinued():
    dc_products = product_repository.select_discontinued()
    financial_report = FinancialReport()
    financial_report.calc_report(dc_products)
    return render_template('reports/discontinued.html.j2',
        financial_report=financial_report,
        products=dc_products)

@reports_blueprint.route("/reports/outofstock")
def out_of_stock():
    products = product_repository.select_out_of_stock()
    return render_template('reports/outofstock.html.j2',
        products=products)

@reports_blueprint.route("/reports/allstock")
def all_stock():
    products = product_repository.select_all()
    financial_report = FinancialReport()
    financial_report.calc_report(products)
    return render_template('reports/allstock.html.j2',
        financial_report=financial_report,
        products=products)