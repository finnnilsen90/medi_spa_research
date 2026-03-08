import pandas as pd
import numpy as np
import copy

class MediForecastAssumptions:
    def __init__(self,operating_hours_per_day=8, receivables_days=5, payables_days=30, tax_rate=0.28, months=36):
        self.minutes_open_month = operating_hours_per_day * 20 * 60  # Assuming 20 days open per month
        self.services = {
            "Premium Facial": {"avg_price": 150,  "sessions_per_month": 3, "growth_rate": 0.04, "time_per_session": 90},
            "European Facial": {"avg_price": 120,  "sessions_per_month": 5, "growth_rate": 0.04, "time_per_session": 75},
            "Express Facial": {"avg_price": 90,  "sessions_per_month": 21, "growth_rate": 0.06, "time_per_session": 45},
            "Lux Facial": {"avg_price": 150,  "sessions_per_month": 4, "growth_rate": 0.04, "time_per_session": 60},
            "Microderm Facial": {"avg_price": 150,  "sessions_per_month": 10, "growth_rate": 0.05, "time_per_session": 60},
            "Gentelmen's Facial": {"avg_price": 100,  "sessions_per_month": 3, "growth_rate": 0.04, "time_per_session": 60},
            "Hand Treatment": {"avg_price": 10,  "sessions_per_month": 25, "growth_rate": 0.07, "time_per_session": 15},
            "Lash Tint": {"avg_price": 30,  "sessions_per_month": 15, "growth_rate": 0.07, "time_per_session": 30},
            "Brow Tint": {"avg_price": 20,  "sessions_per_month": 16, "growth_rate": 0.08, "time_per_session": 15},
            "Retail Products":  {"avg_price": 120,  "sessions_per_month": 75, "growth_rate": 0.03, "time_per_session": 0},
        }

        self.cogs_pct = {
            "Premium Facial": 0.20,
            "European Facial": 0.20,
            "Express Facial": 0.20,
            "Lux Facial": 0.20,
            "Microderm Facial": 0.15,
            "Gentelmen's Facial": 0.20,
            "Hand Treatment": 0.15,
            "Lash Tint": 0.15,
            "Brow Tint": 0.15,
            "Retail Products":  0.50,
        }

        self.fixed_opex = {
            "Rent (SF/Oakland avg)": 3_000,
            "Marketing/SEO":          500,
            "Software/EMR":             100,
            "Insurance (med mal)":    1_000,
            "Utilities":              800,
            "Supplies (non-COGS)":    100,
            "Misc/Admin":             300,
        }

        self.variable_opex_pct = 0.04

        self.initial_investment = {
            "Equipment":              1_500,
            "Leasehold Improvements": 500,
            "Licenses/Legal":          1_000,
            "Working Capital":         1_000,
            "Marketing Launch":        1_000,
        }

        self.total_investment = sum(self.initial_investment.values())

        self.receivables_days = receivables_days
        self.payables_days    = payables_days
        self.tax_rate         = tax_rate
        self.months           = months

    def utilization(self):
        minutes_open_month = self.minutes_open_month
        time_month = [i[1]["time_per_session"] * i[1]["sessions_per_month"] for i in self.services.items()]

        run_down = {
            "minutes_open_month": minutes_open_month,
            "total_time_month": sum(time_month),
            "utilization_pct": str(round(sum(time_month)/minutes_open_month * 100, 2)) + "%"
        }

        return run_down
    def build_forecast(self) -> pd.DataFrame:
        rows = []

        for m in range(1, self.months + 1):
            row = {"Month": m}

            # ── Revenue ──
            rev_by_service = {}
            for svc, params in self.services.items():
                growth = (1 + params["growth_rate"] / 12) ** (m - 1)
                rev_by_service[svc] = params["avg_price"] * params["sessions_per_month"] * growth
            total_revenue = sum(rev_by_service.values())

            # ── COGS ──
            total_cogs = sum(
                rev_by_service[svc] * self.cogs_pct[svc]
                for svc in rev_by_service
            )
            gross_profit = total_revenue - total_cogs
            gross_margin = gross_profit / total_revenue

            # ── OpEx ──
            fixed_opex = sum(self.fixed_opex.values())
            variable_opex = total_revenue * self.variable_opex_pct
            total_opex = fixed_opex + variable_opex
            ebitda = gross_profit - total_opex

            # ── D&A (straight-line, 5yr equipment / 10yr improvements) ──
            da = (
                self.initial_investment["Equipment"] / (5 * 12) +
                self.initial_investment["Leasehold Improvements"] / (10 * 12)
            )
            ebit = ebitda - da
            tax = max(ebit * self.tax_rate, 0)
            net_income = ebit - tax

            # ── Cash Flow ──
            # Operating
            delta_ar = total_revenue * (self.receivables_days / 30) if m == 1 else (
                total_revenue - rows[-1]["Total_Revenue"]
            ) * (self.receivables_days / 30)
            delta_ap = total_cogs * (self.payables_days / 30) if m == 1 else (
                total_cogs - rows[-1]["Total_COGS"]
            ) * (self.payables_days / 30)

            cfo = net_income + da - delta_ar + delta_ap

            # Investing (all upfront, month 0 — show as 0 in monthly)
            cfi = 0

            # Financing (none assumed post-launch)
            cff = 0

            net_cash_flow = cfo + cfi + cff

            # ── Cumulative cash & ROI ──
            cum_net_income = net_income + (rows[-1]["Cum_Net_Income"] if rows else 0)
            cum_cash = net_cash_flow + (rows[-1]["Cum_Cash_Flow"] if rows else -self.total_investment)

            roi = (cum_net_income / self.total_investment) * 100

            row.update({
                "Total_Revenue": total_revenue,
                "Total_COGS": total_cogs,
                "Gross_Profit": gross_profit,
                "Gross_Margin_%": gross_margin * 100,
                "Fixed_OpEx": fixed_opex,
                "Variable_OpEx": variable_opex,
                "EBITDA": ebitda,
                "DA": da,
                "EBIT": ebit,
                "Tax": tax,
                "Net_Income": net_income,
                "CFO": cfo,
                "Net_Cash_Flow": net_cash_flow,
                "Cum_Cash_Flow": cum_cash,
                "Cum_Net_Income": cum_net_income,
                "ROI_%": roi,
            })
            rows.append(row)

        return pd.DataFrame(rows)
    
    def run_scenarios(self):
        scenarios = {}

        # BASE — just instantiate normally
        scenarios["Base"] = self.build_forecast()
        # BEAR — deepcopy so we don't mutate the base instance
        
        bear = copy.deepcopy(self)
        for svc in bear.services:
            bear.services[svc]["sessions_per_month"] = int(
                bear.services[svc]["sessions_per_month"] * 0.70
            )
        bear.fixed_opex["Rent (SF/Oakland avg)"] = 16_000
        scenarios["Bear"] = bear.build_forecast()

        # BULL — deepcopy as well
        bull = copy.deepcopy(self)
        for svc in bull.services:
            bull.services[svc]["sessions_per_month"] = int(
                bull.services[svc]["sessions_per_month"] * 1.25
            )
            bull.services[svc]["avg_price"] *= 1.10
        scenarios["Bull"] = bull.build_forecast()

        return scenarios



