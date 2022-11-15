from flask import Blueprint, render_template

import repositories.product_repository as product_repository

reports_blueprint = Blueprint("reports", __name__)

@reports_blueprint.route("/reports/")
def reports():
    return render_template('reports/index.html.j2')

def _calc_totals(dc_products):
    total_cost = sum(p.cost_price for p in dc_products)
    total_retail = sum(p.retail_price for p in dc_products)
    return total_cost, total_retail

@reports_blueprint.route("/reports/discontinued")
def discontinued():
    dc_products = product_repository.select_discontinued()
    total_cost, total_retail = _calc_totals(dc_products)
    potential_profit = total_retail - total_cost
    return render_template('reports/discontinued.html.j2',
        total_cost=total_cost, total_retail=total_retail,
        potential_profit=potential_profit,
        products=dc_products)