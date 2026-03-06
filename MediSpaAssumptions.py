class MediSpaBase:
    def __init__(self):
        self.services = {
            "Botox/Fillers":    {"avg_price": 650,  "sessions_per_month": 120, "growth_rate": 0.05},
            "Laser Treatments": {"avg_price": 400,  "sessions_per_month": 80,  "growth_rate": 0.06},
            "Facials/Skincare": {"avg_price": 180,  "sessions_per_month": 200, "growth_rate": 0.04},
            "Body Contouring":  {"avg_price": 900,  "sessions_per_month": 40,  "growth_rate": 0.07},
            "IV Therapy":       {"avg_price": 250,  "sessions_per_month": 60,  "growth_rate": 0.08},
            "Retail Products":  {"avg_price": 120,  "sessions_per_month": 150, "growth_rate": 0.03},
        }

        self.cogs_pct = {
            "Botox/Fillers":    0.30,
            "Laser Treatments": 0.15,
            "Facials/Skincare": 0.20,
            "Body Contouring":  0.12,
            "IV Therapy":       0.35,
            "Retail Products":  0.50,
        }

        self.fixed_opex = {
            "Rent (SF/Oakland avg)": 12_000,
            "Staff Salaries":        45_000,
            "Medical Director":       8_000,
            "Marketing/SEO":          5_000,
            "Software/EMR":             800,
            "Insurance (med mal)":    2_500,
            "Utilities":              1_800,
            "Supplies (non-COGS)":    1_500,
            "Misc/Admin":             1_200,
        }

        self.variable_opex_pct = 0.04

        self.initial_investment = {
            "Equipment":              180_000,
            "Leasehold Improvements": 120_000,
            "Licenses/Legal":          15_000,
            "Working Capital":         80_000,
            "Marketing Launch":        25_000,
        }

        self.receivables_days = 5
        self.payables_days    = 30
        self.tax_rate         = 0.28
        self.months           = 36

class MediSpaSola:
    def __init__(self):
        self.services = {
            "Premium Facial": {"avg_price": 150,  "sessions_per_month": 3, "growth_rate": 0.04},
            "European Facial": {"avg_price": 120,  "sessions_per_month": 5, "growth_rate": 0.04},
            "Express Facial": {"avg_price": 90,  "sessions_per_month": 21, "growth_rate": 0.06},
            "Lux Facial": {"avg_price": 150,  "sessions_per_month": 4, "growth_rate": 0.04},
            "Microderm Facial": {"avg_price": 150,  "sessions_per_month": 10, "growth_rate": 0.05},
            "Gentelmen's Facial": {"avg_price": 100,  "sessions_per_month": 3, "growth_rate": 0.04},
            "Hand Treatment": {"avg_price": 10,  "sessions_per_month": 25, "growth_rate": 0.07},
            "Lash Tint": {"avg_price": 30,  "sessions_per_month": 15, "growth_rate": 0.07},
            "Brow Tint": {"avg_price": 20,  "sessions_per_month": 16, "growth_rate": 0.08},
            "Retail Products":  {"avg_price": 120,  "sessions_per_month": 75, "growth_rate": 0.03},
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

        self.receivables_days = 5
        self.payables_days    = 30
        self.tax_rate         = 0.28
        self.months           = 36


class MediAssumptions:
    def __init__(self,operating_hours_per_day=8, days_open_per_month=12):
        self.minutes_open_month = operating_hours_per_day * days_open_per_month * 60
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

        self.receivables_days = 5
        self.payables_days    = 30
        self.tax_rate         = 0.28
        self.months           = 36

    def utilization(self):
        minutes_open_month = self.minutes_open_month
        time_month = [i[1]["time_per_session"] * i[1]["sessions_per_month"] for i in self.services.items()]

        run_down = {
            "minutes_open_month": minutes_open_month,
            "total_time_month": sum(time_month),
            "utilization_pct": str(round(sum(time_month)/minutes_open_month * 100, 2)) + "%"
        }

        return run_down



